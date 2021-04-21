import requests
import jinja2
import datetime
import random
import time as tm



def data_generator():



    time = datetime.datetime.now().strftime('%H:%M:%S')
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    t1 = random.randint(0, 10)
    t2 = random.randint(0, 10)
    t3 = random.randint(0, 10)
    t4 = random.randint(0, 10)

    return t1, t2, t3, t4, time, date



def post_method():
    chanel = f'chanel{random.randint(0, 5)}'
    t1, t2, t3, t4, time, date = data_generator()


    url = f'http://projzal.herokuapp.com/{chanel}'
    headers = {'content-length': '108', 'Content-Type': 'application/json','X-User-Token': 'HsudXwo.token.uzytkownika'}
    k1 = 5000
    json = {

        "t1": t1,
        "t2": t2,
        "t3": t3,
        "t4": t4,
        "time": time,
        "date": date
    }

    req = requests.post(url, headers=headers, json=json)

    print(req.status_code)
    print(req.headers)
    print(req.text)
    return req

def get_method():
    url = 'http://projzal.herokuapp.com/list'
    headers = {'content-length': '108', 'Content-Type': 'application/json'}

    req = requests.get(url)

    print(req.status_code)
    print(req.headers)
    print(req.text)



d_cont = 0

tconst=5 #constant time between  between sending implus###############################################

start = int(tm.time())



while True:

    stop = int(tm.time())
    delta =  stop - start
    if delta != d_cont :
        if delta%tconst==0:

            if post_method().status_code in (200,201) :
                 print(f'delta {delta} wysłano')
                 d_cont = delta
                 print('zawartość bazy' )
                 get_method()




#get_method()
