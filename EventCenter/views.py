import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .responses import success_json_response, error_json_response
from .serializers import event_list_serializer, event_serializer, comment_list_serializer, event_deserializer, \
    comment_deserializer, comment_serializer, event_updater
from .models import Event, Channel, Comment


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

            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 100))
            events = events.order_by('-id')[offset:offset + limit]
        except ValueError:
            return JsonResponse(error_json_response('Invalid arguments'))

        return JsonResponse(success_json_response('events', event_list_serializer(events)))

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            event = event_deserializer(data)
            event.save()
        except ValueError:
            return JsonResponse(error_json_response('Invalid JSON file'))
        except Channel.DoesNotExist:
            return JsonResponse(error_json_response('Invalid channel'))
        except (KeyError, TypeError):
            return JsonResponse(error_json_response('Invalid arguments'))

        return JsonResponse(success_json_response('event', event_serializer(event)))


@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return JsonResponse(error_json_response('No such event'))

    if request.method == 'GET':
        return JsonResponse(success_json_response('event', event_serializer(event)))

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            event = event_updater(event, data)
            event.save()
        except ValueError:
            return JsonResponse(error_json_response('Invalid JSON file'))
        except Channel.DoesNotExist:
            return JsonResponse(error_json_response('Invalid channel'))
        except (KeyError, TypeError):
            return JsonResponse(error_json_response('Invalid arguments'))

        return JsonResponse(success_json_response('event', event_serializer(event)))

    elif request.method == 'DELETE':
        event.delete()
        return JsonResponse(success_json_response('message', 'Event successfully deleted'))


@csrf_exempt
def comment_list(request, event_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(event_id=event_id)
        args = request.GET

        try:
            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 50))
        except ValueError:
            return JsonResponse(error_json_response('Invalid arguments'))

        comments = comments.order_by('-id')[offset:offset + limit]
        return JsonResponse(success_json_response('comments', comment_list_serializer(comments)))

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            data['event_id'] = event_id
            comment = comment_deserializer(data)
            comment.save()
        except ValueError:
            return JsonResponse(error_json_response('Invalid JSON file'))
        except Event.DoesNotExist:
            return JsonResponse(error_json_response('Invalid event'))
        except User.DoesNotExist:
            return JsonResponse(error_json_response('Invalid user'))
        except (KeyError, TypeError):
            return JsonResponse(error_json_response('Invalid arguments'))

        return JsonResponse(success_json_response('comment', comment_serializer(comment)))
