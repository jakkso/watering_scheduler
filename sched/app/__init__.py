""""""
from flask import Flask

import sched.app.prints as prints


def create_app() -> Flask:
    """Return configured app."""

    app = Flask(__name__)
    app.register_blueprint(prints.root_bp)
    app.register_blueprint(prints.relay_bp)

    return app
