from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
'''数据库访问实例'''

from flask_migrate import Migrate
migrate = Migrate()
'''数据库迁移实例'''

