from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import DetailEventSerializer, BriefEventSerializer
from .models import Event

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
        snippets = Event.objects.all()
        serializer = BriefEventSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetailEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def event_detail(request, pk):
    try:
        snippet = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DetailEventSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetailEventSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
