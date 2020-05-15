""""""
from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_ENV = getenv("FLASK_ENV") or "production"
    SECRET_KEY = getenv("FLASK_KEY")
    PIN_NUMBER = getenv("PIN_NUMBER")
    FLASK_DEBUG = getenv("FLASK_DEBUG")


