from .front import front
from .course import course
from .admin import admin
from .user import user


def register_blueprints(app):
    from . import front, course, admin, user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)
