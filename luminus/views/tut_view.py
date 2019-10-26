from django.http import HttpResponse

from luminus.managers import tutorial_manager
from luminus.responses import success_json_response



def get_tutorials_by_coursecode(request, code):
    tutorial = tutorial_manager.get_tutorials_by_coursecode(code)
    return success_json_response({'tutorials': tutorial})


def get_tutorials_by_student(request, username):
    tutorial = tutorial_manager.get_tutorials_by_student(username)
    return HttpResponse(str(tutorial), status=200)


def get_tutorials_by_tA_and_course(request, username, code):
    tutorial = tutorial_manager.get_tutorials_by_tA_and_course(username, code)
    return HttpResponse(str(tutorial), status=200)


def get_tutorials_by_course_and_group(request, code, num):
    tutorial = tutorial_manager.get_tutorials_by_course_and_group(code, num)
    return HttpResponse(str(tutorial), status=200)
