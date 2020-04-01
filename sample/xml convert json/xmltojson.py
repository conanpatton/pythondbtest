import json
import xmltodict

try:
    inputfile = '111.xml'
    outputfile = '111.json'
    xml_file = open(inputfile, 'r', encoding='utf-8')
    xml_src = xml_file.read()
    json_src = xmltodict.parse(xml_src)

    with open(outputfile, 'w+', encoding='utf-8') as f:
        f.write(json.dumps(json_src, indent=8))
    f.close()
except SystemError as err:
    print(err)
finally:
    f.close()
