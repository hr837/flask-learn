from flaskr.exts import db
# from sqlalchemy import Column,Integer, String

class UserModel(db.Model):
    '''系统用户模型'''
    __tablename__  = "user"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    '''用户ID'''
    name =db.Column(db.String,nullable=False)
    '''用户姓名'''