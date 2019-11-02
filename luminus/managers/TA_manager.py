from luminus import sql_helper


def get_TA_by_username(username):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN Participators NATURAL JOIN TAs"
                                       " WHERE uname = %(username)s", {'username': username})


def get_TAs_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN Participators NATURAL JOIN (TAs NATURAL JOIN Assist)"
                                       " WHERE code = %(code)s", {'code': code})


def get_TAs_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN Participators NATURAL JOIN (TAs NATURAL JOIN Assist NATURAL JOIN Facilitate)"
                                       "WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group_num': group_num})


def get_TAs_notincurtut_by_code_group_num(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM USERS u NATURAL JOIN Participators NATURAL JOIN (TAs ta NATURAL JOIN assist a) "
                                       "WHERE a.code = %(code)s "
                                       "AND "
                                       "(NOT EXISTS (SELECT 1 FROM Facilitate f WHERE f.uname = ta.uname AND f.code = f.code AND f.group_num = %(group_num)s))",
                                       {'code': code, 'group_num': group_num})


def add_TA_to_tut_by_uname_code_group_num(uname, code, group_num):
    sql_helper.exec_sql('insert into Facilitate values (%(uname)s, %(code)s, %(group_num)s)',
                        {'uname': uname,
                         'code': code,
                         'group_num': group_num})

    return sql_helper.fetchall_to_dict("SELECT * FROM Users u NATURAL JOIN Participators NATURAL JOIN (Students stu NATURAL JOIN Facilitate f)" 
                                       "WHERE u.uname = %(uname)s AND f.code = %(code)s AND f.group_num = %(group_num)s",
                                       {'uname': uname, 'code': code, 'group_num': group_num})
