from luminus import sql_helper
from datetime import date


def get_students_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN Participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE Enroll.status = 'enrolled' AND Enroll.code = %(code)s ",
                                       {'code': code})


def get_students_for_TAs_by_coursecode(code):
    return  sql_helper.fetchall_to_dict("SELECT * FROM (Enrolls NATURAL JOIN Students) AS es WHERE es.code = %(code)s AND es.status ='COMPLETED' "
                                        "AND NOT EXISTS (SELECT 1 FROM Facilitate f WHERE f.code = %(code)s AND f.uname=es.uname)",
                                        {'code': code})


def add_student_for_TA_by_uname_coursecode_groupnum(uname,code,group_num):
    return sql_helper.fetchall_to_dict("INSERT INTO Facilitate VALUES (uname,coursecode,groupnum);"
                                       "INSERT INTO TAs VALUES (uname)"
                                       "WHERE NOT EXISTS (SELECT 1 FROM TAs t WHERE t.uname=uname);"
                                       "SELECT * FROM Facilitate f "
                                       "WHERE f.uname=%(uname)s and f.code=%(code)s and f.group_num=%(group_num)s)",
                                       {'code':code,'uname':uname,'group_num':group_num})


def add_student_to_tut_by_uname_coursecode_groupnum(uname, code, group_num):
    sql_helper.exec_sql('insert into Attend values (%(uname)s, %(code)s, %(group_num)s )',
                        {'uname': uname, 'code': code, 'group_num': group_num})

    return sql_helper.fetchall_to_dict('SELECT * FROM Users NATURAL JOIN (Students NATURAL JOIN Attend) WHERE code = %(code)s AND group_num = %(group_num)s',
                                       {'code': code, 'group_num': group_num})


def get_student_enrolledbutnotattend_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM USERS u NATURAL JOIN Participators NATURAL JOIN (Students stu NATURAL JOIN Enroll e) "
                                       "WHERE e.code = %(code)s AND e.status ='enrolled' "
                                       "AND "
                                       "(NOT EXISTS (SELECT 1 FROM Attend a WHERE a.uname = stu.uname AND a.code = e.code ) )"
                                       ,{'code': code})


def get_students_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Attend)"
                                       " WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group_num': group_num})


def get_requests_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE status = 'requesting' AND code = %(code)s ",
                                       {'code': code})


def approve_requests(uname, code):
    today = date.today()
    year = today.strftime("%Y")
    return sql_helper.fetchall_to_dict("UPDATE Enroll SET status = 'enrolled', enroll_year = %(year)s"
                                       "WHERE uname = %(uname)s AND code = %(code)s AND status='requesting'",
                                       {'uname': uname, 'code': code, 'year': year})


def reject_requests(uname, code):
    return sql_helper.fetchall_to_dict("UPDATE Enroll SET status = 'rejected'"
                                       "WHERE uname = %(uname)s AND code = %(code)s AND status='requesting'",
                                       {'uname': uname, 'code': code})


def get_ta_candidates_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users u NATURAL JOIN Participators p NATURAL JOIN (Students s NATURAL JOIN Enroll e) "
                                       "WHERE status = 'completed' AND code = %(code)s AND (e.final_grade = 'A' OR e.final_grade = 'B') AND"
                                       "(NOT EXISTS(SELECT 1 FROM Assist a WHERE a.uname=s.uname AND a.code = e.code))"
                                       "ORDER BY e.final_grade ASC,"
                                       "          p.year DESC",
                                       {'code': code})


def add_ta_by_uname_coursecode_group(uname, code):
    # for students that are yet not tutoring any course
    sql_helper.exec_sql('INSERT IGNORE INTO TAs VALUES(%(uname)s)', {'uname': uname})

    return sql_helper.exec_sql('INSERT IGNORE INTO Assist values(%(uname)s,  %(code)s)',
                               {'uname': uname,  'code': code})


def get_students_by_student_uname_and_coursecode(uname, code):
    return  sql_helper.fetchall_to_dict("SELECT * FROM (SELECT group_num FROM Attend NATURAL JOIN tutorials WHERE uname = %(uname)s and code = %(code)s) AS grp"
                                        " ,Attend AS atd, Users AS usr, Participators AS ptp WHERE grp.group_num = atd.group_num"
                                        " AND atd.code = %(code)s AND usr.uname=atd.uname AND ptp.uname=atd.uname",
                                        {'uname': uname, 'code': code})


def get_students_by_coursecode_and_status(code, status):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE status = %(status)s AND code = %(code)s"
                                       " ORDER BY enroll_year DESC",
                                       {'code': code, 'status': status})


def update_testgrade_by_uname_and_code(uname, code, grade):
    return sql_helper.fetchall_to_dict("UPDATE Students NATURAL JOIN Enroll SET test_grade = %(grade)s"
                                       " WHERE uname = %(uname)s AND code = %(code)s",
                                       {'uname': uname, 'code': code, 'grade': grade})


def add_enroll_request_by_uname_and_code(uname, code):
    year = str(date.today().year)
    return sql_helper.exec_sql("INSERT IGNORE INTO Enroll (uname, code, status, enroll_year) VALUES (%(uname)s,  %(code)s, 'requesting', %(year)s)",
                               {'uname': uname, 'code': code, 'year': year})


def retrieve_complete_amount(code):
    today = date.today()
    year = today.strftime("%Y")
    return sql_helper.fetchall_to_dict("select count(*) from enroll e "
                                       "where e.code=%(code)s and e.status='completed' and e.enroll_year=%(year)s "
                                       , {'code': code, 'year': year})


def calculate_final_grade(code, a, b, c, d, e, f):
    today = date.today()
    year = today.strftime("%Y")

    return sql_helper.fetchall_to_dict(
                                    "select r.* ,"
                                    "case when iterator<=%(a)s then 'A' "
                                    "when iterator>%(a)s AND iterator<=%(b)s then 'B' "
                                    "when iterator>%(b)s AND iterator<=%(c)s then 'C' "
                                    "when iterator>%(c)s AND iterator<=%(d)s then 'D'"
                                    "when iterator>%(d)s AND iterator<=%(e)s then 'E' "
                                    "else 'F' end as final_result "
                                    "from "
                                    "("
                                    " select @i:=@i+1 as iterator, e.*,(e.attendance_grade + e.test_grade) as grade "
                                    "from enroll e,(select @i:=0) foo "
                                    "where e.code=%(code)s and e.status='completed' and e.enroll_year=%(year)s order by grade DESC "
                                    ") r"
                                    , {'code': code, 'year': year, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f})


def update_final_grade(uname, code, final_grade):
    return sql_helper.fetchall_to_dict("update enroll set final_grade=%(final_grade)s "
                                       "where uname = %(uname)s AND code = %(code)s AND status='completed'"
                                       , {'uname': uname, 'code': code, 'final_grade': final_grade})


# def retrieve_after_grading(code):
#     today = date.today()
#     year = today.strftime("%Y")
#     return sql_helper.fetchall_to_dict("select @i:=@i+1 as iterator, e.*,(e.attendance_grade + e.test_grade) as grade "
#                                        "from enroll e,(select @i:=0) foo "
#                                        "where e.code=%(code)s and e.status='completed' and e.enroll_year=%(year)s order by grade DESC "
#                                        , {'code': code, 'year': year})
