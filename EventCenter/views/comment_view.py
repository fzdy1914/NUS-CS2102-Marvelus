import json
import logging

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import comment_list_serializer, comment_serializer
from EventCenter.managers import comment_manager
from EventCenter.views.view_decorators import json_request, args_request

logger = logging.getLogger('django')


@login_required
@csrf_exempt
def comment_list(request, event_id):
    if request.method == 'GET':
        return view_comment_list(request, event_id)

    elif request.method == 'POST':
        return add_comment(request, event_id)

    return error_json_response('No such API')

    # elif request.method == 'DELETE':
    #     try:
    #         data = json.loads(request.body)
    #         comment_id = data['comment_id']
    #         comment = Comment.objects.get(pk=comment_id)
    #         comment.delete()
    #     except ValueError:
    #         return error_json_response('Invalid JSON file')
    #     except Comment.DoesNotExist:
    #         return error_json_response('No such comment')
    #     except (KeyError, TypeError):
    #         return error_json_response('Invalid arguments')
    #
    #     return success_json_response({'message': 'Comment successfully deleted'})


@cache_page(60)
@args_request
def view_comment_list(request, event_id):
    args = request.GET

    offset = int(args.get('offset', 0))
    limit = int(args.get('limit', 50))

    comments = comment_list_serializer(comment_manager.get_comments(offset, limit, event_id))
    return success_json_response({'comments': comments, 'count': comment_manager.count(event_id)})


@json_request
def add_comment(request, event_id):
    data = json.loads(request.body)
    data['event_id'] = event_id
    data['user_id'] = request.user.id
    validation = comment_manager.is_valid_comment(data)
    if not validation['state']:
        return error_json_response(validation['error'])

    comment = comment_manager.add_comment(data)
    logger.info('User: %s, Add Comment: [event_id: %s, id: %s]' % (request.user.id, event_id, comment.id))
    return success_json_response({'comment': comment_serializer(comment)})

