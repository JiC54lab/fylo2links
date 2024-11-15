# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '19328466'))
    API_HASH = str(getenv('API_HASH', 'b2f81c541c4e66e7d167393c5dcd48ef'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5240374127:AAFSKFi2XaIhKd1v7chq1pvRx4aY8t7M1jw'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'JiC54'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001660906766'))
    PORT = int(getenv('PORT', 8000))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '104.22.78.190'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1324027496").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'jooma265'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '104.22.78.190:8000')) if not ON_HEROKU or getenv('FQDN', '104.22.78.190:8000') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://jic54autofilter:jic54autofilter@cluster0.nbp6y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'JiC54_official'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
