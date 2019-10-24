from luminus import sql_helper


def get_students_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE status = 'enrolled' AND code = %(code)s ",
                                       {'code': code})


def get_students_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Attend)"
                                       " WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group': group_num})


def get_requests_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE status = 'requesting' AND code = %(code)s ",
                                       {'code': code})


def approve_requests(uname, code):
    return sql_helper.fetchall_to_dict("UPDATE Enroll SET status = 'enrolled'"
                                       "WHERE uname = %(uname)s AND code = %(code)s AND status='requesting'",
                                       {'uname': uname, 'code': code})


def reject_requests(uname, code):
    return sql_helper.fetchall_to_dict("UPDATE Enroll SET status = 'rejected'"
                                       "WHERE uname = %(uname)s AND code = %(code)s AND status='requesting'",
                                       {'uname': uname, 'code': code})


def get_ta_candidates_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users u NATURAL JOIN participators NATURAL JOIN (Students s NATURAL JOIN Enroll e) "
                                       "WHERE status = 'completed' AND code = %(code)s AND "
                                       "(NOT EXISTS(SELECT 1 FROM Assist a WHERE a.uname=s.uname AND a.code = e.code))",
                                       {'code': code})


def add_TA_by_uname_coursecode_group(uname,code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users u NATURAL JOIN participators NATURAL JOIN (Students s NATURAL JOIN Enroll e) "
                                       "WHERE status = 'completed' AND code = %(code)s AND "
                                       "(NOT EXISTS(SELECT 1 FROM Assist a WHERE a.uname=s.uname AND a.code = e.code))",
                                       {'code': code})
