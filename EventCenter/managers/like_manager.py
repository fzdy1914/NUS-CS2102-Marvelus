from EventCenter.models import Like
from EventCenter.managers import event_manager, user_manager


def is_valid_like(data):
    validation = {'state': False}

    if not event_manager.is_event_exists(data['event_id']):
        validation['error'] = 'No such event'
    elif not user_manager.is_user_exists(data['user_id']):
        validation['error'] = 'No such user'
    else:
        validation['state'] = True

    return validation


def is_like_exists(data):
    if is_valid_like(data):
        return Like.objects.filter(event_id=data['event_id'], user_id=data['user_id']).exists()
    return False


def get_like(data):
    if is_valid_like(data) and is_like_exists(data):
        return Like.objects.get(event_id=data['event_id'], user_id=data['user_id'])


def add_like(data):
    if is_valid_like(data):
        if not is_like_exists(data):
            event = event_manager.get_event(data['event_id'])
            user = user_manager.get_user(pk=data['user_id'])
            like = Like(event=event, user=user)
            like.save()
            return like
        return get_like(data)
    return None


def delete_like(data):
    if is_valid_like(data):
        if is_like_exists(data):
            like = get_like(data)
            like.delete()


def all_likes(event_id):
    return Like.objects.filter(event_id=event_id)


def count(event_id):
    return all_likes(event_id).count()
