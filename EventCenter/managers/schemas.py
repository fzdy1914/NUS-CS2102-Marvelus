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
