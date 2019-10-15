from django.db import connections


def exec_sql(sql, params=None, db='luminus'):
    cursor = connections[db].cursor()
    cursor.execute(sql, params)
    cursor.close()
    return True


def fetchone_sql(sql, params=None, db='luminus', flat=False):
    cursor = connections[db].cursor()
    cursor.execute(sql, params)
    fetchone = cursor.fetchone()
    cursor.close()
    if fetchone:
        fetchone = fetchone[0] if flat else fetchone
    return fetchone


def fetchone_to_dict(sql, params=None, db='luminus'):
    cursor = connections[db].cursor()
    cursor.execute(sql, params)
    desc = cursor.description
    try:
        row = dict(zip([col[0] for col in desc], cursor.fetchone()))
    except TypeError:
        return None
    finally:
        cursor.close()
    return row


def fetchall_sql(sql, params=None, db='luminus', flat=False):
    cursor = connections[db].cursor()
    cursor.execute(sql, params)
    fetchall = cursor.fetchall()
    cursor.close()
    if fetchall:
        fetchall = tuple([o[0] for o in fetchall]) if flat else fetchall
    return fetchall


def fetchall_to_dict(sql, params=None, db='luminus'):
    cursor = connections[db].cursor()
    cursor.execute(sql, params)
    desc = cursor.description
    try:
        object_list = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
    except TypeError:
        return None
    finally:
        cursor.close()
    return object_list
