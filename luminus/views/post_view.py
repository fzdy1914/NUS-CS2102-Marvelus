from django.http import HttpResponse

from luminus.managers import post_manager
from luminus.responses import success_json_response


def get_posts_by_code_and_fid(request, code, fid):
    posts = post_manager.get_posts_by_code_and_fid(code, fid)
    return success_json_response({'posts': posts})


def get_posts_by_code_and_fid_and_pid(request, code, fid, pid):
    post = post_manager.get_post_by_code_and_fid_and_pid(code, fid, pid)
    replies = post_manager.get_replies_by_code_and_fid_and_pid(code, fid, pid)
    return success_json_response({'post': post[0], 'replies': replies})
