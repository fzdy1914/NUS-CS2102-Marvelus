from EventCenter.models import Event
from . import channel_manager


def is_event_exists(event_id):
    return Event.objects.filter(pk=event_id).exists()


def is_valid_event(data):
    validation = {'state': False}

    if data['title'] == '':
        validation['error'] = 'Empty event title'
    elif data['channel'] == '':
        validation['error'] = 'Empty event channel'
    elif not channel_manager.is_channel_name_exists(data['channel']):
        validation['error'] = 'No such channel'
    elif data['location'] == '':
        validation['error'] = 'Empty event location'
    elif not str(data['timestamp']).isdigit():
        validation['error'] = 'Invalid / Empty event time'
    elif data['description'] == '':
        validation['error'] = 'Empty event description'
    elif data['image_url'] == '':
        validation['error'] = 'Empty event image url'
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
        channel = channel_manager.get_channel_by_name(data['channel'])
        event.channel = channel
        event.save()
        return event
    else:
        return None


def all_events():
    return Event.objects.all()


def get_event(pk):
    return Event.objects.get(pk=pk)


def get_events(offset, limit, channel_id, since, until):
    events = all_events()

    if channel_id:
        events = events.filter(channel_id=int(channel_id))

    if since:
        events = events.filter(timestamp__gte=int(since))

    if until:
        events = events.filter(timestamp__lte=int(until))

    count = events.count()
    events = events.order_by('-id')[offset:offset + limit]
    return {'events': events, 'count': count}


def delete_event(pk):
    if is_event_exists(pk):
        get_event(pk).delete()


