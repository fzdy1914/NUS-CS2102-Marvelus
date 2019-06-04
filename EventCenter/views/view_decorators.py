from EventCenter.responses import error_json_response


def admin_required(func):
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return error_json_response('Authority required')
        return func(request, *args, **kwargs)
    return wrapper


def json_request(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return error_json_response('Invalid JSON file')
        except (KeyError, TypeError):
            return error_json_response('Missing / Invalid arguments')
    return wrapper


def args_request(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return error_json_response('Missing / Invalid arguments')
    return wrapper
