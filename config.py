import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 20046177
API_HASH = "83d15f2956be4b4b927acded8bdf780f"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "BOT_TOKEN"
# -------------------------------------------------------
OWNER_USERNAME = "zeni_og"
# --------------------------------------------------------
BOT_USERNAME = "marin_xpro_bot"
# --------------------------------------------------------
BOT_NAME = " Marin"
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Nezuko12:Nezuko12@cluster0.xchck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = "-1002116643591"

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = 5268691896


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/paradox-zenu/nikl",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    None 
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hxh_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/as_cosmos")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQFhiOoAJDwdxMqyhBz16SVhHiWyGKV8YmCYp3TZSiUwZFP0eWMds9CvdFdbJwvwe3IXS_zajQ_iKjNzMe9DDBAoyhumssaqj1kW0J09MxyFVE_MtMHvB0-R11fNLmEg3Zj0aEaVOZuOJRmfuuvgyeGO_tGj2gou_5o56-8mJ7JG_32jvTzVI5_ePCWsqHRck5fRYebZiYPWgyFSw1iVLtAjmE8rtve9A4ty_g7d34Q1oC40Td-CzoaEgKmO703eFR-hd4xClpaw5IfRbHbVVjefLo3FSKQ1wkKQzx3sxSwcHCxbPnvJSUescD4kKnyjMQS1CmoK9m_zdV2WNUfJZibJeGsN4gAAAAGdRV_JAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/wxwqv2.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/o2e21c.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/9acd828ec45a363add2e9.jpg"
STATS_IMG_URL = "https://files.catbox.moe/yfvai0.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
