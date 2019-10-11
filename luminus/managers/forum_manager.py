from luminus import sql_helper


def get_forum_by_code(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Forums WHERE code = %(code)s", {'code': code})


def get_forum_by_code_and_group_num(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT F.code, F.fid "
                                       "FROM Forums F JOIN Tutorials T "
                                       "ON F.code = T.code AND T.group_num = %(group_num)s AND F.code = %(code)s"
                                       "WHERE EXISTS("
                                       "    SELECT 1 FROM View V "
                                       "    WHERE V.f_code = F.code AND V.t_code = T.code "
                                       "    AND V.fid = F.fid AND V.group_num = T.group_num"
                                       ")", {'code': code, 'group_num': group_num})
