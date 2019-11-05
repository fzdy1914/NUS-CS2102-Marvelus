from luminus.managers import course_manager, prof_manager
from luminus.responses import success_json_response, error_json_response


def get_courses(request):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        puname = prof_manager.get_prof_by_username(uname)
        if len(puname) > 0:
            return get_courses_by_puname(request, uname)

        return success_json_response({'courses': course_manager.get_course_by_suname(uname)})
    return error_json_response("User not logged in")


def get_assists(request):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        return success_json_response({'assists': course_manager.get_course_by_tuname(uname)})
    return error_json_response("User not logged in")


def get_course_by_code(request, code):
    course = course_manager.get_course_by_code(code)
    return success_json_response({'course': course[0]})


def get_courses_by_puname(request, puname):
    courses = course_manager.get_course_by_puname(puname)
    return success_json_response({'courses': courses})


def get_courses_by_tuname(request, tuname):
    courses = course_manager.get_course_by_tuname(tuname)
    return success_json_response({'courses': courses})


def get_courses_by_suname(request, suname):
    courses = course_manager.get_course_by_suname(suname)
    return success_json_response({'courses': courses})


def search_courses(request, keyword):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        course = course_manager.search_courses(keyword, uname)
        return success_json_response({'courses': course})
    return error_json_response("User not logged in")


def get_all_courses(request):
    return search_courses(request, '')
