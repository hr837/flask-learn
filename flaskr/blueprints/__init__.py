from flask import Blueprint
from .index import bp_index
from .auth import bp_auth
from .user import bp_user


def app_blueprints():
    '''获取蓝图注册的模块'''
    api_router = Blueprint("api",__name__,url_prefix="/api")
    api_router.register_blueprint(bp_auth)
    api_router.register_blueprint(bp_user)
    return [bp_index,api_router]