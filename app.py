from flask import Flask, request
from flask_restful import Resource, Api

import data_operation

app = Flask(__name__)

api = Api(app)

data_operation.create_db()

items = []

class Item (Resource):

    def get(self,name):
        solution= []
        for item in items :
            if item['name']== name:
                solution.append(item)
        return solution




    def post (self,name):
        data = request.get_json()
        item = {'name' : name , 't1' : data['t1'], 't2' : data['t2'], 't3' :data['t3'] ,'t4': data['t4']}
        items.append(item)
        data_operation.add_data_db(name,data['t1'],data['t2'],data['t3'],data['t4'])

        return item,201

class ItemList(Resource):

    def get (self):
        return data_operation.get_data_db()

class ItemListName(Resource):

    def get (self,name):
        return data_operation.get_data_name_db(name)




@app.route('/')
def aaa():
        return 'ok'

api.add_resource(Item,'/<string:name>')
api.add_resource(ItemList,'/list')
api.add_resource(ItemListName,'/list/<string:name>')


#app.run(debug=True)


