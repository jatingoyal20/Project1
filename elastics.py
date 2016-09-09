from elasticsearch import *
from elasticsearch_dsl import *
from datetime import datetime
import json
from collections import defaultdict
import json

from kafka import KafkaProducer

#kafka ip
producer = KafkaProducer(bootstrap_servers='10.5.16.75:9092')

#elastic api
elastic_client='http://10.5.16.75:9200'
es = Elasticsearch(elastic_client)



def get_filter(userName,fieldName,params): #params list
    leng=len(params)/2
    dis = defaultdict(list)
    for i in range(0,leng):
        dis[params[i][1]].append(params[i+leng][1])
    if fieldName in dis:
        del dis[fieldName]
    dis["userId"].append(userName)
    dis["_routing"].append(userName)
    print dis
    return dis

def funquery(userName,fieldName,endtime,starttime,params):
    finalquery = dict()
    query = dict()
    bool = dict()
    must = []
    for key,value in get_filter(userName,fieldName,params).iteritems():
        bools={}
        should=[]
        for values in value:
            should.append({"term": {key: values}})
        bools["should"]=should
        must.append({"bool":bools})

    bool["must"] = must

    timestamp = dict()
    timestamp["gte"] = starttime
    timestamp["lte"] = endtime

    range = {"timestamp": timestamp}
    filter = {"range": range}
    bool["filter"] = filter

    query["bool"] = bool

    finalquery["query"] = query

    field = {"field": fieldName+".raw"}
    terms = {"terms": field}
    fieldagg = {"fieldagg": terms}

    finalquery["aggs"] = fieldagg
    return finalquery

def jsonResponse(buckets): #for response on click
    print buckets
    jsonList = []
    for _pair in buckets:
        a = dict()
        a["key"] = _pair["key"]
        a["doc_count"] = _pair["doc_count"]
        jsonList.append(a)
    print jsonList
    return json.dumps(jsonList)

def insert(username,params):
    toInsert=dict()
    for cur in params:
        toInsert[cur[0]] = cur[1]

    toInsert["userId"] = username
    # add Timestamp
    toInsert["timestamp"] = (datetime.now().isoformat().split('.'))[0]

    print json.dumps(toInsert)

    producer.send('foobars', json.dumps(toInsert))
    return True

def query(username,params):
    query = funquery(username,params[1][1], params[0][1], params[2][1], params[3:])
    print json.dumps(query)
    response = es.search(index="lastseven_index", body=query)
    return jsonResponse(response['aggregations']['fieldagg']['buckets'])


