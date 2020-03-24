import pymongo
import json
from decimal import Decimal
from datetime import date, datetime
from bson.objectid import ObjectId
# import bson
# import bson.json_util
# from bson.json_util import dumps


def default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return str(obj)
    elif isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" %
                    type(obj).__name__)


try:
    client = pymongo.MongoClient('mongodb://47.111.3.150:27000/')
    db = client.lightmes_db_oez
    collection = db.tm_item
    strjson = ''
    for data in collection.find():
        strjson = strjson + ',' + \
            json.dumps(data, ensure_ascii=False, default=default)

    with open('tm_item.json', 'w+', encoding='utf-8') as f:
        f.write('[')
        f.write(strjson)
        f.write(']')
    f.close()
except SystemError as err:
    print(err)
