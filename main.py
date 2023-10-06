from os import link
from telethon import Button
from configs import Config
from pyrogram import Client, idle
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from plugins.tgraph import *
from helpers import *
from telethon import TelegramClient, events
import urllib.parse
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
import re
tbot = TelegramClient('mdisktelethonbot', Config.API_ID, Config.API_HASH).start(bot_token=Config.BOT_TOKEN)
client = TelegramClient(StringSession( Config.USER_SESSION_STRING), Config.API_ID, Config.API_HASH)


async def get_user_join(id):
    if Config.FORCE_SUB == "False":
        return True

    ok = True
    try:
        await tbot(GetParticipantRequest(channel=int(Config.UPDATES_CHANNEL), participant=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok


@tbot.on(events.NewMessage(incoming=True))
async def message_handler(event):
    try:
        if event.message.post:
            return

        # if event.is_channel:return
        if event.text.startswith("/"):return

        print("\n")
        print("Message Received: " + event.text)

        # Force Subscription
        if  not await get_user_join(event.sender_id):
            haha = await event.reply(f'''**𝑱𝒐𝒊𝒏  𝑶𝒖𝒓  𝑼𝒑𝒅𝒂𝒕𝒆  𝑪𝒉𝒂𝒏𝒏𝒆𝒍  𝑻𝒐  𝑼𝒔𝒆  𝑻𝒉𝒊𝒔  𝑩𝒐𝒕  😊**''', buttons=Button.url(' 🔥  𝚄𝙿𝙳𝙰𝚃𝙴  𝙲𝙷𝙰𝙽𝙽𝙴𝙻  🔥 ', f'https://t.me/{Config.UPDATES_CHANNEL_USERNAME}'))
            await asyncio.sleep(Config.AUTO_DELETE_TIME)
            return await haha.delete()

        args = event.text
        args = await validate_q(args)

        print("Search Query: {args}".format(args=args))
        print("\n")

        if not args:
            return

        txt = await event.reply('**ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ "{}" 🔍**'.format(event.text))



        search = []
        if event.is_group or event.is_channel:
            group_info = await db.get_group(str(event.chat_id).replace("-100", ""))

            if group_info["has_access"] and group_info["db_channel"] and await db.is_group_verified(str(event.chat_id).replace("-100", "")):
                CHANNEL_ID = group_info["db_channel"]
            else:
                CHANNEL_ID = Config.CHANNEL_ID
        else:
            CHANNEL_ID = Config.CHANNEL_ID


        async for i in AsyncIter(re.sub("__|\*", "", args).split()):
            if len(i) > 2:
               
                search_msg = client.iter_messages(CHANNEL_ID, limit=5, search=i)
                search.append(search_msg)

        username = Config.UPDATES_CHANNEL_USERNAME
        answer = f'**Join** [@{username}](https://telegram.me/{username}) \n\n'

        c = 0

        async for msg_list in AsyncIter(search):
            async for msg in msg_list:
                c += 1
                f_text = re.sub("__|\*", "", msg.text)

                f_text = await link_to_hyperlink(f_text)
                answer += f'\n\n𝙿𝙰𝙶𝙴 {c} ✅\n\n' + '' + f_text.split("\n", 1)[0] + '' + '\n\n' + '' + f_text.split("\n", 2)[-1] + "\n\n"
                
            # break
        finalsearch = []
        async for msg in AsyncIter(search):
            finalsearch.append(msg)

        if c <= 0:
            answer = f'''𝚃𝙷𝙸𝚂  𝙼𝙾𝚅𝙸𝙴  𝙸𝚂  𝙽𝙾𝚃  𝚈𝙴𝚃  𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳  𝙾𝚁  𝙰𝙳𝙳𝙴𝙳  𝚃𝙾  𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴.'''

            newbutton = [Button.url('ʀᴇǫᴜᴇꜱᴛ  ᴛᴏ  ᴏᴡɴᴇʀ  ❣️',
                                    f'https://telegram.me/nancyji_bot')]
            await txt.delete()
            result = await event.reply(answer, buttons=newbutton, link_preview=False)
            await asyncio.sleep(Config.AUTO_DELETE_TIME)
            await event.delete()
            return await result.delete()
        else:
            pass

        answer += f"\n\n**Uploaded By @{Config.UPDATES_CHANNEL_USERNAME}**"
        answer = await replace_username(answer)
        html_content = await markdown_to_html(answer)
        html_content = await make_bold(html_content)
        
        tgraph_result = await telegraph_handler(
            html=html_content,
            title=event.text,
            author=Config.BOT_USERNAME
        )
        message = f'**ᴄʟɪᴄᴋ  ʜᴇʀᴇ 👇**\n\n[📽️ {str(event.text).upper()}\n🔎 {str("Click me for results").upper()}]({tgraph_result})'
        await txt.delete()
        result = await event.reply(message, link_preview=False)
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        # await event.delete()
        return await result.delete()

    except Exception as e:
        print(e)
        await txt.delete()
        result = await event.reply("𝚃𝙷𝙸𝚂  𝙼𝙾𝚅𝙸𝙴  𝙸𝚂  𝙽𝙾𝚃  𝚈𝙴𝚃  𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳  𝙾𝚁  𝙰𝙳𝙳𝙴𝙳  𝚃𝙾  𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴.")
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete() 
        return await result.delete()


async def escape_url(str):
    escape_url = urllib.parse.quote(str)
    return escape_url


# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

print()
print("-------------------- Initializing Telegram Bot --------------------")
# Start Clients
Bot.start()

print("------------------------------------------------------------------")
print()
print(f"""
 _____________________________________________   
|                                             |  
|          Deployed Successfully              |  
|              Join @MovieVillaYT               |
|_____________________________________________|
    """)

with tbot, client:
    tbot.run_until_disconnected()
    client.run_until_disconnected()

# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
print()
print("------------------------ Stopped Services ------------------------")
Bot.stop()
