import sqlite3
from sys import argv
from admin import env

def test1(state_num):
    sql = f"UPDATE SCRIPT_MONITOR SET STATE={state_num} WHERE NAME='get_DLTBGXGC_datas'"
    cur.execute(sql)
    con.commit()
    cur.execute('select * from SCRIPT_MONITOR')
    print(cur.fetchall())

def test2():
    sql = "INSERT INTO SCRIPT_MONITOR (NAME,STATE) VALUES('get_DLTBGXGC_datas',1)"
    cur.execute(sql)
    con.commit()
    cur.execute('select * from SCRIPT_MONITOR')
    ret = cur.fetchall()
    print(ret)
def test3(arg):
    print(arg)


if __name__ == '__main__':
    con = sqlite3.connect(env.db_path)
    cur = con.cursor()
    # main
    test1(argv[1])
    # end main
    cur.close()
    con.close()

