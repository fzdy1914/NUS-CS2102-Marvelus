def success_json_response(data):
    content = {'state': True, 'data': data}
    return content


def error_json_response(message):
    content = {'state': False, 'error': message}
    return content
