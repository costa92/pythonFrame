# -*- coding: utf-8 -*-

from Config.Conf import Conf
from DB.RedisHelper import RedisHelper  # 引用redis
from DB.MysqlHelper import MysqlHelper  # 引用Mysql
from Util.exception import Con_DB_Fail

class DataHelper():

     def __init__(self):
          conf = Conf()
          self.DB = conf.getDefault('DBData')


     def getDB(self):
        try:
            if self.DB == "redis":
                return RedisHelper()
            elif self.DB == "mysql":
                return MysqlHelper()
            else:
                return None
        except Exception as e:
            raise Con_DB_Fail