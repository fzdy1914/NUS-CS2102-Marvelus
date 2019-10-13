from django.http import HttpResponse

from luminus.managers import post_manager


def get_post_by_code_and_fid(request, code, fid):
    posts = post_manager.get_post_by_code_and_fid(code, fid)
    return HttpResponse(str(posts), status=200)


def get_post_by_code_and_fid_and_pid(request, code, fid, pid):
    posts = post_manager.get_post_by_code_and_fid_and_pid(code, fid, pid)
    return HttpResponse(str(posts), status=200)
