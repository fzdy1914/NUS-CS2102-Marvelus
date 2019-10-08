from luminus import sql_helper


def get_course(code):
    return sql_helper.fetchone_to_dict("SELECT * FROM Courses WHERE code = %(code)s", {'code': code})

