import json
import logging

from django.contrib.auth.decorators import login_required
from django.db import DataError
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from EventCenter.managers import event_manager
from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import event_list_serializer, event_serializer
from EventCenter.views.view_decorators import admin_required, json_request, args_request

logger = logging.getLogger('django')


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

    return error_json_response('No such API')


@cache_page(60)
@args_request
def view_event_list(request):
    args = request.GET

    channel_id = args.get('channel_id')
    since = args.get('since')
    until = args.get('until')

    offset = int(args.get('offset', 0))
    limit = int(args.get('limit', 50))
    res = event_manager.get_events(offset, limit, channel_id, since, until)

    return success_json_response({'events': event_list_serializer(res['events']), 'count': res['count']})


@cache_page(60)
def view_event(request, pk):
    if not event_manager.is_event_exists(pk):
        return error_json_response('No such event')

    event = event_manager.get_event(pk)

    return success_json_response({'event': event_serializer(event)})


@json_request
@admin_required
def add_event(request):
    data = json.loads(request.body)

    validation = event_manager.is_valid_event(data)
    if not validation['state']:
        return error_json_response(validation['error'])

    event = event_manager.create_event(data)
    logger.info('User: %s, Add Event: [id: %s]' % (request.user.id, event.id))

    return success_json_response({'event': event_serializer(event)})


@json_request
@admin_required
def edit_event(request, pk):
    try:
        data = json.loads(request.body)

        validation = event_manager.is_valid_event(data)
        if not validation['state']:
            return error_json_response(validation['error'])

        event = event_manager.update_event(pk, data)
        logger.info('User: %s, Edit Event: [id: %s]' % (request.user.id, event.id))
    except DataError:
        return error_json_response('Invalid date')

    return success_json_response({'event': event_serializer(event)})


@admin_required
def delete_event(request, pk):
    if not event_manager.is_event_exists(pk):
        return error_json_response('No such event')

    event_manager.delete_event(pk)
    logger.info('User: %s, Delete Event: [id: %s]' % (request.user.id, pk))
    return success_json_response({'message': 'Event successfully deleted'})
