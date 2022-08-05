from bot import Bot
from pyrogram import Client
from presets import Presets
from suport.preload import get_dev_info
from humanize import naturalsize as size
from suport.support import get_chat, get_reply_markup
from plugins.commands import admin_user_id, generate_chat_link
from pyrogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

defaults = []

@Client.on_inline_query()
async def inline_search(c: Bot, query: InlineQuery):
    inline_results = []
    results = []
    #
    global defaults
    if not defaults:
        defaults = await get_dev_info()
    inline_results.extend(defaults)
    #
    if not admin_user_id:
        return
    elif admin_user_id and (query.from_user.id != admin_user_id[0]):
        await query.answer(results=inline_results, switch_pm_text=Presets.NOT_AUTH_TXT, switch_pm_parameter="okay")
        return
    else:
        pass
    #
    search = query.query.strip()
    results = await get_chat(c, search)
    #
    if results:
        for result in results:
            #
            file_name = result.document.file_name                                   # Name of the document
            file_size = size(result.document.file_size)                             # Size of the document
            chat_url = str(result.chat.id).replace("-100", "")                      # Chat id of the document
            chat_title = result.chat.title                                          # Title of the chat
            message_id = result.id                                                  # id of the message
            chat_id = result.chat.id                                                # Chat id of the message
            chat_username = result.chat.username if result.chat.username else None  # Username of the chat
            #
            inline_results.append(
                InlineQueryResultArticle(
                    title=Presets.INLINE_RESULT_TITLE.format(
                        file_name,
                        file_size
                    ),
                    input_message_content=InputTextMessageContent(
                        message_text=Presets.FILE_LINK_TXT.format(
                            file_name[:30],
                            file_size
                        )
                    ),
                    thumb_url=Presets.INLINE_THUMB_URL,
                    description=Presets.INLINE_DESCRIPTION.format(
                        file_size,
                        chat_title
                    ),
                    reply_markup=await get_reply_markup(
                        file_name,
                        file_size,
                        chat_url,
                        message_id,
                        await generate_chat_link(chat_username, chat_id),
                    )
                )
            ) 
    #
    if results:
        text = Presets.RESULTS_TXT.format(query.query)
        try:
            await query.answer(
                results=inline_results,
                switch_pm_text=text,
                switch_pm_parameter="start",
            )
        except Exception:
            pass
    else:
        text = Presets.NO_RESULTS.format(query.query)
        try:
            await query.answer(
                results=inline_results,
                switch_pm_text=text,
                switch_pm_parameter="okay",
            )
        except Exception:
            pass
