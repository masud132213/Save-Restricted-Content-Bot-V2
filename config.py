# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "5587539"))
API_HASH = getenv("API_HASH", "8670b598fef377e6782429b1f664dce6")
BOT_TOKEN = getenv("BOT_TOKEN", "7118971920:AAEpHDDq46N6i80faTvl6lEH6zdIAXHCRVs")
OWNER_ID = int(getenv("OWNER_ID", "1826754085"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://lelej78399:8uH6Z0GYhX9sizXp@cluster0.zymda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002173891727"))
FORCESUB = getenv("FORCESUB", "saverestricted_BD")
