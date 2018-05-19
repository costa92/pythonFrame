# -*- coding: utf-8 -*-

import MySQLdb
from Config.Conf import Conf
from DB.SQL.SQLSelect import SQLSelect
from DB.SQL.SQLInsert import SQLInsert
from DB.SQL.SQLUpdate import SQLUpdate
import logging
from Util.exception import Con_DB_Create_Fail

class MysqlHelper():

    def __init__(self):
        config = Conf()
        host = config.getMysql('host')
        dbName = config.getMysql('dbName')
        dbUser = config.getMysql('dbUser')
        password = config.getMysql('password')
        charset = config.getMysql('charset')
        self.__conn = MySQLdb.connect(host = host, user=dbUser, passwd = password,  db=dbName, charset=charset)
        self.__mysql = self.__conn.cursor()


    def first(self,table = '',condition = '',  columns ='*', order = ''):
        sql = self.getSelsctSQL(table, condition, columns, order)
        logging.info("This is debug message")
        self.__mysql.execute(sql)
        return self.__mysql.fetchone()


    def execute(self ,sql):
        self.__mysql.execute(sql)
        return  self.__mysql.fetchall()


    # 查询全部数据
    # condition  = {'id': '2'}
    # order  =  columns desc
    def findAll(self,table = '',condition = '',  columns ='*', order = ''):
        sql = self.getSelsctSQL(table,condition,columns,order)
        logging.info("This is debug message")
        self.__mysql.execute(sql)
        return self.__mysql.fetchall()

    def __del__(self):
        self.close()

    # 关闭mysql连接
    def close(self):
        self.__mysql.close()


    # 获取查询sql
    def getSelsctSQL(self,table = '', condition = '',  columns = '*', order = '',limit = 0):
        return SQLSelect(table).getSQL(condition,columns,order,limit)



    # 获取插入sql
    def getInsertSQL(self,table,data):
        return SQLInsert(table).getSQL(data)


    # 获取更新sql
    def getUpdateAllSQL(self, table, data,searchKeys):
        return SQLUpdate(table).getSQLAll(data,searchKeys)

        # 获取更新sql

    def getUpdateSQL(self, table, data, searchKeys):
        return SQLUpdate(table).getUpdateSQL(data, searchKeys)
    # 添加数据
    def created(self,table,data):
        try:
            sql = self.getInsertSQL(table,data)
            self.__mysql.execute(sql)
            # 提交到数据库执行
            self.__conn.commit()
            return int(self.__mysql.lastrowid)
        except Exception as e:
            # Rollback in case there is any error
            self.__conn.rollback()
            raise Con_DB_Create_Fail



    def updateAll(self,table,datas, searchKeys):
        # 同时更新多条数据
        if len(datas) == 0:
            return

        try:
            sql = self.getUpdateAllSQL(table, datas, searchKeys)
            self.__mysql.execute(sql)
            self.__mysql.fetchall()
            # 提交到数据库执行
            self.__conn.commit()
        except Exception as e:
            print e.message
            # Rollback in case there is any error
            self.__conn.rollback()
            raise Con_DB_Create_Fail

    # 更新一条数据
    def update(self, table, condition, data):

        if len(data) == 0 :
            return
        try:


            self.__conn.commit()
        except Exception as e:
            # Rollback in case there is any error
            self.__conn.rollback()
            raise Con_DB_Create_Fail