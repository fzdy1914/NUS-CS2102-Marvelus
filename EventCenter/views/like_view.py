from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import like_list_serializer, like_serializer
from EventCenter.managers import like_manager
from EventCenter.views.view_decorators import args_request


@login_required
@csrf_exempt
def like_list(request, event_id):
    if request.method == 'GET':
        return view_like_list(request, event_id)

    elif request.method == 'POST':
        return add_like(request, event_id)

    elif request.method == 'DELETE':
        return remove_like(request, event_id)

    return error_json_response('No such API')


@args_request
def view_like_list(request, event_id):
    likes = like_manager.all_likes(event_id)
    count = likes.count()
    args = request.GET

    offset = int(args.get('offset', 0))
    limit = int(args.get('limit', 50))

    likes = likes.order_by('-id')[offset:offset + limit]
    return success_json_response({'likes': like_list_serializer(likes), 'count': count})


def add_like(request, event_id):
    data = {'event_id': event_id, 'user_id': request.user.id}
    validation = like_manager.is_valid_like(data)
    if not validation['state']:
        return error_json_response(validation['error'])

    like = like_manager.add_like(data)

    return success_json_response({'like': like_serializer(like)})


def remove_like(request, event_id):
    data = {'event_id': event_id, 'user_id': request.user.id}
    validation = like_manager.is_valid_like(data)
    if not validation['state']:
        return error_json_response(validation['error'])

    like_manager.delete_like(data)

    return success_json_response({'message': 'Successfully unliked'})
