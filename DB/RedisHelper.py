#coding = utf-8
import redis
from Config.Conf import Conf

class RedisHelper():
    def __init__(self):
        config = Conf()
        host = config.getRedis('host')
        port = config.getRedis('port')
        db = config.getRedis('db')
        password = config.getRedis('password')
        self.__time = config.getRedis('activeTime')
        self.__redis = redis.StrictRedis(host, port,db,password)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""

    def set(self, key, val):
        self.__redis.set(key, val)


    def setex(self, key, val,time = 0):
        time =(time if(time > 0) else self.__time)
        self.__redis.setex(key,time,val)


    def first(self,key):
        return self.get(key)


