from django.http import HttpResponse

from luminus.managers import prof_manager


def get_profs_by_username(username):
    profs = prof_manager.get_profs_by_username(username)
    return HttpResponse(str(profs), status=200)


def get_profs_by_coursecode(code):
    profs = prof_manager.get_profs_by_coursecode(code)
    return HttpResponse(str(profs, status=200))
