import json

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Event, Comment, Channel


def event_list_serializer(events):
    event_list = []
    for event in events:
        fields = {'id': event.id, 'title': event.title, 'timestamp': event.timestamp, 'channel': event.channel_id}
        event_list.append(fields)
    return json.dumps(event_list)


def event_serializer(event):
    fields = {'id': event.id,
              'title': event.title,
              'description': event.description,
              'timestamp': event.timestamp,
              'location': event.location,
              'image_url': event.image_url,
              'channel_id': event.channel_id,
              }
    return json.dumps(fields)


def comment_list_serializer(comments):
    comment_list = []
    for comment in comments:
        fields = {'title': comment.title, 'content': comment.content, 'user_id': comment.user_id}
        comment_list.append(fields)
    return json.dumps(comment_list)


def event_deserializer(data):
    channel = Channel.objects.get(pk=data['channel_id'])
    return Event(**data, channel=channel)


def comment_deserializer(data):
    event = Event.objects.get(pk=data['event_id'])
    user = User.objects.get(pk=data['user_id'])
    return Comment(**data, event=event, user=user)


class DetailEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'timestamp', 'location', 'image_url', 'channel')


class BriefEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'timestamp', 'channel')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title', 'content', 'user_id')
