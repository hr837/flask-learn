class __BaseConfig(object):
    '''默认配置'''
    SECRET_KET = '1234567890'


class DevConfig(__BaseConfig):
    '''开发配置'''
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db" # 数据库连接配置