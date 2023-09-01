from flask import Blueprint,request
from flaskr.models import UserModel
from flaskr.exts import db

bp_user = Blueprint("user",__name__,url_prefix="/users")

@bp_user.get("/")
def query_all():
    '''查询所有用户'''
    return [{"name":"张三"},{"name":"李四"}]

@bp_user.post("/")
def add_user():
    data = request.get_json()
    print(data)
    
    return "OK"