from luminus.managers import student_manager
from luminus.responses import success_json_response
from luminus.responses import error_json_response
import math


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


def calculate_final_grade(request, code, a, b, c, d, e, f):
    if float(a)+float(b)+float(c)+float(d)+float(e)+float(f)!= 100:
        print(float(a)+float(b)+float(c)+float(d)+float(e)+float(f))
        return error_json_response({'error':'Sum not equal to 1' })
    else:
        amount = student_manager.retrieve_complete_amount(code)
        amount = amount[0]['count(*)']
        print(amount)
        a = math.ceil(amount * float(a) / 100.0)
        b = math.ceil(amount * float(b) / 100.0)
        c = math.ceil(amount * float(c) / 100.0)
        d = math.ceil(amount * float(d) / 100.0)
        e = math.ceil(amount * float(e) / 100.0)
        f = math.ceil(amount * float(f) / 100.0)

        enrolls = student_manager.calculate_final_grade(code, a, a + b, a + b + c, a + b + c + d, a + b + c + d + e, a + b + c + d + e + f)

        print(enrolls[0]['uname'])
        print(enrolls[0]['code'])
        print(enrolls[0]['final_result'])

        for enroll in enrolls:
            student_manager.update_final_grade(enroll['uname'], enroll['code'], enroll['final_result'])


        enrolls = student_manager.retrieve_after_grading(code)

        return success_json_response({'enrolls': enrolls})

        # enrolls = student_manager.calculate_final_grade(code, a, b, c, d, e, f)
