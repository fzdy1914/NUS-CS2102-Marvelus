from luminus.managers import tutorial_manager
from luminus.responses import success_json_response


def get_tutorials_by_coursecode(request, code):
    tutorial = tutorial_manager.get_tutorials_by_coursecode(code)
    return success_json_response({'tutorials': tutorial})


def get_tutorials_by_student(request, username):
    tutorials = tutorial_manager.get_tutorials_by_student(username)
    return success_json_response({'tutorials': tutorials})


def get_tutorials_by_tA_and_course(request, username, code):
    tutorials = tutorial_manager.get_tutorials_by_tA_and_course(username, code)
    return success_json_response({'tutorials': tutorials})


def get_tutorials_by_course_and_group(request, code, num):
    tutorials = tutorial_manager.get_tutorials_by_course_and_group(code, num)
    return success_json_response({'tutorials': tutorials})

def add_stu_to_attendance_by_uname_code_group_num(request, uname, code, group_num, attend_week):
    attendance = tutorial_manager.add_stu_to_attendance_by_uname_code_group_num(uname, code, group_num, attend_week)
    return success_json_response({'attendance': attendance})

def retrieve_attendance_by_uname_code_group_num(request,uname, code, group_num):
    attendances = tutorial_manager.retrieve_attendance_by_uname_code_group_num(uname, code, group_num)
    return success_json_response({'attendances': attendances})