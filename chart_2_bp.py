import os
import sqlite3
from werkzeug.security import check_password_hash
from flask import Flask,Blueprint, request,render_template, redirect, session,url_for
from flask_restful import Resource, Api
import json
import data_operation
import jinja2
import datetime

chart_2= Blueprint('chart_2_endpoints', __name__, url_prefix='/')


@chart_2.route('/chart_2', methods=['get', 'post'])
def line_chart_2():


    data_start = request.form.get('data_start')
    time_start = request.form.get('time_start')

    data_stop = request.form.get('data_stop')
    time_stop = request.form.get('time_stop')

    format_data = "%Y-%m-%d"
    format_time = "%H:%M"






    if request.form.get('all_delete') == 'all_delete' or  request.form.get('serie_delete') == 'serie_delete' :
        data_start = '2021-01-01'
        time_start = '10:10'

        data_stop = '2021-01-01'
        time_stop = '10:10'


    else:

            try:
                datetime.datetime. strptime(time_start, format_time)
            except :
                return render_template('fill_db.html')

            try:
                datetime.datetime. strptime(data_stop, format_data)
            except :
                return render_template('fill_db.html')


            try:
                datetime.datetime. strptime(time_stop, format_time)
            except :
                return render_template('fill_db.html')



            try:
                datetime.datetime. strptime(data_start, format_data)
            except :
               return render_template('fill_db.html')






    if request.form.get('all_delete') == 'all_delete':

        data_operation.all_delete()
        return render_template('fill_db.html')




    da_ti =(data_start,time_start,data_stop,time_stop)


    try :
        channel_list = data_operation.get_channel()
    except:
        return 'Brak banych'

    try :
        list_position = int(request.form.get('select_list'))
    except:
        return render_template('fill_db.html')



    channel_name = channel_list[list_position-1]

    data = data_operation.get_data_time_name_db(da_ti,channel_name)



    data_1 =[]
    for i in range(len(data)):
        one_sample = [data[i][0],data[i][2],data[i][3],data[i][4],data[i][5]] #[x,y,y]
        data_1.append(one_sample)

    v_axis_name ='pomiar'
    h_axis_name = 'Temperatura '+u"\u2103"
    name=('','czujnik 1','czujnik 2','czujnik 3','czujnik 4')

    canals=data_operation.get_channel()



    if request.form.get('serie_delete') == 'serie_delete':

        data_operation.serie_delete(channel_name)
        return redirect (url_for('index'))


    try :
        channel_list = data_operation.get_channel()
    except:
        return 'Brak banych'

    list_position = int(request.form.get('select_list'))
    channel_name = channel_list[list_position-1]



    return render_template('chart_21.html', name=name , h_axis_name = h_axis_name , v_axis_name  = v_axis_name , data=data_1, channel_name=channel_name)



