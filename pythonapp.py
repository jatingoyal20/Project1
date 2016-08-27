from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()


res = es.search(index="app", doc_type="users",body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])