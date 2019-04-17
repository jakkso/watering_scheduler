"""Contain logging implementation."""

import logging
from logging.handlers import RotatingFileHandler
import pathlib


def logger() -> logging.getLogger:
    """Create logger."""
    filename = pathlib.Path(__file__).parent.parent / 'water_scheduler.log'
    log = logging.getLogger('water_scheduler')
    log.setLevel(logging.INFO)
    file_handler = RotatingFileHandler(filename=filename, delay=True, backupCount=1, maxBytes=2000000)
    file_handler.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s - %{message}s")
    file_handler.setFormatter(fmt)
    log.addHandler(file_handler)
    return log
