import json
import logging

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from EventCenter.managers import channel_manager
from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import channel_list_serializer, channel_serializer
from EventCenter.views.view_decorators import admin_required, json_request, args_request

logger = logging.getLogger('django')


@login_required
@csrf_exempt
def channel_list(request):
    if request.method == 'GET':
        return view_channel_list(request)

    elif request.method == 'POST':
        return create_channel(request)

    elif request.method == 'PUT':
        return edit_channel(request)

    elif request.method == 'DELETE':
        return delete_channel(request)

    return error_json_response('No such API')


@args_request
def view_channel_list(request):
    args = request.GET
    offset = int(args.get('offset', 0))
    limit = int(args.get('limit', 10))

    return success_json_response({'channels': channel_list_serializer(channel_manager.get_channels(offset, limit)),
                                  'count': channel_manager.count()})


@json_request
@admin_required
def create_channel(request):
    data = json.loads(request.body)
    validation = channel_manager.is_valid_channel(data)
    if not validation['state']:
        return error_json_response(validation['error'])

    channel = channel_manager.create_channel(data)
    logger.info('User: %s, Add Channel: [id: %s, name: %s]' % (request.user.id, channel.id, channel.name))

    return success_json_response({'channel': channel_serializer(channel)})


@json_request
@admin_required
def edit_channel(request):
    data = json.loads(request.body)
    channel_id = data['id']
    if not channel_manager.is_channel_exists(channel_id):
        return error_json_response('No such channel')

    validation = channel_manager.is_valid_channel(data)
    if not validation['state']:
        return error_json_response(validation['error'])

    channel = channel_manager.update_channel(channel_id, data)
    logger.info('User: %s, Edit Channel: [id: %s, name: %s]' % (request.user.id, channel.id, channel.name))

    return success_json_response({'channel': channel_serializer(channel)})


@json_request
@admin_required
def delete_channel(request):
    data = json.loads(request.body)
    channel_id = data['id']
    if not channel_manager.is_channel_exists(channel_id):
        return error_json_response('No such channel')

    channel_manager.delete_channel(channel_id)
    logger.info('User: %s, Delete Channel: [id: %s]' % (request.user.id, channel_id))

    return success_json_response({'message': 'Channel Successfully deleted'})


