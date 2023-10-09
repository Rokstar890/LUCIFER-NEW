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
API_ID = int(environ[''])
API_HASH = environ['']
BOT_TOKEN = environ['']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
@@ -32,9 +32,9 @@ def is_enabled(value, default):


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
@@ -43,24 +43,25 @@ def is_enabled(value, default):
FILDLT_CNL = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('FILDLT_CNL', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
LOG_CHANNEL  = -1001940288450")
DATABASE_NAME = environ.get('DATABASE_NAME', ")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', '')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', ')
MSG_ALRT = environ.get('MSG_ALRT', 'Share and Support Us')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', 0))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', '')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', ''))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
@@ -99,17 +100,17 @@ def is_enabled(value, default):
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

SHORTENER_API = environ.get("SHORTENER_API", "")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "")

SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "")

SHORT_URL = is_enabled((environ.get('SHORT_URL', "True")), True)

TUTORIAL_LINK_2 = os.environ.get('TUTORIAL_LINK_2', '')
TUTORIAL_LINK_1 = os.environ.get('TUTORIAL_LINK_1', '')

