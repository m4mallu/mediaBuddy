from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
    [
        InlineKeyboardButton("🛡 Support Chat", url="t.me/rmprojects"),
        InlineKeyboardButton("🎯 Source", url="https://github.com/m4mallu")
    ],
    [
        InlineKeyboardButton("❌ Close", callback_data="close_btn"),
        InlineKeyboardButton("Help", callback_data="help_btn"),
        InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
    ]
    ]

close_inline = [
               [
                    InlineKeyboardButton("❌ Close", callback_data="close_btn"),
                    InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
               ]
               ]

result = [
         [
                InlineKeyboardButton("🎯 Source", url="https://github.com/m4mallu"),
                InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
         ]
         ]

setup = [
        [
            InlineKeyboardButton("❓ About", callback_data="about_btn"),
            InlineKeyboardButton("🌐 Index Chats", callback_data="index_btn")
        ],
        [
            InlineKeyboardButton("📑 Update Chats", callback_data="update_btn"),
            InlineKeyboardButton("⛔ Delete Chats", callback_data="delete_btn")
        ],
        [
            InlineKeyboardButton("🔍 View Chats", callback_data="view_btn"),
            InlineKeyboardButton("⬅️ Back", callback_data="start_btn")
        ]
        ]

back_close = [
             [
                 InlineKeyboardButton("Close", callback_data="close_btn"),
                 InlineKeyboardButton("⬅️ Back", callback_data="back_btn")
             ]
             ]

help_button = InlineKeyboardMarkup(setup)
start_button = InlineKeyboardMarkup(start)
back_button = InlineKeyboardMarkup(back_close)
inline_result_markup = InlineKeyboardMarkup(result)
close_with_inline = InlineKeyboardMarkup(close_inline)
