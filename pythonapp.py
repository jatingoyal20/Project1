#!/usr/bin/env python

from flask import Flask , request ,render_template , session , url_for ,redirect , make_response
from datetime import datetime
from elasticsearch import *
from elasticsearch_dsl import *
import json

import json
es = Elasticsearch()

# create my flask application
app=Flask(__name__)

#setiing the secret key
app.secret_key ='rohitjoseph0808@gmail.com'

def get_id(): #from cookie
    return "admin"

def get_fields(): #from userId (via redis)
    return ['rr']

def get_filter(): #from sessionId (via redis)
    return [('rr',4)]

def get_start_time(): #from user
    return "2011-01-22T21:22:58"

def get_end_time(): #from user
    return "2017-01-22T21:22:58"


def funquery(fieldName):

    finalquery=dict()

    query = dict()

    bool = dict()

    must = []
    for f in get_filter():
        must.append({"term": {f[0]:f[1]}});

    bool["must"] = must

    timestamp = dict()
    timestamp["gte"] = get_start_time()
    timestamp["lte"] = get_end_time()

    range = {"timestamp": timestamp}
    filter = {"range": range}
    bool["filter"] = filter

    query["bool"] = bool

    finalquery["query"]=query

    field={"field":fieldName}
    terms={"terms":field}
    fieldagg={"fieldagg":terms}


    finalquery["aggs"]=fieldagg
    return finalquery

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

    #add user id
    print get_id()
    toInsert["userId"] = get_id()
    #add Timestamp
    toInsert["timestamp"] =(datetime.now().isoformat().split('.'))[0]

    print toInsert

    res = es.index(index="app", doc_type='users', body=json.dumps(toInsert))

    #to create
    if res['created'] == True :
        return render_template('register.html' , message = msg)
    else:
        return render_template('500.html' , message = msg)


# query GET
@app.route('/query', methods=['GET'])
def query_page():
    msg=True
    s=Search().using(es)

    finalFields=get_fields()
    print finalFields

    for currentfield in finalFields:
        query=funquery(currentfield)
        print query
        print json.dumps(query)
        s.update_from_dict(query).to_dict()
        response=s.execute()
        print response.hits.total

    return render_template('fields.html' , message = msg)



if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True, use_reloader=True)
