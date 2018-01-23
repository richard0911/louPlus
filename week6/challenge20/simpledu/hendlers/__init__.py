from .front import front
from .course import course
from .admin import admin
from .user import user
from .live import live
from .ws import ws
from flask_sockets import Sockets


def register_blueprints(app):
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(live)
    sockets = Sockets(app)
    sockets.register_blueprint(ws)
