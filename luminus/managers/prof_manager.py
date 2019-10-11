from luminus import sql_helper


def get_profs_by_username(username):
    return sql_helper.fetchall_to_dict("SELECT name, email, expr FROM Users NATURAL JOIN Profs"
                                       " WHERE uname = %(username)s", {'username': username})

def get_profs_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT name, email, expr FROM Users NATURAL JOIN (Profs NATURAL JOIN Teach)"
                                       " WHERE code = %(code)s", {'code': code})
