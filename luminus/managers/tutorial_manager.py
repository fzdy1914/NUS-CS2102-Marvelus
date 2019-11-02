from luminus import sql_helper


def get_tutorials_by_coursecode(code):
    return sql_helper.fetchall_to_dict("select * from"
                                       "(select code, group_num,sum(amount) as stuAmount from"
                                       "(select code, group_num, case when uname is not null then 1 else 0 end as amount from tutorials natural left join attend where code=%(code)s) as t1 "
                                       "group by code, group_num) as s1 "
                                       "natural join"
                                       "(select code, group_num,sum(amount) as TAAmount from"
                                       "(select code, group_num, case when uname is not null then 1 else 0 end as amount from tutorials natural left join facilitate where code=%(code)s) as t2 "
                                       "group by code, group_num) as s2", {'code': code})


def get_tutorials_by_student(username):
    return sql_helper.fetchall_to_dict("SELECT * FROM Attend NATURAL JOIN tutorials WHERE uname = %(username)s", {'username': username})


def get_tutorials_by_tA_and_course(username, code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Facilitate WHERE uname=%(username)s AND code=%(code)s ", {'code': code, 'username': username})


def get_tutorials_by_course_and_group(code, num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Tutorials WHERE code=%(code)s AND group_num=%(num)s", {'code': code, 'num': num})


def add_stu_to_attendance_by_uname_code_group_num(uname, code, group_num, attend_week):
    sql_helper.exec_sql('insert into Attendance values (%(uname)s, %(code)s, %(group_num)s,%(attend_week)s)',
                        {'uname': uname,
                         'code': code,
                         'group_num': group_num,
                         'attend_week': attend_week})

    return sql_helper.fetchall_to_dict("SELECT * FROM Users u "
                                       # "NATURAL JOIN Participators p"
                                       " NATURAL JOIN (Students stu NATURAL JOIN Attendance a)"
                                       "WHERE u.uname = %(uname)s AND"
                                       " a.code = %(code)s AND a.group_num = %(group_num)s "
                                       "AND a.attend_week=%(attend_week)s",
                                       {'uname': uname, 'code': code, 'group_num': group_num, 'attend_week': attend_week})


def retrieve_attendance_by_uname_code_group_num(uname, code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Attendance a "
                                       "WHERE a.uname=%(uname)s AND a.code=%(code)s AND a.group_num=%(group_num)s" , {'uname': uname, 'code': code, 'group_num': group_num })
