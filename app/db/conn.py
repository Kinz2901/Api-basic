"""Module responsable by create db connection"""
from contextvars import ContextVar
import peewee
from dotenv import dotenv_values
from playhouse.shortcuts import ReconnectMixin
config = dotenv_values(".env")

db_name = config['db_name']
db_host = config['db_host']
db_user = config['db_username']
db_password = config['db_password']

db_state_default: dict[str, None]= {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state: ContextVar[dict[str, None]] = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState): # type: ignore
    """Class representing peewee connection"""
    def __init__(self, **kwargs) -> None: # type: ignore
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs) # type: ignore

    def __setattr__(self, name, value) -> None: # type: ignore
        self._state.get()[name] = value # type: ignore

    def __getattr__(self, name: str) -> str:
        return self._state.get()[name] # type: ignore

class Ext_DB (ReconnectMixin, peewee.MySQLDatabase): # type: ignore
    pass
db = Ext_DB(db_name, **{
    'charset': 'utf8',
    'sql_mode': 'PIPES_AS_CONCAT',
    'use_unicode': True,
    'host': db_host,
    'user': db_user,
    'password': db_password
    }) # type: ignore

db._state = PeeweeConnectionState() # type: ignore
