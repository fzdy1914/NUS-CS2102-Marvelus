from luminus.managers import student_manager
from luminus.responses import success_json_response


def get_students_by_coursecode(request, code):
    print(code)
    students = student_manager.get_students_by_coursecode(code)
    print(code)
    return success_json_response({'students': students})


def get_students_by_coursecode_and_groupnum(request, code, group_num):
    students = student_manager.get_students_by_coursecode_and_groupnum(code, group_num)
    return success_json_response({'students': students})


def add_student_to_tut_by_uname_coursecode_groupnum(request, uname, code, group_num):

    student = student_manager.add_student_to_tut_by_uname_coursecode_groupnum(uname, code, group_num)
    return success_json_response({'student':student})


def get_students_noattend_by_coursecode(request, code):
    print(code)
    students = student_manager.get_student_enrolledbutnotattend_by_coursecode(code)
    print(code)
    return success_json_response({'students': students})
