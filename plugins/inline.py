from bot import Bot
from pyrogram import Client
from presets import Presets
from suport.support import get_chat
from suport.preload import get_info
from humanize import naturalsize as size
from bot import bot_user_name as username
from plugins.commands import admin_user_id
from suport.buttons import inline_result_markup
from pyrogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle


defaults = []

@Client.on_inline_query()
async def inline_search(c: Bot, iq: InlineQuery):
    results = []
    #
    if iq.from_user.id != admin_user_id[0]:
        return
    #
    global defaults
    if not defaults:
        defaults = await get_info()
    results.extend(defaults)
    #
    search = iq.query.strip()
    values = await get_chat(c, search)
    if values:
        for value in values:
            results.append(
                InlineQueryResultArticle(
                    title=value.document.file_name,
                    input_message_content=InputTextMessageContent(
                        message_text=Presets.FILE_LINK_TXT.format(
                            str(value.chat.id).replace("-100", ""),
                            value.message_id,
                            value.document.file_name,
                            size(value.document.file_size),
                            str(username[0]).split("@")[1],
                            'start'
                        )
                    ),
                    thumb_url=Presets.INLINE_THUMB_URL,
                    description=Presets.INLINE_DESCRIPTION.format(
                        size(value.document.file_size),
                        value.chat.title
                    ),
                    reply_markup=inline_result_markup,
                )
            )
    if values:
        switch_pm_text = Presets.RESULTS_TXT.format(iq.query)
        try:
            await iq.answer(
                results=results,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
    else:
        switch_pm_text = Presets.NO_RESULTS.format(iq.query)
        try:
            await iq.answer(
                results=results,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
