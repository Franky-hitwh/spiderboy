#coding=utf-8
"""
    调用Info.py，获取数据并插入数据库
"""
import excel
from db import *
from sqlalchemy.orm import mapper
import info
import traceback

db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'db': 'gk_infomation',
}

class Database:
    """
        初始化和定义数据库操作
    """
    def __init__(self):
        engine = create_engine('mysql://%s:%s@%s/%s' % (db_config['user'],
            db_config['passwd'],
            db_config['host'],
            db_config['db']), echo=True)
        self.metadata = Base.metadata
        db_session = sessionmaker(bind=engine)
        self.session = db_session()

    def insert(self, rows):
        #GK_14_L = Table('GK_14_L', self.metadata, autoload=True)
        for row in rows:

            item = GK_13_L(nf=row[0], kl=row[1], zy=row[2], xx=row[3], pc=row[4], bzylqrs=row[5], zgfxc=row[6], zdfxc=row[7], pjfxc=row[8], zgf=row[9], zdf=row[10], pjf=row[11], zgfmc=row[12], zdfmc=row[13], pjfmc=row[14])
            self.session.add(item)

        self.session.commit()


    def insert_yx(self):
        pass

    def insert_zy_xw(self, rows):
        for row in rows:
            try:
                #print row
                item = ZY_INFO(xkml=row[0], zyl=row[1], zydm=row[2], zymc=row[3], xkdm=row[4], yjxk=row[5])
                self.session.add(item)
            except:
                print row
                print traceback.print_exc()
                break

        self.session.commit()

    def insert_xk(self, rows):
        for row in rows:
            try:
                #print row
                item = XK_INFO(xkdm=row[0], xkcc=row[1], xkmc=row[2], xx=row[3], add=row[4], yjxk=row[5])
                self.session.add(item)
            except:
                print row
                print traceback.print_exc()
                break

        self.session.commit()


    def finish(self):
        self.session.close()

#args = ['2014', '数据', '数据', '数据', '数据', '9', '650', '593', '617', '45', '8088', '48008', '27358']


db = Database()

rows = info.getRows()           #获取专业数据
db.insert(rows)                 #插入

zy_xws = info.getZyXwInfo()     #获取专业-学位表的数据
db.insert_zy_xw(zy_xws)         #插入

xks = info.getXkInfo()          #获取学科数据
db.insert_xk(xks)               #插入

db.finish()
