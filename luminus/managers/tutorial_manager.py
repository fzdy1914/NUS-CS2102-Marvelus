from luminus import sql_helper


def get_tutorials_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT group_num FROM Tutorials NATURAL JOIN Attend WHERE code= %(code)s", {'code': code})


def get_tutorials_by_student(username):
    return sql_helper.fetchall_to_dict("SELECT * FROM Attend NATURAL JOIN tutorials WHERE uname = %(username)s", {'username': username})


def get_tutorials_by_tA_and_course(username, code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Facilitate WHERE uname=%(username)s AND code=%(code)s ", {'code': code, 'username': username})


def get_tutorials_by_course_and_group(code, num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Tutorials WHERE code=%(code)s AND group_num=%(num)s", {'code': code, 'num': num})
