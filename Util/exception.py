# coding:utf-8
from Config.Conf import Conf

class Test_URL_Fail(Exception):
    def __str__(self):
        conf = Conf()
        str = "访问%s失败，请检查网络连接" % conf.getDefault('TestIP')
        return str


class Con_DB_Fail(Exception):
    def __str__(self):
        conf = Conf()
        str = "使用DB_CONNECT_STRING:%s--连接数据库失败" % conf.getDefault('DBData')
        return str


class Con_DB_Create_Fail(Exception):
    def __str__(self):
        str = "数据插入保存失败"
        return str