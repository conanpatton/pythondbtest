import json
import xmltodict

try:
    xml_file = open('111.xml', 'r', encoding='utf-8')
    xml_src = xml_file.read()
    json_src = xmltodict.parse(xml_src)

    with open('111.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(json_src, indent=8))
    f.close()
except SystemError as err:
    print(err)
