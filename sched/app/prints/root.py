"""Contain root route."""

import typing as tp

from flask import Blueprint, render_template, redirect, url_for
from sched.pin import Pin

root_bp = Blueprint("root_bp", __name__)


@root_bp.route("/", methods=["GET"])
def index() -> tp.Tuple[str, int]:
    """Return index route."""
    classes = {0: ("waterOn", "on"), 1: ("waterOff", "off")}

    css_class, text = classes.get()
    return render_template("index.html", css_class=css_class, text=text, href="toggle")


@root_bp.route("/toggle")
def toggle() -> redirect:
    """Toggle pin state."""
    with Pin() as pin:
        pin.toggle()
    return redirect(url_for("root_bp.index"))
