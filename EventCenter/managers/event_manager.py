from EventCenter.models import Event
from . import channel_manager


def is_event_exists(event_id):
    return Event.objects.filter(pk=event_id).exists()


def is_valid_event(data):
    validation = {'state': False}

    if data['title'] == '':
        validation['error'] = 'Empty event title'
    elif data['description'] == '':
        validation['error'] = 'Empty event description'
    elif data['location'] == '':
        validation['error'] = 'Empty event location'
    elif data['image_url'] == '':
        validation['error'] = 'Empty event image url'
    elif not str(data['timestamp']).isdigit():
        validation['error'] = 'Invalid / Empty event timestamp'
    elif not str(data['channel_id']).isdigit():
        validation['error'] = 'Invalid / Empty event channel id'
    elif not channel_manager.is_channel_exists(data['channel_id']):
        validation['error'] = 'No such channel'
    else:
        validation['state'] = True

    return validation


def create_event(data):
    validation = is_valid_event(data)
    if validation['state']:
        channel = channel_manager.get_channel(data['channel_id'])
        event = Event(channel=channel, **data)
        event.save()
        return event
    else:
        return None


def update_event(pk, data):
    validation = is_valid_event(data)
    if validation['state']:
        event = get_event(pk)
        event.__dict__.update(**data)
        channel = channel_manager.get_channel(data['channel_id'])
        event.channel = channel
        event.save()
        return event
    else:
        return None


def all_events():
    return Event.objects.all()


def get_event(pk):
    return Event.objects.get(pk=pk)


def delete_event(pk):
    if is_event_exists(pk):
        get_event(pk).delete()


