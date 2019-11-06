from luminus import sql_helper


def get_forum_by_code(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Forums WHERE code = %(code)s", {'code': code})


def get_forum_by_code_and_group_num(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT f.fid as fid,f.title as title "
                                       "FROM Forums f JOIN view v  "
                                       "WHERE v.t_code=%(code)s AND v.group_num=%(group_num)s "
                                       "AND v.f_code=f.code AND v.fid=f.fid  "
                                       , {'code': code, 'group_num': group_num})


def get_forum_by_code_and_uname(code, uname):
    return sql_helper.fetchall_to_dict("WITH X AS (SELECT * FROM Attend NATURAL JOIN tutorials "
                                       "    WHERE uname = %(uname)s AND code=%(code)s) "
                                       "SELECT * FROM Forums F JOIN X "
                                       "ON F.code = X.code "
                                       "WHERE EXISTS("
                                       "    SELECT 1 FROM View V "
                                       "    WHERE V.f_code = F.code AND V.t_code = X.code "
                                       "    AND V.fid = F.fid AND V.group_num = X.group_num)",
                                       {'uname': uname, 'code': code})


def get_forum_notintut_by_code_and_group_num(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT  f.title, f.fid, count(*) as stuNum"
                                       " FROM Forums f JOIN (Tutorials T NATURAL JOIN Attend A)"
                                       "WHERE f.code = %(code)s AND"
                                       " (NOT EXISTS ( "
                                       "    SELECT 1 FROM View v "
                                       "    WHERE v.f_code=%(code)s AND v.group_num=%(group_num)s AND v.fid = f.fid "
                                       ")) "
                                       "GROUP BY f.fid", {'code': code, 'group_num': group_num})


def add_forum_to_tut_by_code_group_num_fid(code, group_num, fid):
    sql_helper.exec_sql('insert into View values (%(f_code)s, %(fid)s,%(t_code)s ,%(group_num)s)',
                        {'f_code': code, 'fid': fid, 't_code': code, 'group_num': group_num})

    return sql_helper.fetchall_to_dict("SELECT * FROM Forums f "
                                       "WHERE f.code = %(code)s AND f.fid = %(fid)s",
                                       {'code': code, 'fid': fid})


def delete_forum(code, fid):
    sql_helper.exec_sql('DELETE FROM Forums WHERE code=%(code)s AND fid=%(fid)s',
                        {'code': code, 'fid': fid})


def add_reply(code, title):
    max_fid = sql_helper.fetchone_to_dict("SELECT max(fid) as max FROM Forums "
                                          "WHERE code = %(code)s",
                                          {'code': code})['max']

    if not max_fid:
        max_fid = 0

    sql_helper.exec_sql('INSERT IGNORE INTO Forums values (%(code)s, %(fid)s, %(title)s)',
                        {'code': code, 'fid': max_fid + 1, 'title': title})
