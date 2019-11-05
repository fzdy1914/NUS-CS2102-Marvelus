from luminus.managers import student_manager
from luminus.responses import success_json_response, error_json_response


def get_students_by_coursecode(request, code):
    students = student_manager.get_students_by_coursecode(code)
    return success_json_response({'students': students})


def get_students_by_coursecode_and_groupnum(request, code, group_num):
    students = student_manager.get_students_by_coursecode_and_groupnum(code, group_num)
    return success_json_response({'students': students})


def add_student_to_tut_by_uname_coursecode_groupnum(request, uname, code, group_num):
    student = student_manager.add_student_to_tut_by_uname_coursecode_groupnum(uname, code, group_num)
    return success_json_response({'student':student})


def get_students_noattend_by_coursecode(request, code):
    students = student_manager.get_student_enrolledbutnotattend_by_coursecode(code)
    return success_json_response({'students': students})


def get_requests_by_coursecode(request, code):
    students = student_manager.get_requests_by_coursecode(code)
    return success_json_response({'students': students})


def approve_requests(request, uname, code):
    student = student_manager.approve_requests(uname, code)
    return success_json_response({'student': student})


def reject_requests(request, uname, code):
    student = student_manager.reject_requests(uname, code)
    return success_json_response({'student': student})


def get_ta_candidates_by_coursecode(request, code):
    students = student_manager.get_ta_candidates_by_coursecode(code)
    return success_json_response({'students': students})


def add_ta_by_uname_coursecode_group(request, uname, code):
    ta = student_manager.add_ta_by_uname_coursecode_group(uname, code)
    return success_json_response({'ta': ta})


def get_students_by_student_uname_and_coursecode(request, uname, code):
    students = student_manager.get_students_by_student_uname_and_coursecode(uname, code)
    return success_json_response({'students': students})


def get_students_by_coursecode_and_status(request, code, status):
    students = student_manager.get_students_by_coursecode_and_status(code, status)
    return success_json_response({'students': students})


def update_testgrade_by_uname_and_code(request, uname, code, grade):
    student = student_manager.update_testgrade_by_uname_and_code(uname, code, grade)
    return success_json_response({'student': student})


def add_enroll_request_by_uname_and_code(request, code):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        students = student_manager.add_enroll_request_by_uname_and_code(uname, code)
        return success_json_response({'students': students})
    return error_json_response("User not logged in")
