import random

from collections import defaultdict

totalqueries=100000
field_disct=50
value_disct=50
field_length=10
value_length=10

def bool():
    return int(random.random() * 2)


def randomfield(size):
    str=""
    for i in range(0,size):
        cur= random.random() * 26 + ord('a') # character between ['a','z']
        str+=chr(int(cur))
    return str

fields=defaultdict()

for i in range(0,field_disct):
    fsize=int(random.random() * field_length + 1) # from (1,field_length)
    field=randomfield(fsize)
    #print field
    list=[]
    for j in range(0,value_disct):
        vsize = int(random.random() * value_length + 1)  # from (1,value_length)
        list.append(randomfield(vsize))
    fields[field]=list

r = open("bashscript.sh", 'w')
r.write("#!/bin/bash\n")
url="curl 'http://172.16.164.100:5000/insert?"
for i in range(0,totalqueries):
    ct=0
    str=""
    for k,v in fields.iteritems():
        if(bool()):
            ct+=1
            str+=k+"="
            vsize = int(random.random() * value_disct)  # from (0,value_disct-1)
            str+=v[vsize]
            str+="&"
    str=str[:-1]
    if(ct==0):
        continue
    r.write(url+str+'\'\n')
r.close()

