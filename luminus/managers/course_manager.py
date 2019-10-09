from luminus import sql_helper


def get_course(code):
    return sql_helper.fetchone_to_dict("SELECT * FROM Courses WHERE code = %(code)s", {'code': code})


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
                                       "WHERE e.uname = %(suname)s AND c.code = e.code",
                                       {'suname': suname})