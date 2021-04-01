import sqlite3
import datetime


def create_db():

    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
        DROP TABLE IF EXISTS "stock";
        CREATE TABLE "stock" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "name"  TEXT,
        "t1"	REAL,
        "t2"	REAL,
        "t3"    REAL,
        "t4"	REAl,
        "Time"  STRING,
        "Date"  STRING
        
    );
    """
    c.executescript(query)
    conn.commit()
    conn.close()

def add_data_db(name,t1,t2,t3,t4,time,date):
    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
         INSERT INTO "stock" ("name", "t1", "t2", "t3", "t4", "time", "date")
         VALUES (:name, :t1, :t2, :t3, :t4, :time, :date);       
"""

    item = {"name":name, "t1":t1, "t2":t2, "t3":t3,"t4":t4, "time":time, "date":date }

    c.execute(query, item)

    conn.commit()
    conn.close()


def get_data_db(da_ti):
    da_ti_start = datetime.datetime.strptime(da_ti[0]+' '+da_ti[1],"%Y-%m-%d %H:%M")
    da_ti_stop = datetime.datetime.strptime(da_ti[2]+' '+da_ti[3],"%Y-%m-%d %H:%M")
    print (da_ti_start.time())
    print (da_ti_stop.time())
    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
    SELECT * FROM "stock" WHERE "time" > ? AND "time" < ? ;
    """

    c.execute(query,(str(da_ti_start.time()),str(da_ti_stop.time())))

    item =c.fetchall()
    return item

def get_data_name_db(name):
    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
    SELECT * FROM "stock" WHERE "name" = ?;
    """
    name=name
    c.execute(query,(name,))
    item =c.fetchall()
    return item
