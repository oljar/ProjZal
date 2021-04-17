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
        
        INSERT INTO "stock"
       
        VALUES
        (1, 'canal_1', 0, 0, 0 , 5,'05:00:00','2021-04-04'),
        (2, 'canal_1',1, 2, 2, 5,'05:05:00','2021-04-04'),
        (3, 'canal_1', 2, 3, 3, 4,'05:07:00','2021-04-04'),
        (4, 'canal_1', 3, 2, 5, 5,'05:09:00','2021-04-04'),
        (5, 'canal_2', 7, 8, 9, 10,'05:10:00','2021-04-04'),
        (6, 'canal_2', 6, 9, 9, 9,'05:14:00','2021-04-04'),
        (7, 'canal_2', 5,5, 5, 10,'05:17:00','2021-04-04');

        
        
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
    SELECT "*" FROM "stock" WHERE "name" = ?;
    """
    name=name
    c.execute(query,(name,))
    item =c.fetchall()
    return item








def get_channel():
    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
    SELECT "name" FROM "stock" ;
    """
    c.execute(query,)
    item =c.fetchall()
    channel_list=[]
    for i in item :
        channel_list.append (i[0])

    return list(set(channel_list))




def get_data_time_name_db(da_ti,channel_name):
    conn =sqlite3.connect("data.db")
    c=conn.cursor()

    query = """
    SELECT * FROM "stock"
    WHERE  datetime("Date","Time") > strftime('%Y-%m-%d %H:%M:S' ,?) AND datetime("Date","Time") < strftime('%Y-%m-%d %H:%M:S' ,?)AND "name" = ?  ;
   
    """





    t5= datetime.datetime.strptime(da_ti[0] +' '+ da_ti[1]+':00','%Y-%m-%d %H:%M:%S')
    t6= datetime.datetime.strptime(da_ti[2] +' '+ da_ti[3]+':00','%Y-%m-%d %H:%M:%S')


    c.execute(query,(t5,t6,channel_name))

    item =c.fetchall()
    return item


def all_delete():

    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
    DELETE FROM "stock" ;
    """
    c.execute(query,)
    conn.commit()


def serie_delete(channel_name):

    conn =sqlite3.connect("data.db")
    c=conn.cursor()
    query = """
    DELETE FROM "stock" WHERE "name" = ?;
    """
    c.execute(query,(channel_name,))
    conn.commit()




