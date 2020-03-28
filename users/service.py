from apps.commons import ServiceBase
from apps.db import to_dict
from users.models import User


class UserService(ServiceBase):
    def find_all(self):
        ret = self.session.execute("select * from users").fetchall()
        return to_dict(ret)

    def find_by_id(self, id):
        users = self.session.query(User).\
            filter(User.id == id).\
            first()
        return to_dict(users)
