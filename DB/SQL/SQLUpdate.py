# -*- coding: utf-8 -*-


class SQLUpdate():
    def __init__(self, table=''):
        self.table = table
        self.sql = ''


    # 更新多个SQL
    def getSQLAll(self,datas,searchKeys):
        sets = {}
        updateSql = "UPDATE `" + self.table + "` set "
        whereValues = []
        whereKey = "WHERE CONCAT(`" + "`,',',`".join(searchKeys) + "`) IN "
        for data in datas:
            whereValue = []
            for searchKey in searchKeys:
                whereValue.append(data[searchKey])
            whereValueString = ",".join(whereValue)
            whereValues.append(whereValueString)
            for key in data:
                if key in searchKeys:
                    pass
                else:
                    searchValue = []
                    for searchKey in searchKeys:
                        searchValue.append(str(data[searchKey]))
                    searchValueString = ",".join(searchValue)
                    try:
                        sets[key][searchValueString] = data[key]
                    except KeyError as e:
                        sets[key] = {}
                        sets[key][searchValueString] = data[key]
        searchKeysString = "(`" + "`,',',`".join(searchKeys) + "`)"
        whereValuesString = "('" + "','".join(whereValues) + "')"
        setStringArray = []
        for key1 in sets:
            setString = ""
            for key2 in sets[key1]:
                if setString == "":
                    setString = "`" + key1 + "` = CASE WHEN (CONCAT" + searchKeysString + "='" + key2 + "') THEN '" + \
                                sets[key1][key2] + "'"
                else:
                    setString = setString + " WHEN (CONCAT" + searchKeysString + "='" + key2 + "') THEN '" + sets[key1][
                        key2] + "'"
            setString += " END "
            setStringArray.append(setString)
        setStrings = ",".join(setStringArray)
        whereStrings = whereKey + whereValuesString
        updateSql += setStrings
        updateSql += whereStrings

        return updateSql

    def getSQL(self,datas,searchKeys ):
        updateSql = "UPDATE `" + self.table + "` set "

