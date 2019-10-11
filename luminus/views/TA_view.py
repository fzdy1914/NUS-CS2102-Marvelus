from django.http import HttpResponse

from luminus.managers import TA_manager


def get_TAs_by_coursecode(code):
    TAs = TA_manager.get_TAs_by_coursecode(code)
    return HttpResponse(TAs, status=200)


def get_TAs_by_coursecode_and_groupnum(code, group_num):
    TAs = TA_manager.get_TAs_by_coursecode_and_groupnum(code, group_num)
    return HttpResponse(TAs, status=200)
