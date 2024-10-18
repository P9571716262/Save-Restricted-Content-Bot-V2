# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24793246"))
API_HASH = getenv("API_HASH", "4c19bc941eec1b863336d717dafc6f06")
BOT_TOKEN = getenv("BOT_TOKEN", "8042134692:AAHaSbNp55qmpHng8z3FsjFut6iGU7gSCoM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6172202347").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://pks_900:zmil7xlBYBaTBSca@cluster0.dm5qp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002393231571"))
