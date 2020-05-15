""""""
from flask import Flask

import sched.app.prints as prints
from sched.config import Config


def create_app() -> Flask:
    """Return configured app."""

    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(prints.root_bp)

    return app
