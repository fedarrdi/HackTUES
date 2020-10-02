import sqlite3 as sqlite
import sys
import functools
con = sqlite.connect('ydb.db')
cur = con.cursor()

def MakeTable():
    cur.execute("CREATE TABLE IF NOT EXISTS urlvis ( url TEXT )" )

def PushURL(URL):
    cur.execute("INSERT INTO urlvis(url) VALUES(?)", (URL, ))

def URLvis(URL):    
    cur.execute("SELECT COUNT(*) FROM urlvis WHERE url = ?", (URL, )) 
    return functools.reduce(lambda sub, ele: sub * 10 + ele, cur.fetchone())

