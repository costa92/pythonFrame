# -*- coding: utf-8 -*-


class SQLSelect():

    def __init__(self,table = ''):
        self.table = table
        self.sql = ''

    def getSQL(self,condition = '', columns = '', order= '',limit = 0):
        if condition != '':
            conditionSQL = self.cond_dict(condition)
            self.sql = "SELECT %s FROM %s WHERE %s" % (columns, self.table, conditionSQL)
        else:
            self.sql = "SELECT %s FROM %s" % (columns, self.table)

        if order != '':
            sql = self.sql + ' ORDER BY ' + order

        if limit != 0:
            sql = sql + ' limit ' + limit

        return sql

    def cond_dict(self,condition = ""):
        if condition != "":
            consql = ""
            for k,v in condition.items():
                consql = consql + k + '="' + v + '" and'
            consql = consql + ' 1=1 '
            return consql
        else:
           return  ""