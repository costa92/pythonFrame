# coding:utf-8
import ConfigParser

class Conf():
    def __init__(self,path='config.ini'):
        self.config = ConfigParser.ConfigParser()
        self.config.read(path)


    def get(self,apply,name):
        return self.config.get(apply,name)


    # 获取redis配置
    def getRedis(self,name):
        apply = 'redis'
        return self.get(apply,name)

    # 获取mysql配置
    def getMysql(self, name):
        apply = 'mysql'
        return self.get(apply, name)

    # 获取默认
    def getDefault(self,name):
        apply = 'default'
        return self.get(apply, name)
