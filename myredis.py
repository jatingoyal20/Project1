import redis

# connecting to redis server
hosts='127.0.0.1'
ports=6379
r = redis.StrictRedis(host=hosts, port=ports, db=0)

def get_redis(key):
    a = r.smembers(key)
    a = list(a)
    return a
def add_list(username,params):
    for cur in params:
        r.sadd(username, cur[0])
