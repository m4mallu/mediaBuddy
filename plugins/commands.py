from bot import Bot
from presets import Presets
from pyrogram import filters
from asyncio import sleep as slp
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from bot import bot_user_name as username
from suport.buttons import start_button, close_with_inline

# Let's define two global variables
final_chat_list = []        # Chat list of session user having media content only (Master list)
admin_user_id = []          # User id of admin to be shared


@Bot.on_message(filters.private & filters.command('start'))
async def start_bot(c: Bot, m: Message):
    await m.reply_text(
        Presets.WELCOME_TXT.format(m.from_user.first_name),
        reply_markup=start_button
    )


# ------------------------------ Index the total chats and media chats ----------------------------------------------- #
@Bot.on_message(filters.private & filters.command('index'))
async def index_media_chats(c: Bot, m: Message):
    """
    Bot need to fetch all the chat ids (groups & channels) to proceed the inline search from different chats.
    When the bot is deployed, user will send this command to bot as self and bot will respond to this command
    by fetching complete list of chat ids, and make a list of chat ids. From the above list bot will filter out
    the groups and channels list and later create a final list of chat ids of media contents. The bot will push two
    message to the user with the mentioned list of total groups and channels, and media contained chats. I CANNOT FIND
    ANY ALTERNATE WAY TO STORE THE CHAT IDS INITIALLY.
    """
    #
    chat_list = []          # A chat id list with user's groups and channels
    chat_names_A = []       # A mentioned name lts with the above chat ids
    chat_names_B = []       # A mentioned name list with the chats of having media only.
    detail_A = str()
    detail_B = str()
    chat = int()
    #
    await m.delete()
    # Check Admin
    try:
        chat = await c.USER.get_me()
    except FloodWait as e:
        await slp(e.x)
    #
    if m.from_user.id != int(chat.id):
        return
    #
    admin_user_id.append(chat.id)
    #
    # Let's find the chat ids (groups / channels) and create a primary list. Bot will message this list as mentioned.
    #
    msgA = await m.reply_text(Presets.FIND_ALL_CHATS_TXT)
    try:
        async for user_dialogs in c.USER.iter_dialogs():
            if not user_dialogs.chat.is_restricted:
                dialogues = user_dialogs.chat.id
                if str(dialogues).startswith('-100'):
                    chat_list.append(dialogues)
    except FloodWait as e:
        await slp(e.x)
    #
    # Let's create a mentioned chat titles from the chat ids filtered above
    #
    for chats in chat_list:
        try:
            detail_A = await c.USER.get_chat(chats)
            result = Presets.CHAT_LIST_TXT.format(detail_A.invite_link,
                                                  detail_A.title,
                                                  'SG' if detail_A.type == 'supergroup' else 'Ch')
            chat_names_A.append(result)
        except FloodWait as e:
            await slp(e.x)
    #
    # Let's output the complete chat list as a mentioned message.
    #
    await msgA.edit(
        Presets.CHAT_LIST_AUTO_1.format('\n'.join(map(str, chat_names_A))),
        disable_web_page_preview=True,
        reply_markup=start_button
    )
    """
    Let's find out the movie chats using a small trick. Every movie groups have a document file
    in their last 10 out of 25 messages. Through this way, we can filter out the exact chat ids
    from the entire list of chat ids. Here also bot will message the final list as mentioned.
    The list created will be shared globally for the inline searching of medias. 
    """
    msgB = await m.reply_text(Presets.FIND_MEDIA_CHATS_TXT)
    try:
        count = int()
        for chats in chat_list:
            async for user_messages in c.USER.iter_history(chat_id=chats, limit=25):
                if user_messages.document is not None:
                    count += 1
            if count >= 10:
                final_chat_list.append(chats)
            count = int()
    except FloodWait as e:
        await slp(e.x)
    #
    # Let's create a mentioned chat titles from the chat ids filtered above
    #
    for chats in final_chat_list:
        try:
            detail_B = await c.USER.get_chat(chats)
            result = Presets.CHAT_LIST_TXT.format(detail_B.invite_link,
                                                  detail_B.title,
                                                  'SG' if detail_B.type == 'supergroup' else 'Ch')
            chat_names_B.append(result)
        except FloodWait as e:
            await slp(e.x)
    #
    # Let's output the above final media contained chat list as a mentioned message.
    #
    await msgB.edit(
        Presets.CHAT_LIST_AUTO_2.format('\n'.join(map(str, chat_names_B)), str(username[0]).split("@")[1], 'start'),
        disable_web_page_preview=True,
        reply_markup=close_with_inline
    )


# ------------------------------------- Add a media chat to the master list ------------------------------------------ #
@Bot.on_message(filters.private & filters.command('update'))
async def update_media_chat(c: Bot, m: Message):
    if m.from_user.id != admin_user_id[0]:
        await m.delete()
        return
    msg = await m.reply_text(Presets.PROCESSING_TXT, reply_to_message_id=m.message_id)
    if (" " in m.text) and m.text.split(" ")[1].startswith("-100"):
        chat_id = m.text.split(" ")[1]
        if chat_id not in final_chat_list:
            try:
                chat = await c.USER.get_chat(chat_id)
            except Exception:
                await msg.edit(Presets.INVALID_CHAT_ID, reply_markup=close_with_inline)
                return
            final_chat_list.append(chat_id)
            await msg.edit(Presets.NEW_CHAT_CNF_TXT.format(chat.title,
                                                           "SuperGroup" if chat.type == "supergroup" else "Channel"))
        else:
            await msg.edit(Presets.CHAT_DUPLICATED_TXT, reply_markup=close_with_inline)
    else:
        await msg.edit(Presets.INVALID_UPDATE, reply_markup=close_with_inline)


# ------------------------------------ Delete a chat from the media chat list ---------------------------------------- #
@Bot.on_message(filters.private & filters.command('delete'))
async def remove_media_chat(c: Bot, m: Message):
    if m.from_user.id != admin_user_id[0]:
        await m.delete()
        return
    msg = await m.reply_text(Presets.PROCESSING_TXT, reply_to_message_id=m.message_id)
    if (" " in m.text) and m.text.split(" ")[1].startswith("-100"):
        chat_id = m.text.split(" ")[1]
        if chat_id in final_chat_list:
            final_chat_list.remove(chat_id)
            await msg.edit(Presets.CHAT_DELETE_TXT.format(chat_id), reply_markup=close_with_inline)
        else:
            await msg.edit(Presets.CHAT_NOT_EXIST_TXT.format(chat_id), reply_markup=close_with_inline)
    else:
        await msg.edit(Presets.INVALID_UPDATE, reply_markup=close_with_inline)


# ---------------------------------------- View the current media chats list------------------------------------------ #
@Bot.on_message(filters.private & filters.command('view'))
async def view_media_chat(c: Bot, m: Message):
    if m.from_user.id != admin_user_id[0]:
        await m.delete()
        return
    #
    detail_C = str()
    chat_names_C = []
    #
    msg = await m.reply_text(Presets.PROCESSING_TXT, reply_to_message_id=m.message_id)
    for chats in final_chat_list:
        try:
            detail_C = await c.USER.get_chat(chats)
            result = Presets.CHAT_LIST_TXT.format(detail_C.invite_link,
                                                  detail_C.title,
                                                  'SG' if detail_C.type == 'supergroup' else 'Ch')
            chat_names_C.append(result)
        except FloodWait as e:
            await slp(e.x)
        except Exception:
            pass
    #
    await msg.edit(
        Presets.CHAT_LIST_AUTO_2.format('\n'.join(map(str, chat_names_C)), str(username[0]).split("@")[1], 'start'),
        disable_web_page_preview=True,
        reply_markup=close_with_inline
    )
