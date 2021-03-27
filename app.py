import os

from flask import Flask, request
from flask_restful import Resource, Api


import data_operation

app = Flask(__name__)

api = Api(app)

if not os.path.isfile('data.db'):
    data_operation.create_db()

print(data_operation)
items = []


class Item(Resource):

    def get(self, name):
        solution = []
        for item in items:
            if item['name'] == name:
                solution.append(item)
        return solution

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 't1': data['t1'], 't2': data['t2'], 't3': data['t3'], 't4': data['t4'],
'date': data['date'], 'time': data['time']}
        items.append(item)
        data_operation.add_data_db(name, data['t1'], data['t2'], data['t3'], data['t4'], data['date'], data['time'])

        return item, 201


class ItemList(Resource):

    def get(self):
        return data_operation.get_data_db()


class ItemListName(Resource):

    def get(self, name):
        return data_operation.get_data_name_db(name)


@app.route('/')
def aaa():
    return 'oki'


api.add_resource(Item, '/<string:name>')
api.add_resource(ItemList, '/list')
api.add_resource(ItemListName, '/list/<string:name>')

# app.run(debug=True)


if __name__ == "__main__":
   #port = int(os.environ.get("PORT", 5000))
   #app.run(host='0.0.0.0', port=port)

   app.run(debug=True)
#app.run()
