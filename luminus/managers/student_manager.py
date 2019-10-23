from luminus import sql_helper
from datetime import datetime

def get_students_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE code = %(code)s", {'code': code})


def get_students_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN"
                                       " (Students NATURAL JOIN Attend)"
                                       " WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group_num': group_num})

def get_students_for_TAs_by_coursecode(code):
    return  sql_helper.fetchall_to_dict("SELECT * FROM (Enrolls NATURAL JOIN Students) AS es WHERE es.code = %(code)s AND es.status ='COMPLETED' "
                                        "AND NOT EXISTS (SELECT 1 FROM Facilitate f WHERE f.code = %(code)s AND f.uname=es.uname)",
                                        {'code':code})


def add_student_for_TA_by_uname_coursecode_groupnum(uname,code,group_num):
    return sql_helper.fetchall_to_dict("INSERT INTO Facilitate VALUES (uname,coursecode,groupnum;"
                                       "INSERT INTO TAs VALUES (uname)"
                                       "WHERE NOT EXISTS (SELECT 1 FROM TAs t WHERE t.uname=uname);"
                                       "SELECT * FROM Facilitate f "
                                       "WHERE f.uname=%(uname)s and f.code=%(code)s and f.group_num=%(group_num)s)",
                                       {'code':code,'uname':uname,'group_num':group_num})


def add_student_to_tut_by_uname_coursecode_groupnum(uname, code, group_num):
    print(uname)
    print(code)
    print(group_num)
    sql = 'insert into Attend values (%(uname)s, %(code)s, %(group_num)s, %(date)s )'
    data = {}
    data['uname'] = uname
    data['code'] = code
    data['group_num'] = group_num
    data['date'] = datetime.now()
    sql_helper.exec_sql(sql, data)

    sql1 = 'SELECT * FROM Users NATURAL JOIN (Students NATURAL JOIN Attend) WHERE code = %(code)s AND group_num = %(group_num)s'
    return sql_helper.fetchall_to_dict(sql1, {'code': code, 'group_num': group_num})


    # return sql_helper.fetchall_to_dict("INSERT INTO Attend VALUES (uname,code,group_num)"
    #                                    "WHERE NOT EXISTS"
    #                                    "(SELECT 1 FROM Attend a WHERE a.uname=uname);"
    #                                    , {'code': code, 'uname': uname, 'group_num': group_num})

def get_student_enrolledbutnotattend_by_coursecode(code):
    # return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN"
    #                                    " (Students NATURAL JOIN Enroll) WHERE code = %(code)s", {'code': code})
    return sql_helper.fetchall_to_dict("SELECT * FROM USERS NATURAL JOIN Students NATURAL JOIN Enroll "
                                       "WHERE code = %(code)s ",{'code': code})
                                       # "AND "
                                       # "NOT EXISTS "
                                       # "(SELECT 1 FROM Attend a WHERE a.uname=use.uname AND a.code=%(code)s ) "
                                       # ,{'code': code})