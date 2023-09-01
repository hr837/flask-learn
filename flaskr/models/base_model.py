from datetime import datetime
from sqlalchemy import Column,DateTime

class BaseModel():
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)