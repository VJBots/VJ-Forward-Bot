# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ


def _get_required_env(name: str) -> str:
    value = environ.get(name, "").strip()
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def _get_required_int_env(name: str) -> int:
    value = _get_required_env(name)
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(
            f"Environment variable {name} must be an integer, got: {value!r}"
        ) from exc


class Config:
    API_ID = _get_required_int_env("API_ID")
    API_HASH = _get_required_env("API_HASH")
    BOT_TOKEN = _get_required_env("BOT_TOKEN")
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot").strip() or "vjbot"
    DATABASE_URI = _get_required_env("DATABASE_URI")
    DATABASE_NAME = (
        environ.get("DATABASE_NAME", "vj-forward-bot").strip() or "vj-forward-bot"
    )
    BOT_OWNER = _get_required_int_env("BOT_OWNER")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


class temp(object):
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
