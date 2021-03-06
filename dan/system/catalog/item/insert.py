import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Item import Item
from system.catalog.classes.Char import Char


def insert(SITE):
    print('FUNCTION -> system-> calalog -> item -> insert')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/section/' + SITE.post['section_id']}

    ITEM = Item(SITE)
    CHAR = Char(SITE)
    ITEM.insert({
        'section_id': SITE.post['section_id'],
        'name': SITE.post['name'],
        'text': SITE.post['text'],
        'data': SITE.post['data'],
        'status': SITE.post['status'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/section/' + SITE.post['section_id']}
