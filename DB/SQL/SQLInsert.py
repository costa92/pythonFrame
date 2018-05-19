# -*- coding: utf-8 -*-


class SQLInsert():
    def __init__(self, table=''):
        self.table = table
        self.sql = ''

    def getSQL(self,data):
        dataArr=self.cond_dict(data)
        sql = 'INSERT INTO %s (%s)VALUES(%s)' % (self.table,dataArr[0], dataArr[1])
        return sql

    def cond_dict(self,data):
        dataArr = []
        key =  value =  ''
        if data != '':
            for k, v in data.items():
                if key == '':
                    key = k
                else:
                    key = key + ',' + k

                if value == '':
                    value = "'"+v+ "'"
                else:
                    value = value + ',' + "'"+v+ "'"

                dataArr = [key,value]

        return dataArr


