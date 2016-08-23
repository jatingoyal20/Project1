import json

from datetime import datetime

def get_date_time():
	cur=datetime.now().isoformat()
	now=cur.split('.')
	cur=now[0]
	return now[0]
metajson="FDfdfdgTgdfgTg"
k = metajson.rfind("T")
new_string = metajson[:k] + "zz" + metajson[k+1:]
print new_string

y=[(1,2),(3,4)]
print y[0][1]


def get_id(): #from cookie
    return "admin"

def get_fields(): #from userId (via redis)
    return ['rr']

def get_filter(): #from sessionId (via redis)
    return []

def get_start_time(): #from user
    return "2011-00-22T21:22:58"

def get_end_time(): #from user
    return "2017-00-22T21:22:58"


def funquery(fieldName):
    query = dict()

    bool = dict()

    must = []
    for f in get_filter():
        must.append({"term": f[0]});

    bool["must"] = must

    gte = {"gte": get_start_time()}
    lte = {"lte": get_end_time()}

    timestamp = dict()
    timestamp["gte"] = gte
    timestamp["lte"] = lte

    range = {"timestamp": timestamp}
    filter = {"range": range}
    bool["filter"] = filter

    query["bool"] = bool

    field={"field":fieldName}
    terms={"terms":field}
    fieldagg={"fieldagg":terms}

    query["aggs"]=fieldagg
    return {"query":query}
y="{'query': {'bool': {'filter': {'range': {'timestamp': {'gte': '2011-00-22T21:22:58', 'lte': '2011-00-22T21:22:58'}}}, 'must': []}}, 'aggs': {'fieldagg': {'terms': {'field': 'rr'}}}}
"

print funquery("S")