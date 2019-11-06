import json

from django.views.decorators.csrf import csrf_exempt

from luminus.managers import post_manager
from luminus.responses import success_json_response, error_json_response
from luminus.view_decorators import json_request


def get_posts_by_code_and_fid(request, code, fid):
    posts = post_manager.get_posts_by_code_and_fid(code, fid)
    return success_json_response({'posts': posts})


def get_posts_by_code_and_fid_and_pid(request, code, fid, pid):
    post = post_manager.get_post_by_code_and_fid_and_pid(code, fid, pid)
    replies = post_manager.get_replies_by_code_and_fid_and_pid(code, fid, pid)
    return success_json_response({'post': post, 'replies': replies})


@json_request
@csrf_exempt
def add_post(request):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        data = json.loads(request.body)
        post = post_manager.add_post(data['code'], data['fid'], data['title'], data['content'], uname)
        return success_json_response({'post': post})
    return error_json_response("User not logged in")


@json_request
@csrf_exempt
def add_reply(request):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        data = json.loads(request.body)
        post = post_manager.add_reply(data['code'], data['fid'], data['pid'], data['title'], data['content'], uname)
        return success_json_response({'reply': post})
    return error_json_response("User not logged in")


def delete_post(request, code, fid, pid):
    post_manager.delete_post(code, fid, pid)
    return success_json_response({})
