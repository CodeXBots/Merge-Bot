import os


class Config(object):
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "LinkSearchbot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_OWNER = int(os.getenv("BOT_OWNER"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", '''{},

ɪ  ᴄᴀɴ  ᴘʀᴏᴠɪᴅᴇ  ᴍᴏᴠɪᴇs  ᴀɴᴅ  sᴇʀɪᴇs,
ᴊᴜsᴛ  ᴀᴅᴅ  ᴍᴇ  ᴛᴏ  ʏᴏᴜʀ  ɢʀᴏᴜᴘ  ᴀɴᴅ  ᴇɴᴊᴏʏ  😍''')
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/7de1d9ff50461400a22b6.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", START_MSG)
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "30"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''𝐇𝐎𝐖  𝐓𝐎  𝐔𝐒𝐄  𝐁𝐎𝐓  𝐈𝐍  𝐆𝐑𝐎𝐔𝐏 !!


🗣  ᴀᴅᴅ  ʙᴏᴛ  ᴀꜱ  ᴀᴅᴍɪɴ  ɪɴ  ʏᴏᴜʀ  ɢʀᴏᴜᴘ.

🗣  ᴛʏᴘᴇ  "/request"  ɪɴ  ɢʀᴏᴜᴘ.

🗣  ᴡᴀɪᴛ  ᴜɴᴛɪʟ  ʏᴏᴜʀ  ʀᴇǫᴜᴇꜱᴛ  ɪꜱ  ᴀᴘᴘʀᴏᴠᴇᴅ  ʙʏ  ᴏᴡɴᴇʀ.

🗣  ɪꜰ  ʏᴏᴜ  ᴡᴀɴᴛ  ᴛᴏ  ᴜꜱᴇ  ʏᴏᴜʀ  ʟɪɴᴋꜱ  ɪɴ  ɢʀᴏᴜᴘ  ᴛʜᴇɴ   👇  👇  

🗣  ʙᴜʏ  ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ  <a href="https://telegra.ph/SUPPORT-12-22-2">₹ 99/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°

𝐍𝐎𝐓𝐄 :  ɪꜰ  ʏᴏᴜʀ  ʀᴇǫᴜᴇꜱᴛ  ɪꜱ  ɴᴏᴛ  ᴀᴄᴄᴇᴘᴛ  ᴛʜᴇɴ   👇  👇''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT")