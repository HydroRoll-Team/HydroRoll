from iamai import Event, Depends
from .permission import Permission
from .database import Database


class WorkRoutes:
    event: Event = Depends()
    database: Database = Depends()
    permission: Permission = Depends()
