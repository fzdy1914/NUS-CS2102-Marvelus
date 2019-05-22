def success_json_response(model, data):
    content = {'state': True, model: data}
    return content


def error_json_response(message):
    content = {'state': False, 'error': message}
    return content
