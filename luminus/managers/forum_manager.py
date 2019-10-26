from luminus import sql_helper


def get_forum_by_code(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Forums WHERE code = %(code)s", {'code': code})


def get_forum_by_code_and_group_num(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * "
                                       "FROM Forums F JOIN Tutorials T "
                                       "ON F.code = T.code AND T.group_num = %(group_num)s AND F.code = %(code)s"
                                       "WHERE EXISTS("
                                       "    SELECT 1 FROM View V "
                                       "    WHERE V.f_code = F.code AND V.t_code = T.code "
                                       "    AND V.fid = F.fid AND V.group_num = T.group_num"
                                       ")", {'code': code, 'group_num': group_num})


def get_forum_notintut_by_code_and_group_num(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Forums f "
                                       "WHERE f.code = %(code)s AND"
                                       " (NOT EXISTS ( "
                                       "    SELECT 1 FROM View v "
                                       "    WHERE v.f_code=%(code)s AND v.group_num=%(group_num)s AND v.fid = f.fid "
                                       "))", {'code': code, 'group_num': group_num})


def add_forum_to_tut_by_code_group_num_fid(code, group_num, fid):
    sql_helper.exec_sql('insert into View values (%(f_code)s, %(fid)s,%(t_code)s ,%(group_num)s)',
                        {'f_code': code, 'fid': fid, 't_code': code, 'group_num': group_num})

    return sql_helper.fetchall_to_dict("SELECT * FROM Forums f "
                                       "WHERE f.code = %(code)s AND f.fid = %(fid)s",
                                       {'code': code, 'fid': fid})
