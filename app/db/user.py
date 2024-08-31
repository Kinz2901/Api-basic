from peewee import Model, CharField, IntegerField, ForeignKeyField
from app.db.conn import db

class BaseModel(Model):
    """Base class for models"""
    class Meta:
        """Subclass for table"""
        database = db


class User(BaseModel):
    """Class representing the table queue"""
    username = CharField(max_length=50)
    password = CharField(max_length=50)
    
    class Meta:
        """Subclass for table"""
        table_name: str = 'tb_users'
