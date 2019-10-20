from luminus.managers import prof_manager
from luminus.responses import success_json_response


def get_prof_by_username(request, username):
    profs = prof_manager.get_prof_by_username(username)
    return success_json_response({'profs': profs})


def get_profs_by_coursecode(request, code):
    profs = prof_manager.get_profs_by_coursecode(code)
    return success_json_response({'profs': profs})
