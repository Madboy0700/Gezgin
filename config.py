import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21233241"))
API_HASH = getenv("API_HASH", "00ddb4e997cff92de1506e2371bec2b2")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7910907997:AAHU5-MZ4cHcPeKfn-Mj2zQq7qvac33pM1o")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://acha:acha@cluster0.pjq3j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002330130767"))
# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "1860611760"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", #ticaret
    "https://t.me/Etikettaggerbot", 
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Bot_Destek") #duyuru
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Bot_Destek") #gurup

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFD_lkAq6EUuE3ctYjm-y5zLdBErsuX_qUyobkNSnkHgDV00gWI5dDaKPzUDF0o2WAlvUWM459srq0ZdcvmxeO3NxyyYrith0pMike3eiPTmvmI4hsOkPE0PBo25z6Yw7NowpPvCYum_6OsA-f007t3-pXuHtTALCtnP60_rV0svPdqmf2PZ3O7SualfzLETZ0kdnodSO3DqWad-6bhddjiEL9dAnizxNNbcPLreYZI-xg_Ho5qGlgHCaWK2YVUvXFIyCf-EeejOabrsvmucAMxNT8oit3AKHhkyXVe1nCRzttel0oMTloTdZw_qW6brtxzmBRqQS19czmAs_ekP0wY_vR9LAAAAAGxHTLHAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
)
PLAYLIST_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
STATS_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
TELEGRAM_AUDIO_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
TELEGRAM_VIDEO_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
STREAM_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
SOUNCLOUD_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
YOUTUBE_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
SPOTIFY_ARTIST_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
SPOTIFY_ALBUM_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"
SPOTIFY_PLAYLIST_IMG_URL = "https://pbs.twimg.com/media/Ge8YdS6W0AAeCdr?format=jpg&name=small"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



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
