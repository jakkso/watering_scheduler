"""Contain root route."""

import typing as tp

from flask import Blueprint, render_template
from sched.pin import Pin

root_bp = Blueprint("root_bp", __name__)


@root_bp.route("/", methods=["GET"])
def index() -> tp.Tuple[str, int]:
    """Return index route."""
    classes = {0: ("waterOn", "on"), 1: ("waterOff", "off")}

    pin = Pin()
    css_class, text = classes.get(pin.state)
    return render_template("index.html", css_class=css_class, text=text)
