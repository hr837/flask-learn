from flask import Blueprint


bp_auth = Blueprint("auth",__name__,url_prefix="/auth")
'''授权蓝图

   basePath: /auth
'''


@bp_auth.get("/code")
def get_verifycode():
    '''获取验证码'''
    return '2389995'


@bp_auth.post("/login")
def user_login():
    '''用户登录'''
    return {
        "token":"12345678999",
        "avatar_url":"http://example.com/xfGxd98_2k"
    }