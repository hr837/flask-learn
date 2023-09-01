from flask import Blueprint

bp_index = Blueprint('index',__name__,)
'''根路由模块'''

@bp_index.route("/")
def hello():
    return "Hello World!"
