comment_schema = {
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 128
        },
        'content': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        }
    }
}

event_schema = {
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 128
        },
        'channel_name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 256
        },
        'location': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 256
        },
        'timestamp': {
            'type': 'number',
            "minimum": 1,
        },
        'description': {
            'type': 'string',
            'minLength': 1
        },
        'image_url': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        }
    }
}
