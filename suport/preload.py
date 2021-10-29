from presets import Presets
from suport.buttons import inline_result_markup
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


async def get_info():
    result = []
    set1 = InlineQueryResultArticle(
        title=Presets.DEFAULT_TITLE,
        input_message_content=InputTextMessageContent(
            message_text=Presets.DEFAULT_LINK
        ),
        thumb_url=Presets.DEFAULT_THUMB_URL,
        description=Presets.DEFAULT_DESCRIPTION,
        reply_markup=inline_result_markup
    )
    set2 = InlineQueryResultArticle(
        title=Presets.DEV_TITLE,
        input_message_content=InputTextMessageContent(
            message_text=Presets.DEV_LINK
        ),
        thumb_url=Presets.DEV_THUMB_URL,
        description=Presets.DEV_DESCRIPTION,
        reply_markup=inline_result_markup
    )
    result.extend([set1, set2])
    return result
