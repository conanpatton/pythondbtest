import mysql.connector
import json
from decimal import Decimal
from datetime import date, datetime

config = {
    'user': 'root',
    'password': 'osksh3008',
    'host': 'localhost',
    'database': 'omzsw',
    'raise_on_warnings': True
}


def default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" %
                    type(obj).__name__)


try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    sqlcmd = ("SELECT * FROM tb_products_list")
    cursor.execute(sqlcmd)
    results = cursor.fetchall()

    with open('result.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(results, default=default))
    f.close()
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    cnx.close()
