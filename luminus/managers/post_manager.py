from luminus import sql_helper


def get_posts_by_code_and_fid(code, fid):
    return sql_helper.fetchall_to_dict("SELECT * FROM Posts NATURAL JOIN Users "
                                       "WHERE code = %(code)s AND fid = %(fid)s "
                                       "AND t_code IS NULL AND t_fid IS NULL AND t_pid IS NULL",
                                       {'code': code, 'fid': fid})


def get_post_by_code_and_fid_and_pid(code, fid, pid):
    return sql_helper.fetchone_to_dict("SELECT * FROM Posts NATURAL JOIN Users "
                                       "WHERE code = %(code)s AND fid = %(fid)s AND pid = %(pid)s",
                                       {'code': code, 'fid': fid, 'pid': pid})


def get_replies_by_code_and_fid_and_pid(code, fid, pid):
    return sql_helper.fetchall_to_dict("SELECT * FROM Posts NATURAL JOIN Users "
                                       "WHERE t_code = %(code)s AND t_fid = %(fid)s AND t_pid = %(pid)s"
                                       "ORDER BY pid",
                                       {'code': code, 'fid': fid, 'pid': pid})


def add_post(code, fid, title, content, uname):
    max_pid = sql_helper.fetchone_to_dict("SELECT max(pid) as max FROM Posts "
                                          "WHERE code = %(code)s AND fid = %(fid)s",
                                          {'code': code, 'fid': fid})['max']

    if not max_pid:
        max_pid = 0

    sql_helper.exec_sql('INSERT IGNORE INTO Posts values (%(code)s, %(fid)s, %(pid)s, null, null, null, '
                        '%(uname)s, %(title)s, %(content)s)',
                        {'code': code, 'fid': fid, 'pid': max_pid + 1, 'title': title, 'content': content, 'uname': uname})

    return get_post_by_code_and_fid_and_pid(code, fid, max_pid + 1)


def add_reply(code, fid, pid, title, content, uname):
    max_pid = sql_helper.fetchone_to_dict("SELECT max(pid) as max FROM Posts "
                                          "WHERE code = %(code)s AND fid = %(fid)s",
                                          {'code': code, 'fid': fid})['max']

    if not max_pid:
        max_pid = 0

    sql_helper.exec_sql('INSERT IGNORE INTO Posts values (%(code)s, %(fid)s, %(pid)s, %(code)s, %(fid)s, %(t_pid)s, '
                        '%(uname)s, %(title)s, %(content)s)',
                        {'code': code, 'fid': fid, 'pid': max_pid + 1, 't_pid': pid, 'title': title, 'content': content, 'uname': uname})

    return get_post_by_code_and_fid_and_pid(code, fid, max_pid + 1)
