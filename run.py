# coding:utf-8

from DB.RedisHelper import RedisHelper  # 引用类文件
from DB.DataHelper import DataHelper  # 引用类文件

def main():
    db = DataHelper().getDB()
    # db.setex('11',33,5)
    where = {'id':"5"}
    rs = db.first('migrations',where,'migration','id desc')
    # rs = db.findAll('migrations',where,'migration','id desc')
    # rs = db.first('11')

    # redis = RedisHelper()
    # rs = redis.get('partner')
    print(rs)


if __name__ == '__main__':
    main()