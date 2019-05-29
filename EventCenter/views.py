import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm
from .responses import success_json_response, error_json_response
from .serializers import event_list_serializer, event_serializer, comment_list_serializer, event_deserializer, \
    comment_deserializer, comment_serializer, event_updater, like_list_serializer, like_deserializer, like_serializer, \
    channel_list_serializer, channel_updater, channel_serializer
from .models import Event, Channel, Comment, Like


@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        print('login access')
        return success_json_response({'user': {'username': request.user.username,
                                               'isAdmin': request.user.is_staff or request.user.is_superuser}})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username + ' ' + password)

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return success_json_response({'user': {'username': request.user.username,
                                                       'isAdmin': request.user.is_staff or request.user.is_superuser}})
            else:
                return error_json_response('Wrong password. Please try again.')
        else:
            return error_json_response('Invalid username')

    return error_json_response('User not logged in.')


@csrf_exempt
def logout(request):
    auth.logout(request)
    return success_json_response({'message': 'Successfully log out'})


@csrf_exempt
def reject(request):
    return error_json_response('User not logged in.')


@login_required
@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        args = request.GET

        try:
            channel_id = args.get('channel_id')
            if channel_id:
                events = events.filter(channel_id=int(channel_id))

            since = args.get('since')
            if since:
                events = events.filter(timestamp__gte=int(since))

            until = args.get('until')
            if until:
                events = events.filter(timestamp__lte=int(until))

            count = events.count()
            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 50))
            events = events.order_by('-id')[offset:offset + limit]
        except ValueError:
            return error_json_response('Invalid arguments')

        return success_json_response({'events': event_list_serializer(events), 'count': count})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            event = event_deserializer(data)
            event.save()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Channel.DoesNotExist:
            return error_json_response('No such channel')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'event': event_serializer(event)})


@login_required
@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return error_json_response('No such event')

    if request.method == 'GET':
        return success_json_response({'event': event_serializer(event)})

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            event = event_updater(event, data)
            event.save()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Channel.DoesNotExist:
            return error_json_response('No such channel')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'event': event_serializer(event)})

    elif request.method == 'DELETE':
        event.delete()
        return success_json_response({'message': 'Event successfully deleted'})


@login_required
@csrf_exempt
def comment_list(request, event_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(event_id=event_id)
        count = comments.count()
        args = request.GET

        try:
            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 50))
        except ValueError:
            return error_json_response('Invalid arguments')

        comments = comments.order_by('-id')[offset:offset + limit]
        return success_json_response({'comments': comment_list_serializer(comments), 'count': count})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            data['event_id'] = event_id
            data['user_id'] = request.user.id
            comment = comment_deserializer(data)
            comment.save()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Event.DoesNotExist:
            return error_json_response('No such event')
        except User.DoesNotExist:
            return error_json_response('No such user')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'comment': comment_serializer(comment)})

    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            comment_id = data['comment_id']
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Comment.DoesNotExist:
            return error_json_response('No such comment')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'message': 'Comment successfully deleted'})


@login_required
@csrf_exempt
def like_list(request, event_id):
    if request.method == 'GET':
        likes = Like.objects.filter(event_id=event_id)
        count = likes.count()
        args = request.GET

        try:
            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 50))
        except ValueError:
            return error_json_response('Invalid arguments')

        likes = likes.order_by('-id')[offset:offset + limit]
        return success_json_response({'likes': like_list_serializer(likes), 'count': count})

    elif request.method == 'POST':
        try:
            data = {'event_id': event_id, 'user_id': request.user.id}
            like = like_deserializer(data)
            if not Like.objects.filter(event_id=event_id, user_id=like.user_id).exists():
                like.save()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Event.DoesNotExist:
            return error_json_response('No such event')
        except User.DoesNotExist:
            return error_json_response('No such user')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'like': like_serializer(like)})

    elif request.method == 'DELETE':
        try:
            like = Like.objects.filter(event_id=event_id, user_id=request.user.id)
            if like.exists():
                like.delete()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Event.DoesNotExist:
            return error_json_response('No such event')
        except User.DoesNotExist:
            return error_json_response('No such user')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'message': 'Successfully unliked'})


@login_required
@csrf_exempt
def channel_list(request):
    if request.method == 'GET':
        args = request.GET
        try:
            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 10))
        except ValueError:
            return error_json_response('Invalid arguments')

        count = Channel.objects.all().count()
        channels = Channel.objects.all().order_by('-id')[offset:offset + limit]
        return success_json_response({'channels': channel_list_serializer(channels),
                                      'count': count})

    elif request.method == 'POST':
        if not is_admin(request):
            return error_json_response('Authority required')
        try:
            data = json.loads(request.body)
            channel = Channel.objects.get(pk=data['id'])
            channel = channel_updater(channel, data)
            channel.save()
        except IntegrityError:
            return error_json_response('Duplicated Channel Name')
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Event.DoesNotExist:
            return error_json_response('No such event')
        except User.DoesNotExist:
            return error_json_response('No such user')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'channel': channel_serializer(channel)})

    elif request.method == 'DELETE':
        if not is_admin(request):
            return error_json_response('Authority required')
        try:
            data = json.loads(request.body)
            channel = Channel.objects.get(pk=data['id'])
            channel.delete()
        except ValueError:
            return error_json_response('Invalid JSON file')
        except Event.DoesNotExist:
            return error_json_response('No such event')
        except User.DoesNotExist:
            return error_json_response('No such user')
        except (KeyError, TypeError):
            return error_json_response('Invalid arguments')

        return success_json_response({'message': 'Channel Successfully deleted'})


def is_admin(request):
    return request.user.is_superuser or request.user.is_staff
