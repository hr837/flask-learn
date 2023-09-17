from flask import Blueprint,request,json
from flaskr.exts import db
from sqlalchemy import select
from .user_model import UserModel
from flask import Blueprint
from .user_dto import UserSchema

bp_user = Blueprint("user",__name__,url_prefix="/users")
'''用户蓝图

basePath: /users
'''


@bp_user.get("/")
def query_all():
    '''查询所有用户'''
    # all = db.session.query(UserModel).all()
    # db.session.execute()
    
    stmt  = select(UserModel).where(UserModel.name == 'Duang')
    result = db.session.execute(stmt).scalars().all()
    return result

@bp_user.post("/")
def add_user():
    obj = request.get_json()
    user = UserModel(name=obj['name'],email=obj['email'])
    # user.name = obj['name']
    # user.email = obj['email']
    db.session.add(user)
    db.session.commit()
    print(obj)
    user_res = UserSchema().dump(user)
    return user_res