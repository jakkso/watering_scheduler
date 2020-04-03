"""Settings for SMS listener."""
from os import environ as env

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Config values."""

    account_sid = env.get("account_sid")
    auth_token = env.get("auth_token")
