import sqlalchemy as sa
from ..base_model import BaseModel

class UserModel(BaseModel):
    '''系统用户模型'''
    __tablename__  = "user"
    id = sa.Column(sa.Integer,autoincrement=True,primary_key=True)
    '''用户ID'''
    name =sa.Column(sa.String(50),comment="用户姓名")
    '''用户姓名'''
    email = sa.Column(sa.String(100),comment="电子邮箱")
    '''电子邮箱'''
    password=sa.Column(sa.String(100),default='888888')
