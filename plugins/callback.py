from bot import Bot
from pyrogram import filters
from presets import Presets
from pyrogram.types import CallbackQuery
from suport.buttons import help_button, back_button, start_button


@Bot.on_callback_query(filters.regex(r'^start_btn$'))
async def help_start_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.WELCOME_TXT.format(cb.from_user.first_name), reply_markup=start_button)


@Bot.on_callback_query(filters.regex(r'^close_btn$'))
async def close_button(c: Bot, cb: CallbackQuery):
    await cb.message.delete()


@Bot.on_callback_query(filters.regex(r'^back_btn$'))
async def help_back_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_HEADER_TXT, reply_markup=help_button)


@Bot.on_callback_query(filters.regex(r'^help_btn$'))
async def help_text_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_HEADER_TXT, reply_markup=help_button)


@Bot.on_callback_query(filters.regex(r'^about_btn$'))
async def help_about_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_ABOUT_TXT, reply_markup=back_button, disable_web_page_preview=True)


@Bot.on_callback_query(filters.regex(r'^index_btn$'))
async def help_index_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_INDEX_TXT, reply_markup=back_button, disable_web_page_preview=True)


@Bot.on_callback_query(filters.regex(r'^update_btn$'))
async def help_update_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_UPDATE_TXT, reply_markup=back_button, disable_web_page_preview=True)


@Bot.on_callback_query(filters.regex(r'^delete_btn$'))
async def help_delete_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_DELETE_TXT, reply_markup=back_button, disable_web_page_preview=True)


@Bot.on_callback_query(filters.regex(r'^view_btn$'))
async def help_view_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_VIEW_TXT, reply_markup=back_button, disable_web_page_preview=True)
