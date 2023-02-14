def detect_handles(text: str) -> str:
    if text.startswith('@'):
        return 'User handle'
    elif text.startswith('#'):
        return 'Hashtag handle'
    elif text.startswith('www.') or text.startswith('http://'):
        if '.com' in text:
            return 'Web handler'
    else:
        return 'Not a handle'


print(detect_handles(input('Insert a text: ')))
