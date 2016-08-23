#!/usr/bin/env python

from flask import Flask , request ,render_template , session , url_for ,redirect , make_response
from datetime import datetime
from elasticsearch import Elasticsearch
import json
es = Elasticsearch()

# create my flask application
app=Flask(__name__)

#setiing the secret key
app.secret_key ='rohitjoseph0808@gmail.com'

fields=set()

def get_id():
    if 'name' in request.cookies:
        return request.cookies['name']

def get_field():
    return fields



@app.route("/login", methods=['GET','POST'])
@app.route("/", methods=['GET','POST'])
def login():

    if request.method == 'GET':
            msg = False
            return render_template('login.html', message = msg)

    if request.method == 'POST':

            u=request.form['username']
            p=request.form['password']

            if u == 'admin' and p =='admin':
                response = make_response(redirect('/query'))
                response.set_cookie('name', u)
                return response

            else :
                    msg= True
                    return render_template('login.html', message = msg)




# Insert the GET parameters
@app.route('/insert', methods=['GET'])
def default():
    params = request.args.items()
    jsonparams = json.dumps(params)
    toInsert = dict()
    msg = True

    #testing for correct input from client side
    for cur in params:
        if cur[0] == "" or cur[1] == "":
               return render_template('400.html' , message = msg)


    for cur in params:
        toInsert[cur[0]] = cur[1]
        fields.insert(cur[0]) #to remove later

    #add user id
    print get_id()
    toInsert["userId"] = get_id()
    #add Timestamp
    toInsert["timestamp"] =(datetime.now().isoformat().split('.'))[0]

    res = es.index(index="app", doc_type='users', body=json.dumps(toInsert))

    #to create
    if res['created'] == True :
        return render_template('register.html' , message = msg)
    else:
        return render_template('500.html' , message = msg)


# query GET
@app.route('/query', methods=['GET'])
def query_page():
    finalField=get_field()
    print finalField

    return render_template('500.html' , message = msg)



if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True, use_reloader=True)


