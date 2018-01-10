from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course
from simpledu.hendlers.__init__ import register_blueprints


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)

    return app