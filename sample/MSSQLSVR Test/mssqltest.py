import pyodbc
import json
from decimal import Decimal
from datetime import date, datetime


def default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" %
                    type(obj).__name__)


try:
    # connstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=QITEC;UID=sa;PWD=pass@2018'
    # cnx = pyodbc.connect(connstr)

    config = {
        'DRIVER': '{ODBC Driver 17 for SQL Server}',
        'SERVER': 'localhost',
        'DATABASE': 'QITEC',
        'UID': 'sa',
        'PWD': 'pass@2018'
    }
    cnx = pyodbc.connect(**config)
    cursor = cnx.cursor()

    sqlcmd = ('SELECT * FROM T_SYOKUZAI_ITEM')
    cursor.execute(sqlcmd)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    listdata = []
    for row in rows:
        listdata.append(dict(zip(columns, row)))

    outputfile = 'qitec_result.json'
    with open(outputfile, 'w+', encoding='utf-8') as f:
        f.write(json.dumps(listdata, ensure_ascii=False, default=default))
    f.close()
except pyodbc.DatabaseError as err:
    print(err)
finally:
    cursor.close()
    cnx.close()
    # f.close()
