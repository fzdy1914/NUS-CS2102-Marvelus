from luminus.managers import TA_manager
from luminus.responses import success_json_response


def get_TAs_by_coursecode(request, code):
    TAs = TA_manager.get_TAs_by_coursecode(code)
    return success_json_response({'TAs': TAs})


def get_TAs_by_coursecode_and_groupnum(request, code, group_num):
    TAs = TA_manager.get_TAs_by_coursecode_and_groupnum(code, group_num)
    return success_json_response({'TAs': TAs})
