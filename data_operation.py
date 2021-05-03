import datetime
import os
import logging
import psycopg2
logging.basicConfig(level=logging.DEBUG)
DATABASE_URL = os.environ['HEROKU_POSTGRESQL_ONYX_URL']

def create_db():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    c = conn.cursor()
    query = """
        DROP TABLE IF EXISTS "stock";
        CREATE TABLE "stock" (
        "id"       SERIAL PRIMARY KEY NOT NULL,
        "name"  VARCHAR(200),
        "t1"	REAL,
        "t2"	REAL,
        "t3"    REAL,
        "t4"	REAl,
        "time"  VARCHAR(400),
        "date"  VARCHAR(400)
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
            "id"       SERIAL PRIMARY KEY NOT NULL,
            "username" VARCHAR (400)   NOT NULL,
            "password" VARCHAR (400)  NOT NULL,
            "token"    VARCHAR (500) NOT NULL
        );
        
        -- 'testowy' ma hasło 'testowy'
        INSERT INTO "users"
        VALUES (1, 'testowy', 'pbkdf2:sha256:150000$pZTQ81tw$0b4c87aaa463676d91c6c99690634288b1fae8a4f8a34df865ae72f504a50e0a', 'pbkdf2:sha256:150000$j9TH0PIp$d07b8a533d1de17748d5f64c5a63e16f310ace0413ffab2628794950bc91da04');

        
        
   
    """
    c.execute(query)
    conn.commit()
    conn.close()


def add_data_db(name, t1, t2, t3, t4, time, date):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    query = """
         INSERT INTO "stock" ("name", "t1", "t2", "t3", "t4", "time", "date")
         VALUES (:name, :t1, :t2, :t3, :t4, :time, :date);       
"""

    item = {"name": name, "t1": t1, "t2": t2, "t3": t3, "t4": t4, "time": time, "date": date}

    c.execute(query, item)

    conn.commit()
    conn.close()


def get_data_db(da_ti):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    print(da_ti)
    query = """
    SELECT * FROM "stock" WHERE  datetime("Date","Time") > strftime('%Y-%m-%d %H:%M:S' ,?) AND datetime("Date","Time") < strftime('%Y-%m-%d %H:%M:S' ,?) ;
    """
    print((da_ti[0], da_ti[2]))

    print(da_ti[1])

    t5 = str(datetime.datetime.strptime(da_ti[0] + ' ' + da_ti[1] + ':00', '%Y-%m-%d %H:%M:%S'))
    t6 = str(datetime.datetime.strptime(da_ti[2] + ' ' + da_ti[3] + ':00', '%Y-%m-%d %H:%M:%S'))

    # "Time" > strftime('%Y-%m-%d',?) AND "Time" < strftime('%Y-%m-%d',?) AND
    c.execute(query, (t5, t6),)





    item = c.fetchall()
    return item


def get_data_db_all():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    query = """
    SELECT * FROM "stock" ;
    """

    c.execute(query, )

    item = c.fetchall()
    return item


def get_data_name_db(name):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    query = """
    SELECT "*" FROM "stock" WHERE "name" = ?;
    """
    name = name
    c.execute(query, (name,))
    item = c.fetchall()
    return item


def get_channel():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    query = """
    SELECT "name" FROM "stock" ;
    """
    c.execute(query, )
    item = c.fetchall()
    channel_list = []
    for i in item:
        channel_list.append(i[0])

    return list(set(channel_list))


def get_data_time_name_db(da_ti, channel_name):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()

    query = """
    SELECT * FROM "stock"
    WHERE  datetime("Date","Time") > strftime('%Y-%m-%d %H:%M:S' ,?) AND datetime("Date","Time") < strftime('%Y-%m-%d %H:%M:S' ,?)AND "name" = ?  ;
   
    """

    t5 = str(datetime.datetime.strptime(da_ti[0] + ' ' + da_ti[1] + ':00', '%Y-%m-%d %H:%M:%S'))
    t6 = str(datetime.datetime.strptime(da_ti[2] + ' ' + da_ti[3] + ':00', '%Y-%m-%d %H:%M:%S'))

    logging.debug(t5, t6,channel_name,)

    c.execute(query, (t5, t6,channel_name,))



    item = c.fetchall()
    return item


def all_delete():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    query = """
    DELETE FROM "stock" ;
    """
    c.execute(query, )
    conn.commit()


def serie_delete(channel_name):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    query = """
    DELETE FROM "stock" WHERE "name" = ?;
    """
    c.execute(query, (channel_name),)
    conn.commit()
