from django.http import HttpResponse

from luminus.managers import forum_manager


def get_forum_by_code(request, code):
    forums = forum_manager.get_forum_by_code(code)
    return HttpResponse(str(forums), status=200)


def get_forum_by_code_and_group_num(request, code, group_num):
    forums = forum_manager.get_forum_by_code_and_group_num(code, group_num)
    return HttpResponse(str(forums), status=200)
