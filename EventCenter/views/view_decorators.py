from EventCenter.responses import error_json_response


def admin_required(func):
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            return error_json_response('Authority required')
        return func(request, *args, **kwargs)
    return wrapper
