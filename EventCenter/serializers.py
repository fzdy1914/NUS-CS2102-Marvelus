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
    return event_list


def event_serializer(event):
    fields = {'id': event.id,
              'title': event.title,
              'description': event.description,
              'timestamp': event.timestamp,
              'location': event.location,
              'image_url': event.image_url,
              'channel_id': event.channel_id,
              }
    return fields


def comment_list_serializer(comments):
    comment_list = []
    for comment in comments:
        fields = {'id': comment.id,
                  'title': comment.title,
                  'content': comment.content,
                  'user_id': comment.user_id,
                  }
        comment_list.append(fields)
    return comment_list


def comment_serializer(comment):
    fields = {'id': comment.id,
              'event_id': comment.event_id,
              'title': comment.title,
              'content': comment.content,
              'user_id': comment.user_id,
              }
    return fields


def event_deserializer(data):
    channel = Channel.objects.get(pk=data['channel_id'])
    return Event(channel=channel, **data)


def event_updater(event, data):
    event.__dict__.update(**data)
    if 'channel_id' in data:
        event.channel = Channel.objects.get(pk=data['channel_id'])
    return event


def comment_deserializer(data):
    event = Event.objects.get(pk=data['event_id'])
    user = User.objects.get(pk=data['user_id'])
    return Comment(event=event, user=user, **data)
