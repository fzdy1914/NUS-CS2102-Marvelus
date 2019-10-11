from luminus import sql_helper


def get_students_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT name, email, major FROM Users NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE code = %(code)s", {'code': code})


def get_students_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT name, email, major FROM Users NATURAL JOIN"
                                       " (Students NATURAL JOIN Attend)"
                                       " WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group': group_num})
