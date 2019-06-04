import json

from django.contrib.auth.decorators import login_required
from django.db import DataError
from django.views.decorators.csrf import csrf_exempt

from EventCenter.managers import event_manager
from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import event_list_serializer, event_serializer
from EventCenter.views.view_decorators import admin_required


@login_required
@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        return view_event_list(request)

    elif request.method == 'POST':
        return add_event(request)

    return error_json_response('No such API')


@login_required
@csrf_exempt
def event_detail(request, pk):
    if request.method == 'GET':
        return view_event(request, pk)

    elif request.method == 'PUT':
        return edit_event(request, pk)

    elif request.method == 'DELETE':
        return delete_event(request, pk)


def view_event_list(request):
    events = event_manager.all_events()
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


def view_event(request, pk):
    if not event_manager.is_event_exists(pk):
        return error_json_response('No such event')

    event = event_manager.get_event(pk)
    return success_json_response({'event': event_serializer(event)})


@admin_required
def add_event(request):
    try:
        data = json.loads(request.body)

        validation = event_manager.is_valid_event(data)
        if not validation['state']:
            return error_json_response(validation['error'])

        event = event_manager.create_event(data)
    except ValueError:
        return error_json_response('Invalid JSON file')
    except (KeyError, TypeError):
        return error_json_response('Invalid arguments')

    return success_json_response({'event': event_serializer(event)})


@admin_required
def edit_event(request, pk):
    try:
        data = json.loads(request.body)

        validation = event_manager.is_valid_event(data)
        if not validation['state']:
            return error_json_response(validation['error'])

        event = event_manager.update_event(pk, data)
    except ValueError:
        return error_json_response('Invalid JSON file')
    except DataError:
        return error_json_response('Invalid date')
    except (KeyError, TypeError):
        return error_json_response('Invalid arguments')

    return success_json_response({'event': event_serializer(event)})


@admin_required
def delete_event(request, pk):
    if not event_manager.is_event_exists(pk):
        return error_json_response('No such event')

    event_manager.delete_event(pk)
    return success_json_response({'message': 'Event successfully deleted'})
