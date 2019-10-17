from django.http import JsonResponse


def json_wrapper(func):
    def wrapper(*args, **kwargs):
        return JsonResponse(func(*args, **kwargs))
    return wrapper


@json_wrapper
def success_json_response(data):
    content = {'state': True, 'data': data}
    return content


@json_wrapper
def error_json_response(message):
    content = {'state': False, 'error': message}
    return content
