from EventCenter.models import Channel


def is_channel_exists(pk):
    return Channel.objects.filter(pk=pk).exists()


def is_channel_name_exists(channel_name):
    return Channel.objects.filter(name=channel_name).exists()


def get_channel(pk):
    return Channel.objects.get(pk=pk)


def get_channel_by_name(name):
    return Channel.objects.get(name=name)


def get_channels(offset, limit):
    return all_channels().order_by('-id')[offset:offset + limit]


def is_valid_channel(data):
    validation = {'state': False}
    name = data['name']

    if name == '':
        validation['error'] = 'Empty channel name'
    elif is_channel_name_exists(name):
        validation['error'] = 'Duplicated channel name'
    else:
        validation['state'] = True

    return validation


def create_channel(data):
    validation = is_valid_channel(data)
    if validation['state']:
        channel = Channel(**data)
        channel.save()
        return channel
    return None


def update_channel(pk, data):
    validation = is_valid_channel(data)
    if validation['state'] and is_channel_exists(data['id']):
        channel = get_channel(pk)
        channel.name = data['name']
        channel.save()
        return channel
    return None


def delete_channel(pk):
    if is_channel_exists(pk):
        get_channel(pk).delete()


def all_channels():
    return Channel.objects.all()


def count():
    return all_channels().count()


