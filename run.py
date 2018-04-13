#!.env/bin/python
import os
import json
import urllib.parse 
# folder = './files/'
# file_list = os.listdir(folder)
# for file_name in file_list:
#     print(file_list.index(file_name), file_name)

# index = input('Type file number of the file:')
# file_path = folder + file_list[int(index)]
file = open('/Users/Max/GitHub/learning/python/markdown-to-things/md.txt')

data = []

content = file.readlines()

for title in content:
    print(content.index(title))
    if title[:2] == '# ':
        project = {
            'type': 'project',
            'attributes': {
                'title': title[2:].rstrip(),
                'notes': ' ',
                'items': []
            }
        }
        data.append(project)
    elif title[:2] == '##':
        header = {
            'type': 'heading',
            'attributes': {
                'title': title[2:].rstrip()
            }
        }
        data[-1]['attributes']['items'].append(header)
    elif title[:2] == '> ':
        if not data[-1]['attributes']['items']:
            data[-1]['attributes']['notes'] = title[2:].rstrip()
        else:
            data[-1]['attributes']['items'][-1]['attributes']['notes'] = title[2:].rstrip()
    elif title[:2] == '- ':
        checklist = {
            'type': 'checklist-item',
            'attributes': {
                'title': title[2:].rstrip(),
                'notes': '',
                'checklist-items': []
            }
        }
        if 'checklist-items' not in data[-1]['attributes']['items'][-1]['attributes']:
            data[-1]['attributes']['items'][-1]['attributes']['checklist-items'] = []
        data[-1]['attributes']['items'][-1]['attributes']['checklist-items'].append(checklist)
    else:
        if title[:2] == '* ':
            todo = {
                'type': 'to-do',
                'attributes': {
                    'title': title[2:].rstrip()
                }}
        else:
            todo = {
                'type': 'to-do',
                'attributes': {
                    'title': title.rstrip()
                }}
        data[-1]['attributes']['items'].append(todo)

things_url = 'things:///add-json?data=' + urllib.parse.quote(json.dumps(data))
print(things_url)
