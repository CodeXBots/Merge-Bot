from datetime import datetime
from configs import Config
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TeamTeleRoid.database import db

@Client.on_message(filters.command("help") & filters.private)
async def help_handler(_, event: Message):
    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url=f'http://telegram.me/{Config.BOT_USERNAME}?startgroup=true')
            ],

             [InlineKeyboardButton("About", callback_data="About_msg"),
             InlineKeyboardButton("Help", callback_data="Help_msg")
             ]
        ])
    )                        

@Client.on_message(filters.command("total_users") & filters.private &  filters.chat(Config.BOT_OWNER))
async def total_users(_, event: Message):
    total_users = await db.total_users_count()
    msg = f"""
    Users: {total_users} users

    """
    await event.reply_text(msg)

@Client.on_message( filters.command("start") & filters.private)
async def start_handler(_,event: Message):
    await event.reply_photo(
        photo=Config.START_PHOTO,
        caption=Config.START_MSG.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton('➕     ᴀᴅᴅ  ᴍᴇ  ᴛᴏ  ʏᴏᴜʀ  ɢʀᴏᴜᴘ     ➕', url=f'http://telegram.me/{Config.BOT_USERNAME}?startgroup=true')
            ],
            [
            InlineKeyboardButton('⚚     ɱᴀɪɴ   ᴄʜᴀɴɴᴇʟ     ⚚', url='https://telegram.me/RahulReviewsYT')
            ],
            [
            InlineKeyboardButton('🔍   ꜱᴇᴀʀᴄʜ', url='https://youtube.com/@RahulReviews'),
            InlineKeyboardButton('📝   ᴀʙᴏᴜᴛ', callback_data="About_msg")
            ]
        ])
    )

VERIFY = {}
@Client.on_message(filters.command("request") & filters.group)
async def request_handler(c,m: Message):
    global VERIFY
    chat_id = m.chat.id
    user_id = m.from_user.id if m.from_user else None


    if VERIFY.get(str(chat_id)) == None: # Make Admin's ID List
        admin_list = []
        async for x in c.iter_chat_members(chat_id=chat_id, filter="administrators"):
            admin_id = x.user.id 
            admin_list.append(admin_id)
        admin_list.append(None)
        VERIFY[str(chat_id)] = admin_list

    if not user_id in VERIFY.get(str(chat_id)): # Checks if user is admin of the chat
        return

    group_id = m.chat.id
    group_info = await db.get_group(group_id)

    if not group_info["has_access"] or not await db.is_group_verified(group_id):
        REPLY_MARKUP = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('ʀᴇǫᴜᴇsᴛ ᴀᴄᴄᴇss', callback_data=f'request_access#{m.chat.id}#{m.from_user.id}'),
            ],

        ])

        return await m.reply_text(f"ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴍᴀʏ ɴᴏᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ ᴀᴅᴅ ʏᴏᴜʀ ᴏᴡɴ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴍᴀʏ ʜᴀᴠᴇ ᴇxᴘɪʀᴇᴅ. ᴘʟᴇᴀsᴇ ʀᴇǫᴜᴇsᴛ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ" ,reply_markup=REPLY_MARKUP ,disable_web_page_preview=True)

    else:
        return await m.reply_text("ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ /addb")


@Client.on_message(filters.command("addb") & filters.group)
async def addb_handler(c, m: Message):
    global VERIFY
    chat_id = m.chat.id
    user_id = m.from_user.id if m.from_user else None


    if VERIFY.get(str(chat_id)) == None: # Make Admin's ID List
        admin_list = []
        async for x in c.iter_chat_members(chat_id=chat_id, filter="administrators"):
            admin_id = x.user.id 
            admin_list.append(admin_id)
        admin_list.append(None)
        VERIFY[str(chat_id)] = admin_list

    if not user_id in VERIFY.get(str(chat_id)): # Checks if user is admin of the chat
        return

    group_id = m.chat.id
    group_info = await db.get_group(str(group_id))

    if group_info["has_access"] and await db.is_group_verified(group_id):
        if len(m.command) == 2:
            db_channel = m.command[1]


            try:
                invite_link =  await c.create_chat_invite_link(int(db_channel))
            except Exception as e:
                return await m.reply_text("ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴍᴀᴅᴇ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ "+str(db_channel))
                

            REPLY_MARKUP = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('ᴀʟʟᴏᴡ ᴅʙ ᴄʜᴀɴɴᴇʟ', callback_data=f'dbgive_access#{group_id}#{m.from_user.id}#{db_channel}'),
            InlineKeyboardButton('ᴅᴇɴʏ', callback_data=f'dbdeny_access#{m.from_user.id}#{db_channel}'),
        ],
        [
            
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data=f'delete'),
        ],

    ])      

            await c.send_message(Config.LOG_CHANNEL,  f"ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴀʟʟᴏᴡ. \n\n#NewDBChannel\n\nDB Chnl Invite Link: {invite_link.invite_link}\nGroup:`{group_id}`\n\nNote: ᴛʜɪs ɢʀᴏᴜᴘ ʜᴀs ʙᴇᴇɴ ᴀʟʀᴇᴀᴅʏ ʜᴀs ᴀᴄᴄᴇss", reply_markup=REPLY_MARKUP)
            return await m.reply_text("ᴅʙ ᴄʜᴀɴɴᴇʟ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ. ᴡᴀɪᴛ ꜰᴏʀ ᴛʜᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ. ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪꜰɪᴇᴅ", )
        else:
            return await m.reply_text("ᴍᴀᴋᴇ ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ /addb -100xxx")
    else:
        return await m.reply_text("ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ᴘʟᴇᴀsᴇ /request ᴀᴄᴄᴇss")