import json

import pkg_resources


def get_messages():
    file_addr = pkg_resources.resource_filename('mypackage', 'data/messages.json')
    with open(file_addr, 'r') as fp:
        return json.load(fp)['messages']
