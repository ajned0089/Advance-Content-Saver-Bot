#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "27872897" #config("API_ID", default=None, cast=int)
API_HASH = "c813ba7b7215484aa212f98ae1e8a686" #config("API_HASH", default=None)
BOT_TOKEN = "8049480268:AAFOT516JlELurkeImSn7IB6u5P38SG6K44" #config("BOT_TOKEN", default=None)
SESSION = "BAGpToEAKqhcXRUHgPNRVe2mlrYOnZVawk_VtN6VqzIYdtKhzFclH2HLubTmlzQ9_sdg_KImNvTLnctciw8Zgg-PpxO2SfZEkbGvWtEP1avIWA5hkf2npY01-Zucpy6zDi8GMxa_VOd6muy56_rruzBL-lHpLksIfYYaSn1om8zADoEdPn3fteQj7TJZUHNFg0x9i3PQJQiNeCf4lVKuQdHRDb4uG_ag26c70q71Kk_PtOusYfJRf7gtbS0TRkxJ8FCFHBeWb5T-lZqOYeyOv9kajNDjW10GMLRLeC7RWLl35l4FR_JNb2qnaJe3HtW-YV8Iw0pXbKksHaJYsJ6rb49tUxf25gAAAAHNev2vAA" #config("SESSION", default=None)
FORCESUB = "" #config("FORCESUB", default=None)
AUTH = "7742356911" #config("AUTH", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
