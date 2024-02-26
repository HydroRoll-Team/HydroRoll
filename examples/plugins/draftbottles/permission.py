from iamai import Event, Depends
from .database import Database


class Permission:
    event: Event = Depends()
    database: Database = Depends()

    def is_admin(self):
        return self.event.user_id in self.database.admin_list
