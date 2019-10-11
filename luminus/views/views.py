from django.http import HttpResponse

from luminus import sql_helper


def template(request):
    list = sql_helper.fetchall_to_dict('select * from Users')
    print(list)
    print(list[0]['uname'])
    return HttpResponse('EXECUTED', status=200)
