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


cur=datetime.now()
cur.date=12
print cur