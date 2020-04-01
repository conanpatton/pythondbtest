import pymongo
import json
from decimal import Decimal
from datetime import date, datetime
from bson.objectid import ObjectId


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
    strconn = 'mongodb://47.111.3.150:27000/'
    client = pymongo.MongoClient(strconn)
    db = client.lightmes_db_oez
    collection = db.tm_item
    cursor = collection.find()
    listdata = []
    for data in cursor:
        listdata.append(data)

    outputfile = 'tm_item.json'
    with open(outputfile, 'w+', encoding='utf-8') as f:
        f.write(json.dumps(listdata, ensure_ascii=False, default=default))
    f.close()
except pymongo.errors as err:
    print(err)
finally:
    f.close()
