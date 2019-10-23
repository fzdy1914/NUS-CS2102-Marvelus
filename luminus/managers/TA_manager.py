from luminus import sql_helper


def get_TA_by_username(username):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN TAs"
                                       " WHERE uname = %(username)s", {'username': username})


def get_TAs_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN (TAs NATURAL JOIN Assist)"
                                       " WHERE code = %(code)s", {'code': code})


def get_TAs_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN (TAs NATURAL JOIN Facilitate)"
                                       " WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group_num': group_num})
