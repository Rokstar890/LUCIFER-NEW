import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
API_ID = int(environ['23762978'])
API_HASH = environ['eff30dac5504a8660e69bfe19f668571']
BOT_TOKEN = environ['6335802263:AAFB1gPJQDTtYfXkbi0mmLvYlDcXbEUHiYo']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
@@ -32,9 +32,9 @@ def is_enabled(value, default):


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1216307744').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1216307744').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
@@ -43,24 +43,25 @@ def is_enabled(value, default):
FILDLT_CNL = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('FILDLT_CNL', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hebapir376:ravi1234@cluster0.x9pmpfx.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL  = -1001940288450")
DATABASE_NAME = environ.get('DATABASE_NAME', "EvaMaria")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/iPapkornMovieGroup')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/potterhub')
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/netflixrequstgroup1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Netflixvilla_india')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '+-ojTuVVnMehiZmU1')
MSG_ALRT = environ.get('MSG_ALRT', 'Share and Support Us')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', 0))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/+KxOOERk2WYdmNWM1')
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/+KEUXcl2WUT02MzA1')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001533446425'))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', '-1001533446425'))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001940288450'))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', '-1001940288450'))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
@@ -99,17 +100,17 @@ def is_enabled(value, default):
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


SHORTENER_API = environ.get("SHORTENER_API", "638bea22e5b27f9420265c902cb1051100513daa")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shorturllink.in")
SHORTENER_API = environ.get("SHORTENER_API", "00b0eacdca74780666d78f22ec43440e43994c2b")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "MdiskShortner.link")

SHORTENER_API2 = environ.get("SHORTENER_API2", "eO4VNo2S4vfJJwVBWuEtZnLlVzm2")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "shareus.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "00b0eacdca74780666d78f22ec43440e43994c2b")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "MdiskShortner.link")

SHORT_URL = is_enabled((environ.get('SHORT_URL', "True")), True)


TUTORIAL_LINK_2 = os.environ.get('TUTORIAL_LINK_2', 'https://youtu.be/k7DDXE530gA')
TUTORIAL_LINK_1 = os.environ.get('TUTORIAL_LINK_1', 'https://youtu.be/5FtwNbg2iYU')
TUTORIAL_LINK_2 = os.environ.get('TUTORIAL_LINK_2', 'https://t.me/Netflixvilla_india/46')
TUTORIAL_LINK_1 = os.environ.get('TUTORIAL_LINK_1', 'https://t.me/Netflixvilla_india/46')

