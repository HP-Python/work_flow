import sqlite3
from admin import env

def dict_factory(cursor, row):
    d = {}
    for index,col in enumerate(cursor.description):
        d[row[0]] = row[1]
    return d
def get_script_state():
    # return dict{'name',state}
    cur, con, ret = None,None,None
    try:
        con = sqlite3.connect(env.db_path)
        cur = con.cursor()
        cur.row_factory = dict_factory
        sql = 'SELECT NAME,STATE FROM SCRIPT_MONITOR'
        cur.execute(sql)
        ret = cur.fetchall()

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return ret[0]

