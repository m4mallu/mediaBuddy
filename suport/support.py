from asyncio import sleep
from pyrogram import enums
from presets import Presets
from pyrogram.errors import FloodWait
from plugins.commands import final_chat_list as channels
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

doc = enums.MessagesFilter.DOCUMENT
filter_docs = ('.mp4', '.mkv', '.avi', '.webp')

""" Let's search the messages with the chat id list  and create an output list. The chat ids will be obtained from
    the master list shared globally from the "index" command """
async def get_chat(client, search):
    #
    count = int()
    results = []
    #
    for channel in channels:
        try:
            async for user_messages in client.USER.search_messages(channel, search, filter=doc, limit=20):
                messages = await client.USER.get_messages(channel, user_messages.id, replies=0)
                if str(messages.document.file_name).lower().endswith(filter_docs):
                    results.append(messages)
                    count += 1
            if count >= 20:
                count = int()
                break
        except FloodWait as e:
            await sleep(e.value)
        except Exception:
            pass
    return results


""" Generate a reply markup for the inline results """
async def get_reply_markup(file_name, size, chat_link, message_link, chat_invite_link):
    """ Create a reply markup for the inline results """
    inline_result_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=file_name[:25] + " || " + size, url=Presets.INLINE_RESULT_MARKUP.format(
                    chat_link, message_link))
            ],
            [
                await gen_chat_invite_btn(chat_invite_link),
                InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat=str())
            ]
        ]
    )
    return inline_result_markup


"""Generate InlineKeyboardButton pattern to share chat invite link"""
async def gen_chat_invite_btn(chat_invite_link):
    if str(chat_invite_link) == "no_chat_invite_link":
        return InlineKeyboardButton('🔰 Chat Link', callback_data='empty_chat_invite_link')
    else:
        return InlineKeyboardButton('🔰 Chat Link', url=f'{chat_invite_link}')
