from apps.app import api

from users.views import UsersView, UsersSearchView

api.add_route("/users/findall", UsersSearchView)
api.add_route("/users/findbyid/{id}", UsersView)

api.run()
