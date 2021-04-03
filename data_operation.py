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
        "time"  STRING,
        "date"  STRING
        );
        
        DROP TABLE IF EXISTS "users";
        
        CREATE TABLE "users"
        (
            "id"       INTEGER PRIMARY KEY AUTOINCREMENT,
            "username" TEXT    NOT NULL,
            "password" TEXT    NOT NULL
        );
        
        -- 'testowy' ma hasło 'testowy'
        INSERT INTO "users"
        VALUES (NULL, 'testowy', 'pbkdf2:sha256:150000$pZTQ81tw$0b4c87aaa463676d91c6c99690634288b1fae8a4f8a34df865ae72f504a50e0a');

        
        
   
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
    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    print (da_ti)
    query = """
    SELECT * FROM "stock" WHERE  datetime("Date","Time") > strftime('%Y-%m-%d %H:%M:S' ,?) AND datetime("Date","Time") < strftime('%Y-%m-%d %H:%M:S' ,?) ;
    """
    print ((da_ti[0],da_ti[2]))


    print (da_ti[1])

    t5= datetime.datetime.strptime(da_ti[0] +' '+ da_ti[1]+':00','%Y-%m-%d %H:%M:%S')
    t6= datetime.datetime.strptime(da_ti[2] +' '+ da_ti[3]+':00','%Y-%m-%d %H:%M:%S')


# "Time" > strftime('%Y-%m-%d',?) AND "Time" < strftime('%Y-%m-%d',?) AND
    c.execute(query,(t5,t6))

    item =c.fetchall()
    return item

def get_data_db_all():
    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
    SELECT * FROM "stock" ;
    """

    c.execute(query,)

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
