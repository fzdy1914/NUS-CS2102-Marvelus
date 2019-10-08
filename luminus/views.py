from django.http import HttpResponse
from django.db import transaction
from django.db import connections


def template(request):
    # cursor = connections['default'].cursor()
    # cursor.execute('select * from channel_tab')
    # row = cursor.fetchone()  # 只读取一行

    # cursor.execute('select * from channel_tab WHERE name=%s', [row[1]])
    # rows = cursor.fetchall()  # 读取所有行
    #

    cursor = connections['luminus'].cursor()
    cursor.execute('select count(*) from Users')
    print(cursor.fetchone())
    transaction.commit()
    return HttpResponse('EXECUTED', status=200)
