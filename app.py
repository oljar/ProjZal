import os
import sqlite3
from werkzeug.security import check_password_hash
from flask import Flask, request,render_template, redirect, session,url_for,jsonify
from flask_restful import Resource, Api
import json
import data_operation
import jinja2
from chart_2_bp import chart_2

import requests
from functools import wraps
from werkzeug.exceptions import abort



def authenticate_request(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):

        # w rzeczywistej aplikacji dla każdego użytkownika powinien być wygenerowany osobny token
        token_from_database = 'HsudXwo.token.uzytkownika'

        if request.headers.get('X-User-Token') == token_from_database:
            # jeśli użytkownik przekazał w zapytaniu poprawny token, dostanie dostęp do zasobu
            return view(*args, **kwargs)
        else:
            abort(401)

    return wrapped_view






app = Flask(__name__,template_folder='templates')

api = Api(app)
app.secret_key = 'tajny-klucz-hQmJW0Sz2K'
app.register_blueprint(chart_2)

if not os.path.isfile('data.db'):
    data_operation.create_db()


items = []


class Item(Resource):

    @authenticate_request
    def get(self, name):
        solution = []
        for item in items:
            if item['name'] == name:
                solution.append(item)
        return solution


    @authenticate_request
    def post(self, name):
        data = request.get_json()
        item = {'name': name, 't1': data['t1'], 't2': data['t2'], 't3': data['t3'], 't4': data['t4'],'date': data['time'], 'time': data['date']}
        items.append(item)
        data_operation.add_data_db(name, data['t1'], data['t2'], data['t3'], data['t4'], data['time'], data['date'])

        return item, 201


class ItemList(Resource):

    @authenticate_request
    def get(self):

        data=data_operation.get_data_db_all()


        return data


class ItemListName(Resource):


    def get(self, name):
        return data_operation.get_data_name_db(name)



@app.route('/')
def index():

        if not session:
            return redirect(url_for('login'))

        canals=data_operation.get_channel()


        return render_template('index.html',canals=canals)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        conn =sqlite3.connect("data.db")
        #conn.row_factory = sqlite3.Row
        c=conn.cursor()
        query = """
        SELECT * FROM "users" WHERE "username" = ?;
        """
        username=username
        c.execute(query,(username,))
        user_data = c.fetchall()
        print (user_data)



        if user_data:
            password_from_db = user_data[0][2]

            if check_password_hash(password_from_db, password):
                session['username'] = user_data[0][1]
                return redirect(url_for('index'))


    return 'błąd!'


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


api.add_resource(Item, '/<string:name>')
api.add_resource(ItemList, '/list')
#api.add_resource(ItemListName, '/list/<string:name>')






if __name__ == "__main__":

     app.run(debug=True)
