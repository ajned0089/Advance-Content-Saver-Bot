from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27872897")
    API_HASH = environ.get("API_HASH", "c813ba7b7215484aa212f98ae1e8a686")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8049480268:AAFOT516JlELurkeImSn7IB6u5P38SG6K44") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7742356911').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
