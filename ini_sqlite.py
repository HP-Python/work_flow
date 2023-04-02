import sqlite3
import os

db_path = '/home/harry/dev/test_sqlite.db'
def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d

if os.path.exists(db_path):
    print('db exists | deleting')
    os.remove(db_path)
try:
    con = sqlite3.connect(db_path)
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = """
        CREATE TABLE SCRIPT_MONITOR (
        NAME TEXT,
        STATE NUMBER)
        """
    cur.execute(sql)

    sql = 'select * from SCRIPT_MONITOR'
    cur.execute(sql)
    ret = cur.fetchall()
    print(ret)

except Exception as e:
    print(e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
