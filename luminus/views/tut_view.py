from django.http import HttpResponse

from luminus.managers import tutorial_manager
from luminus.responses import success_json_response, error_json_response


def get_tutorials_by_coursecode(request, code):
    tutorials = tutorial_manager.get_tutorials_by_coursecode(code)
    return success_json_response({'tutorials':tutorials})
    # return HttpResponse(str(tutorial), status=200)


def get_tutorials_by_student(request, username):
    tutorials = tutorial_manager.get_tutorials_by_student(username)
    return success_json_response({'tutorials': tutorials})
    # return HttpResponse(str(tutorial), status=200)


def get_tutorials_by_tA_and_course(request, username, code):
    tutorials = tutorial_manager.get_tutorials_by_tA_and_course(username, code)
    return success_json_response({'tutorials': tutorials})
    # return HttpResponse(str(tutorial), status=200)


def get_tutorials_by_course_and_group(request, code, num):
    tutorials = tutorial_manager.get_tutorials_by_course_and_group(code, num)
    return success_json_response({'tutorials': tutorials})
    # return HttpResponse(str(tutorial), status=200)
