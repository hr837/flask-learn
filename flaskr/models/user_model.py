from flaskr.exts import db
from sqlalchemy import Column,Integer, String

class UserModel(db.Model):
    '''系统用户模型'''
    __tablename__  = "user"
    id = Column(Integer,autoincrement=True,primary_key=True)
    '''用户ID'''
    name =Column(String(50))
    '''用户姓名'''
    email = Column(String(100))
    '''电子邮箱'''
    password=Column(String(100),default='888888')