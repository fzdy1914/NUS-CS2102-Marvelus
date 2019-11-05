from luminus import sql_helper


def search_courses(keyword, uname):
    return sql_helper.fetchall_to_dict("SELECT DISTINCT c.code, c.title, c.info, c.lec_day, c.start_time, c.end_time, e.status, e.enroll_year"
                                       " FROM Courses c LEFT JOIN (SELECT * FROM Enroll WHERE uname = %(uname)s) e"
                                       " on c.code = e.code WHERE c.code LIKE %(keyword)s ORDER BY enroll_year DESC",
                                       {'keyword': '%' + keyword + '%', 'uname': uname})


def get_course_by_code(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Courses WHERE code = %(code)s", {'code': code})


def get_course_by_puname(puname):
    return sql_helper.fetchall_to_dict("SELECT * FROM Courses c, Teach t "
                                       "WHERE t.uname = %(puname)s AND c.code = t.code",
                                       {'puname': puname})


def get_course_by_tuname(tuname):
    return sql_helper.fetchall_to_dict("SELECT * FROM Courses c, Assist a "
                                       "WHERE a.uname = %(tuname)s AND c.code = a.code",
                                       {'tuname': tuname})


def get_course_by_suname(suname):
    return sql_helper.fetchall_to_dict("SELECT * FROM Courses c, Enroll e "
                                       "WHERE e.uname = %(suname)s AND c.code = e.code AND e.status='enrolled'",
                                       {'suname': suname})
