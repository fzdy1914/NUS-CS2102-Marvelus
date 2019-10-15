import random

from django.contrib import auth
from django.http import HttpResponse

from . import sql_helper


def test(request):
    auth.logout(request)
    user = auth.authenticate(username="root", password="root")
    if user is not None:
        auth.login(request, user)

    return HttpResponse('EXECUTED', status=200)


def add_user(request):
    sql = 'insert into Users values (%(username)s, %(password)s, %(name)s, %(email)s)'
    for i in range(20):
        data={}
        data['username'] = 'A' + str(i)
        data['name'] = 'A' + str(i)
        data['email'] = 'A' + str(i) + '@test.com'
        data['password'] = 'root'
        sql_helper.exec_sql(sql, data)

    return HttpResponse('Users added', status=200)


def add_participator(request):
    sql = 'insert into Students values (%(username)s, %(major)s)'
    for i in random.sample(range(20), 5):
        data={}
        data['username'] = 'A' + str(i)
        data['major'] = 'A' + str(i)
        sql_helper.exec_sql(sql, data)

    return HttpResponse('Participators added', status=200)
