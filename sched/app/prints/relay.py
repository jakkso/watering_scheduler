""""""
import typing as tp

from flask import Blueprint, redirect, url_for

from sched.pin import Pin

relay_bp = Blueprint("relay_bp", __name__)


@relay_bp.route("/toggle", methods=["GET"])
def relay() -> tp.Tuple[str, int]:
    """Control relay."""
    Pin().toggle()
    return redirect(url_for("root_bp.index"))
