from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from .serializers import DetailEventSerializer, BriefEventSerializer
from .models import Event, Channel


@login_required
def index(request):
    latest_event_list = Event.objects.order_by('id')[:5]
    context = {
        'latest_event_list': latest_event_list,
    }
    return render(request, 'EventCenter/index.html', context)


@login_required
def event_detail_a(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'EventCenter/event_detail.html', context)


class IndexView(generic.ListView):
    template_name = 'EventCenter/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five events."""
        return Event.objects.order_by('id')[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = 'EventCenter/event_detail.html'


@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()

        try:
            channel_id = request.GET.get('channel', None)
            if channel_id:
                events = events.filter(channel_id=int(channel_id))

            since = request.GET.get('since', None)
            if since:
                events = events.filter(timestamp__gte=int(since))

            until = request.GET.get('until', None)
            if until:
                events = events.filter(timestamp__lte=int(until))

            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 100))
            events = events.order_by('-id')[offset: offset + limit]
        except ValueError:
            return HttpResponse('Invalid arguments', status=400)

        serializer = BriefEventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse('Invalid JSON file', status=400)

        serializer = DetailEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DetailEventSerializer(event)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetailEventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)


# quick way to add events
def add_events(request):
    for i in range(1, 100):
        title = str(i + 300)
        description = 'event ' + title
        timestamp = 511111111 + 1000 * i
        channel = Channel.objects.all()[1]
        e = Event(title=title, description=description, timestamp=timestamp, channel=channel)
        e.save()
    return HttpResponse(status=200)

