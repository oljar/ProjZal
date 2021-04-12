import os
import sqlite3
from werkzeug.security import check_password_hash
from flask import Flask,Blueprint, request,render_template, redirect, session,url_for
from flask_restful import Resource, Api
import json
import data_operation
import jinja2

chart_2= Blueprint('chart_2_endpoints', __name__, url_prefix='/')


@chart_2.route('/chart_2', methods=['POST'])
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

    data=data_operation.get_data_db(da_ti)

    print(data)
    data_1 =[]
    for i in range(len(data)):
        one_sample = [data[i][0],data[i][2],data[i][3],data[i][4],data[i][5]] #[x,y,y]
        data_1.append(one_sample)

    v_axis_name ='pomiar'
    h_axis_name = 'Temeratura '+u"\u2103"
    name=('','czujnik 1','czujnik 2','czujnik 3','czujnik 4')



    return render_template('chart_21.html', name=name , h_axis_name = h_axis_name , v_axis_name  = v_axis_name , data=data_1)



