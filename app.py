import os

from flask import Flask, request,render_template, redirect
from flask_restful import Resource, Api
import json
import data_operation
import jinja2
import requests


app = Flask(__name__,template_folder='templates')

api = Api(app)

if not os.path.isfile('data.db'):
    data_operation.create_db()


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
        item = {'name': name, 't1': data['t1'], 't2': data['t2'], 't3': data['t3'], 't4': data['t4'],'date': data['date'], 'time': data['time']}
        items.append(item)
        data_operation.add_data_db(name, data['t1'], data['t2'], data['t3'], data['t4'], data['date'], data['time'])

        return item, 201


class ItemList(Resource):

    def get(self):
        data_start = request.form.get('data_start')
        time_start = request.form.get('time_start')
        data_stop = request.form.get('data_stop')
        time_stop = request.form.get('time_stop')

        da_ti =(data_start,time_start,data_stop,time_stop)


        data=data_operation.get_data_db_all()

        return data


class ItemListName(Resource):

    def get(self, name):
        return data_operation.get_data_name_db(name)



@app.route('/')
def index():

      return render_template('index.html')







@app.route('/chart_2', methods=['POST'])
def line_chart_2():

    name_1=''
    name_2='linia_02'
    name_3='linia_02'
    name_4='linia_02'
    name_5='linia_02'

    data_start = request.form.get('data_start')
    time_start = request.form.get('time_start')

    data_stop = request.form.get('data_stop')
    time_stop = request.form.get('time_stop')

    da_ti =(data_start,time_start,data_stop,time_stop)

    data=data_operation.get_data_db_all()

    print(data)
    data_1 =[]
    for i in range(len(data)):
        one_sample = [data[i][0],data[i][2],data[i][3],data[i][4],data[i][5]] #[x,y,y]
        data_1.append(one_sample)

    v_axis_name ='pomiar'
    h_axis_name = 'temperatura'
    name=('','linia_1','linia_2','linia_3','linia_4')



    return render_template('chart_2.html', name=name , h_axis_name = h_axis_name , v_axis_name  = v_axis_name , data=data_1)



api.add_resource(Item, '/<string:name>')
api.add_resource(ItemList, '/list')
api.add_resource(ItemListName, '/list/<string:name>')



# app.run(debug=True)

# #
if __name__ == "__main__":
# #port = int(os.environ.get("PORT", 5000))
# #    #app.run(host='0.0.0.0', port=port)
# #
     app.run(debug=True)
# #app.run()
