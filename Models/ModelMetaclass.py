# -*- coding: utf-8 -*-

from DB.DataHelper import DataHelper  # 引用类文件
import logging;

class ModelMetaclass(type):

    def __new__(cls,name,bases,attrs):#当前准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合。
        if name == 'Model': #排除掉对Model类的修改；
            return type.__new__(cls,name,bases,attrs)
        tableName = attrs.get('__table__',None) or name
        logging.info('found a model: %s (table: %s)'%(name,tableName))
        # 获取所有的Field和主键名:
        mappings = dict() #保存映射关系
        fields = [] #保存除主键外的属性
        primarykey = None
        for k,v in attrs.items():
            if isinstance(v,Field):
                logging.info('Found mapping: %s ==> %s'%(k,v))
                mappings[k] = v
                if v.primary_key: #找到主键名
                    if primarykey:
                        raise StandardError('Duplicate primary key for field: k'%k)
                    primarykey = k #此列设为列表的主键
                else:
                    fields.append(k) #保存除主键外的属性
        if not primarykey:
            raise StandardError('primary key not found.')
        for k in mappings.keys():
            attrs.pop(k) #从类属性中删除Field属性,否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）
        escaped_fields = list(map(lambda f: "`%s`"%f,fields))#转换为sql语法
        #创建供Model类使用属性
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = tableName #表的名字
        attrs['__primary_key__'] = primarykey # 主键属性名
        attrs['__fields__'] = fields # 除主键外的属性名
        attrs['__select__'] = 'select `%s`,%s from %s'%(primarykey,','.join(escaped_fields),tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primarykey, create_args_string(len(escaped_fields) + 1))#占位符
        attrs['__update__'] = 'update `%s` set %s where `%s`=?'%(tableName,','.join(map(lambda f: '`%s`=?'%(mappings.get(f).name or f),fields)),primarykey)#查询列的名字，也看一下在Field定义上有没有定义名字，默认None
        attrs['__delete__'] = 'delete from `%s` where `%s`=?'%(tableName,primarykey)
        return type.__new__(cls,name,bases,attrs)