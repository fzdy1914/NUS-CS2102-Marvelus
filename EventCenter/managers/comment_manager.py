from EventCenter.models import Comment
from EventCenter.managers import event_manager, user_manager


def is_valid_comment(data):
    validation = {'state': False}

    if data['title'] == '':
        validation['error'] = 'Empty comment title'
    elif data['content'] == '':
        validation['error'] = 'Empty comment content'
    elif not event_manager.is_event_exists(data['event_id']):
        validation['error'] = 'No such event'
    elif not user_manager.is_user_exists(data['user_id']):
        validation['error'] = 'No such user'
    else:
        validation['state'] = True

    return validation


def add_comments(data):
    if is_valid_comment(data):
        event = event_manager.get_event(data['event_id'])
        user = user_manager.get_user(pk=data['user_id'])
        comment = Comment(event=event, user=user, **data)
        comment.save()
        return comment
    return None


def all_comments(event_id):
    return Comment.objects.filter(event_id=event_id)


def count(event_id):
    return all_comments(event_id).count()
