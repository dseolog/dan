from classes.Item import Item
import sys
sys.path.append('system/catalog/classes')


def item_pub(SITE):
    print('FUNCTION -> system-> calalog -> item -> pub/unpub')
    type = SITE.p[2]
    id = SITE.p[3]

    ITEM = Item(SITE)
    section_id = ITEM.pub(type, id)

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/section/' + str(section_id)}
    return {'redirect': '/system/catalog/section/' + str(section_id)}