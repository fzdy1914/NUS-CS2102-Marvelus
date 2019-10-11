from luminus import sql_helper


def get_post_by_code_and_fid(code, fid):
    return sql_helper.fetchall_to_dict("SELECT code, fid, pid FROM Posts "
                                       "WHERE code = %(code)s AND fid = %(fid)s "
                                       "AND t_code IS NULL AND t_fid IS NULL AND t_pid IS NULL",
                                       {'code': code, 'fid': fid})


def get_post_by_code_and_fid_and_pid(code, fid, pid):
    return sql_helper.fetchall_to_dict("SELECT code, fid, pid FROM Posts "
                                       "WHERE t_code = %(code)s AND t_fid = %(fid)s AND t_pid = %(pid)s"
                                       "ORDER BY pid",
                                       {'code': code, 'fid': fid, 'pid': pid})
