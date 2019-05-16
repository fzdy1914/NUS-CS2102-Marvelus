from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Event


def index(request):
    latest_event_list = Event.objects.order_by('id')[:5]
    context = {
        'latest_event_list': latest_event_list,
    }
    return render(request, 'EventCenter/index.html', context)


def event_detail(request, event_id):
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
