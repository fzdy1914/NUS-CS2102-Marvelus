# quick way to add events
import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Channel, Event, Comment, Like


def add_channels(request):
    Channel.objects.create(name='none')
    for i in range(2, 15):
        name = 'channel ' + str(i)
        Channel.objects.create(name=name)
    return HttpResponse('Channel added', status=200)


def add_events(request):
    for i in range(1, 301):
        title = 'event ' + str(i)
        description = 'description ' + title
        timestamp = 611111111 + 100000 * i
        channel_id = random.randint(1, 15)
        channel = Channel.objects.get(pk=channel_id)
        e = Event(title=title, description=description, timestamp=timestamp, channel=channel)
        e.save()
    return HttpResponse('Event added', status=200)


# quick way to add users
def add_users(request):
    for i in range(2, 101):
        username = 'user ' + str(i)
        password = '123456'
        u = User(username=username, password=password, is_superuser=False)
        u.save()
    return HttpResponse('User added', status=200)


# quick way to add comments
def add_comments(request):
    for event in Event.objects.all():
        for i in range(1, 101):
            title = "Event " + event.title + " comment " + str(i)
            content = "Content " + event.title + " comment " + str(i)
            user_id = random.randint(1, 100)
            user = User.objects.get(id=user_id)
            c = Comment(event=event, title=title, content=content, user=user)
            c.save()
    return HttpResponse('Comment added', status=200)


def add_likes(request):
    for event in Event.objects.all():
        for i in random.sample(range(1, 100), 20):
            user = User.objects.get(id=i)
            like = Like(user=user, event=event)
            like.save()
    return HttpResponse("Like added", status=200)


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


