from classes.Catalog import Catalog
from classes.Section import Section
from classes.Item import Item
import sys
sys.path.append('system/catalog/classes')


def item_edit(SITE):
    print('PATH -> system/catalog/item/edit')
    SITE.addHeadFile('/plugins/ckeditor/ckeditor.js')

    CATALOG = Catalog(SITE)
    SECTION = Section(SITE)
    ITEM = Item(SITE)

    if SITE.p[2] == 'edit':
        item_id = SITE.p[3]
        item = ITEM.getItem(item_id)
        section_id = item['section_id']
        title = 'Редактировать элемент'
        action = 'update/' + item_id
    else:
        section_id = SITE.p[3]
        title = 'Добавить  элемент'
        action = 'insert'
        ordering = ITEM.getMaxOrdering(section_id) + 1
        item = {'id': 0, 'name': '', 'text': '', 'data': '', 'status': 1, 'ordering': ordering}

    section = SECTION.getSection(section_id)
    catalog = CATALOG.getItem(section['catalog_id'])

    data = {}
    data['catalog_id'] = catalog['id']
    data['parent_id'] = section['parent_id']
    breadcrubmps_list = SECTION.breadcrumbsPath(data)[::-1]

    breadcrumbs = ''

    if (len(breadcrubmps_list) > 0):
        for i in breadcrubmps_list:
            breadcrumbs += '<svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>'
            breadcrumbs += '<a href="/system/catalog/section/' + \
                str(i['id']) + '">' + i['name'] + '</a>'

    rows = SECTION.tree(catalog['id'])
    sec_options = ''
    # Уровень, ниже которого опускаться нельзя для дочерних пунктов нашего раздела
    tabu_level = 1000
    if (rows):
        for row in rows:

            if row['id'] == section['id']:
                # Если это текущий раздел, не отображать его и дочерние разделы
                tabu_level = row['level']
                continue

            if row['level'] <= tabu_level:
                # Вышли из дочерних разделов текущего раздела - всё сбрасываем
                tabu_level = 1000
                level = '&nbsp;-&nbsp;' * row['level']
                selected = 'selected' if row['id'] == section['parent_id'] else ''
                sec_options += f'''<option { selected } value="{ row['id'] }">{ level }{ row['name'] }</option>'''

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
			<a href="/system/catalog/cat/''' + str(catalog['id']) + '''">''' + catalog['name'] + '''</a>
            ''' + breadcrumbs + '''
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/section/''' + str(section['id']) + '''">''' + section['name'] + '''</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
        <form method="post" action="/system/catalog/item/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="name" placeholder="Элемент" required value="''' + item['name'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Раздел</div>
					<div class="tc_item_r flex_grow">
						<select class="input" name="parent_id">
                            <option value="0">Нет</option>
                            ''' + sec_options + '''
                        </select>
					</div>
				</div>
				<div class="flex_row p_5_20">
                    <div class="tc_item_l">Текст</div>
                    <div class="tc_item_r flex_grow"> 
					    <textarea id="editor1" name="text">''' + item['text'] + '''</textarea>
                    </div>
				</div>
                <div class="flex_row p_5_20">
      				<div class="tc_item_l">Данные</div>
					<div class="tc_item_r flex_grow">          
					    <textarea class="input" name="data" style="width:100%;height:100px;">''' + item['data'] + '''</textarea>
                    </div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Статус</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="status" type="number" value="''' + str(item['status']) + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Порядок следования</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="ordering" type="number" value="''' + str(item['ordering']) + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
            <input class="input" name="section_id" type="hidden" value="''' + str(section_id) + '''">
            <script type="text/javascript">
                CKEDITOR.replace( 'editor1', {
                    height: '400px',
                    filebrowserBrowseUrl : '/system/plugins/filemanager'
                });
            </script>
		</form>
    </div>
    '''
