from flask import Blueprint
from .auth_bp import bp_auth
from .user_bp import bp_user


bp = Blueprint('index',__name__,)
'''根路由模块'''

@bp.route("/")
def hello():
    return "Hello World!"

    

def app_blueprints():
    '''获取蓝图注册的模块'''
    api_router = Blueprint("api",__name__,url_prefix="/api")
    api_router.register_blueprint(bp_auth)
    api_router.register_blueprint(bp_user)
    return [bp,api_router]