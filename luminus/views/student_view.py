from django.http import HttpResponse

from luminus.managers import student_manager


def get_students_by_coursecode(request, code):
    students = student_manager.get_students_by_coursecode(code)
    return HttpResponse(str(students), status=200)


def get_students_by_coursecode_and_groupnum(request, code, group):
    students = student_manager.get_students_by_coursecode_and_groupnum(code, group)
    return HttpResponse(str(students), status=200)
