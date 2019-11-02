from luminus.managers import student_manager
from luminus.responses import success_json_response


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


def get_students_by_coursecode_enrolled(request, code):
    students = student_manager.get_students_by_coursecode_enrolled(code)
    return success_json_response({'students': students})


def get_students_by_coursecode_completed(request, code):
    students = student_manager.get_students_by_coursecode_completed(code)
    return success_json_response({'students': students})


def get_students_by_coursecode_rejected(request, code):
    students = student_manager.get_students_by_coursecode_rejected(code)
    return success_json_response({'students': students})


def get_students_by_coursecode_requesting(request, code):
    students = student_manager.get_students_by_coursecode_requesting(code)
    return success_json_response({'students': students})
