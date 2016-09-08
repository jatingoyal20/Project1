import requests
from bs4 import BeautifulSoup
r = requests.get('https://justpaste.it/xuo8')
soup = BeautifulSoup(r.text,'html.parser')
cur=soup.findAll("p")
ok =str(cur[0])
ok=ok[3:len(ok)-4]
print ok
ok=ok.replace("&lt;","<")
ok=ok.replace("&gt;",">")
ok=ok.replace("&amp;","&")
ok=ok.replace("nofollow","stylesheets")
ok = ok.replace("]", ")")

f=open("jatin")
d={}
d[6]=5
d[6]=d[6]-1
print d[6]
print ok