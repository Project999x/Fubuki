#Recoded by @WhiteBeard_Sama

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7045736874:AAENiVmwfUFqcYmLD9oA-_RTf4PMlEGhQl8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28525384"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3a1190585fe5bf1f6324be87ba5b68c6")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001985214229"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1418213560"))

#Port
PORT = os.environ.get("PORT", "9023")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
DB_NAME = os.environ.get("DATABASE_NAME", "fubuki_x_robot_bot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002465142238"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002303321406"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://envs.sh/rSi.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/rSP.jpg")

#text
HELP_TXT = "<b>Hi Dude!\n\nTo use this bot you just have to join both channels that's it..\nWatch Tutorial to open Link - <a href=https://t.me/+ZLu08PF-JUIzMjFl>Clickhere</a></b>"
ABOUT_TXT = "<b><i>About Us..\n\n‣ Made for : <a href=https://t.me/+sOF6oYv8MPVmOGQ1>ClickHere</a>\n‣ Owned by : @Whitebeard_Sama\n‣ Maintained by : @Whitebeard_Sama\n‣ Developed by : @Shirohige_Animes\n\n Adios !!</i></b>"
SHORT_MSG = "Your Link is down here click on Short URL.."

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href=https://t.me/Shirohige_Animes>ᴀɴɪᴍᴇ ᴅʀɪғᴛ</a></b>")
try:
    ADMINS=[1418213560]
    for x in (os.environ.get("ADMINS", "6587003349 7827448605 8160777407").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "shortxlinks.com")
SHORT_API = os.environ.get("SHORTNER_API", "a1a273743377a90c8ac73babb61b2b31a81e6416")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @Shirohige_Animes"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "1800"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1418213560)

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
