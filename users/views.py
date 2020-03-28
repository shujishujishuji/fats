from apps.app import api
from users.service import UserService
from apps.db import to_json


class UsersBaseView:
    def __init__(self):
        self.service = UserService()

    def __del__(self):
        del self.service


class UsersSearchView(UsersBaseView):
    async def on_request(self, req, resp):
        users = self.service.find_all()
        resp.content = api.template('users/users.html', list=users) 


class UsersView(UsersBaseView):
    async def on_request(self, req, resp, id=None):
        user = self.service.find_by_id(id)
        resp.content = api.template('users/user.html', data=user) 
