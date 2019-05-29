from django.contrib.auth.models import User

from .models import Event, Comment, Channel, Like


def event_list_serializer(events):
    event_list = []
    for event in events:
        fields = {'id': event.id,
                  'title': event.title,
                  'timestamp': event.timestamp,
                  'channel': event.channel.name,
                  'likes': Like.objects.filter(event=event).count()
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
              'channel': event.channel.name,
              'likes': Like.objects.filter(event=event).count()
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


def comment_list_serializer(comments):
    comment_list = []
    for comment in comments:
        comment_list.append(comment_serializer(comment))
    return comment_list


def comment_serializer(comment):
    fields = {'id': comment.id,
              'title': comment.title,
              'content': comment.content,
              'user_id': comment.user_id,
              'username': comment.user.username
              }
    return fields


def comment_deserializer(data):
    event = Event.objects.get(pk=data['event_id'])
    user = User.objects.get(pk=data['user_id'])
    return Comment(event=event, user=user, **data)


def like_list_serializer(likes):
    like_list = []
    for like in likes:
        like_list.append(like_serializer(like))
    return like_list


def like_serializer(like):
    fields = {'user_id': like.user_id,
              'username': like.user.username,
              }
    return fields


def like_deserializer(data):
    event = Event.objects.get(pk=data['event_id'])
    user = User.objects.get(pk=data['user_id'])
    return Like(event=event, user=user)


def channel_list_serializer(channels):
    channel_list = []
    for channel in channels:
        fields = {'id': channel.id,
                  'name': channel.name,
                  }
        channel_list.append(fields)
    return channel_list
