# quick way to add events
import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Channel, Event, Comment, Like


def add_events(request):
    for i in range(1, 100):
        title = str(i + 300)
        description = 'event ' + title
        timestamp = 511111111 + 1000 * i
        channel = Channel.objects.all()[1]
        e = Event(title=title, description=description, timestamp=timestamp, channel=channel)
        e.save()
    return HttpResponse(status=200)


# quick way to add users
def add_users(request):
    for i in range(3, 101):
        username = 'user ' + str(i)
        password = '123456'
        u = User(username=username, password=password, is_superuser=False)
        u.save()
    return HttpResponse('add user success', status=200)


# quick way to add comments
def add_comments(request):
    for event in Event.objects.all():
        for i in range(1, 101):
            title = "Event " + event.title + " comment " + str(i)
            content = "Content " + event.title + " comment " + str(i)
            user = User.objects.get(username='root')
            c = Comment(event=event, title=title, content=content, user=user)
            c.save()
    return HttpResponse(status=200)


def add_likes(request):
    Like.objects.all().delete()
    for event in Event.objects.all():
        for i in random.sample(range(1, 100), 20):
            user = User.objects.get(id=i)
            like = Like(user=user, event=event)
            like.save()
    return HttpResponse("add like success", status=200)


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


