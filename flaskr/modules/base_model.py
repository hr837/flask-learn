
from datetime import datetime
import sqlalchemy as sa
from ..exts import db  

class BaseModel(db.Model):
    '''基础模型

       createAt: 创建时间

       updateAt: 更新时间
    '''
    __abstract__  = True
    createAt = sa.Column(sa.DateTime, nullable=False, default=datetime.now,comment="创建时间")
    updateAt = sa.Column(sa.DateTime, onupdate=datetime.now,comment="更新时间")