def single(tag):
    name = tag['name']
    other_tag = [
        f'{key}="{value}"'
        for key, value in tag.items()
        if key not in ('name', 'tag_type')
    ]
    return f'<{" ".join([name] + other_tag)}>'


def pair(tag):
    name = tag['name']
    body = tag['body']
    other_tag = [
        f'{key}="{value}"'
        for key, value in tag.items()
        if key not in ('name', 'tag_type', 'body')
    ]
    return f'<{" ".join([name] + other_tag)}>{body}</{name}>'


TAG_TYPE = {'single': single, 'pair': pair}


def stringify(tag):
    tag_type = tag['tag_type']
    return TAG_TYPE[tag_type](tag)


tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': '',
  'id': 'empty',
}
print(pair(tag))
