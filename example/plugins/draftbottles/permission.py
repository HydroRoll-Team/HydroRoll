from iamai import Event, Depends
from .database import Database


class Permission:
    event: Event = Depends()
    database: Database = Depends()
