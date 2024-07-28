import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7029383019:AAGmgfEwT17E-w9wkbhHAiJF1aHrEKLxMfk")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 13384432))
    API_HASH = os.environ.get("API_HASH","ea9db4503ed7088b788e06dfd818e00e")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    # Array to store users who are authorized to use the bot
    AUTH_USERS = int(os.environ.get("AUTH_USERS", "6169288210"))
    # database uri (mongodb)
    DATABASE_NAME = "JOSProjects"
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mrhex86:mrhex86@cluster0.8pxiirj.mongodb.net/?retryWrites=true&w=majority")
    MAX_RESULTS = "50"
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1002205938557")
