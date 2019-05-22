import json

from django.contrib.auth.models import User

from .models import Event, Comment, Channel


def event_list_serializer(events):
    event_list = []
    for event in events:
        fields = {'id': event.id,
                  'title': event.title,
                  'timestamp': event.timestamp,
                  'channel_id': event.channel_id,
                  }
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
        fields = {'id': comment.id,
                  'title': comment.title,
                  'content': comment.content,
                  'user_id': comment.user_id,
                  }
        comment_list.append(fields)
    return json.dumps(comment_list)


def comment_serializer(comment):
    fields = {'id': comment.id,
              'event_id': comment.event_id,
              'title': comment.title,
              'content': comment.content,
              'user_id': comment.user_id,
              }
    return json.dumps(fields)


def event_deserializer(data):
    channel = Channel.objects.get(pk=data['channel_id'])
    return Event(**data, channel=channel)


def comment_deserializer(data):
    event = Event.objects.get(pk=data['event_id'])
    user = User.objects.get(pk=data['user_id'])
    return Comment(**data, event=event, user=user)
