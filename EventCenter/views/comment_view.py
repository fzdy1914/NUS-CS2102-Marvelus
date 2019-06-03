import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import comment_list_serializer, comment_serializer
from EventCenter.managers import comment_manager


@login_required
@csrf_exempt
def comment_list(request, event_id):
    if request.method == 'GET':
        return view_comment_list(request, event_id)

    elif request.method == 'POST':
        return add_comment(request, event_id)

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


def view_comment_list(request, event_id):
    comments = comment_manager.all_comments(event_id)
    args = request.GET

    try:
        offset = int(args.get('offset', 0))
        limit = int(args.get('limit', 50))
    except ValueError:
        return error_json_response('Invalid arguments')

    comments = comments.order_by('-id')[offset:offset + limit]
    return success_json_response({'comments': comment_list_serializer(comments),
                                  'count': comment_manager.count(event_id)})


def add_comment(request, event_id):
    try:
        data = json.loads(request.body)
        data['event_id'] = event_id
        data['user_id'] = request.user.id
        validation = comment_manager.is_valid_comment(data)
        if not validation['state']:
            return error_json_response(validation['error'])

        comment = comment_manager.add_comments(data)
    except ValueError:
        return error_json_response('Invalid JSON file')
    except (KeyError, TypeError):
        return error_json_response('Invalid arguments')

    return success_json_response({'comment': comment_serializer(comment)})

