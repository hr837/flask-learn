import os
from flask import Flask;
from .blueprints import app_blueprints
from .config import DevConfig
from .exts import *


def create_app():
    app  = Flask(__name__,instance_relative_config=True)
    app.config.from_object(DevConfig)
    # 初始化APP关联插件
    db.init_app(app)
    migrate.init_app(app,db)
    # 引入蓝图
    for bp in app_blueprints():
        app.register_blueprint(bp)

        
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    return app
