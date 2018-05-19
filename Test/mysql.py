# -*- coding: utf-8 -*-

import os
import sys
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(parent_path)


from DB.DataHelper import DataHelper  # 引用类文件

def main():
     updateAll()


def updateAll():
    db = DataHelper().getDB()
    data = [{'migration': "created_users_tablew3", 'batch': '1', 'id': '4'},
            {'migration': "created_users_table633", 'batch': '1', 'id': '6'}]
    searchKeys = ['id']
    db = db.updateAll('migrations', data, searchKeys)

if __name__ == '__main__':
    main()
