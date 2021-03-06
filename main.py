from apps.app import api
from chart.views import websocket
from users.views import UsersView, UsersSearchView

# api.add_route('/', static=True)
api.add_route('/ws', websocket, websocket=True)
api.add_route("/users/findall", UsersSearchView)
api.add_route("/users/findbyid/{id}", UsersView)


api.run()
