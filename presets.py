class Presets(object):
    WELCOME_TXT = "<b>Hello.. {}</b>👋\n<i>I'm an inline media searching bot.\nJust search your medias inline. To " \
                  "know more about me, try</i> <b><u>HELP</u></b>"
    DEFAULT_TITLE = "mediaBuddy"
    DEFAULT_LINK = "https://github.com/m4mallu"
    DEFAULT_THUMB_URL = "https://image.flaticon.com/icons/png/512/25/25231.png"
    DEFAULT_DESCRIPTION = "Link: M4mallu | GitHub"
    DEV_TITLE = "Developer Information"
    DEV_LINK = "https://t.me/space4renjith"
    DEV_THUMB_URL = "https://freepikpsd.com/media/2019/10/software-developer-icon-png-2-Transparent-Images.png"
    DEV_DESCRIPTION = "Name: Renjith Mangal | Telegram"
    NOT_AUTH_TXT = "❌ ❌ You are not Authorized ❌ ❌"
    SHARE_BUTTON_TEXT = "Hi  👋\nCheckout : @{username}\nFor searching your medias inline"
    RESULTS_TXT = "👀 Results: for - {}"
    NO_RESULTS = "❌ No Results: for - {}"
    BOT_BLOCKED_MSG = "Bot is blocked by the  session user ! Open the bot chat, then try again."
    CHAT_LIST_TXT = "➡️ <a href='{}'><b>{}</b></a> - <b>{}</b>"
    PROCESSING_TXT = "<b>⚙️ Processing ⚙️</b>"
    INVALID_CHAT_ID = "<b>Error:</b>\n\n<i>You are not a member of the chat id provided</i>"
    NEW_CHAT_CNF_TXT = "<b>Success</b> ✅\n\n<i>New chat added to the master list.</i>\n\nName: {}\nType: {}"
    CHAT_DUPLICATED_TXT = "<b>Error:</b>\n\n<i>The chat is already in the master list. Update denied !</i>"
    INVALID_UPDATE = "<b>Error:</b>\n\n<i>Error in format. Try <b>HELP</b> for the command usage.</i>"
    FIND_ALL_CHATS_TXT = "<b>⚙️ Automated Message ⚙️</b>\n\n<code>Let's figure out the total groups and channels" \
                         " you have..</code>"
    FIND_MEDIA_CHATS_TXT = "<b>⚙️ Processing ⚙️</b>\n\n<code>Let's figure out the media chats from the above " \
                           "list..</code> "
    CHAT_DELETE_TXT = "<b>Success</b> ✅\n\n<i>Chat id <code>{}</code>\nHas been removed from the master list</i>"
    CHAT_NOT_EXIST_TXT = "<b>Error:</b>\n\n<i>Chat id: <code>{}</code>\nDoes not exists in the master list</i>"
    CHAT_LIST_AUTO_1 = "<b><u>Your current groups and channels:</u></b>\n\n{}"
    CHAT_LIST_AUTO_2 = "<b>Your current media chats:</b>\n\n{}\n\n<i>know more about me, click</i>" \
                       "<a href='t.me/{}?start={}'><b> 👉 HERE 👈</b></a>"
    FILE_LINK_TXT = "<b>Click on the file name:</b>\n\n<a href='https://t.me/c/{}/{}'><b>{}</b></a> | {}\n\n" \
                    "<b>Credits:</b><a href='https://github.com/m4mallu/mediaBuddy'><b> @M4Mallu</b></a>" \
                    "\xad    \xad||\xad    \xad<a href='t.me/{}?start={}'><b>HELP</b></a>"
    INLINE_THUMB_URL = "https://telegra.ph/file/6313edecd73bf2c38dd47.png"
    INLINE_DESCRIPTION = "| {} | {} |"
    HELP_HEADER_TXT = "<b>These are my available options:</b>"
    #
    HELP_ABOUT_TXT = "<b>I'm an inline media searching bot.</b>\n\n<i>If you need a particular movie from may of " \
                     "your movie channels, it will be a time consuming job to search it everywhere in the above" \
                     " channels.\n\nHere comes the demand for an inline media searching bot working within your " \
                     "dialogues and public chats.\n\nWhen this bot is deployed, it will search for the groups and " \
                     "channels within your dialogue and creates a list with chat ids of media contents. when you " \
                     "search a keyword inline, the bot will search the same inside the above and delivers a message" \
                     " as the movie name wth a hyper link to the file location. By clicking the same, you can easily " \
                     "access the file without wasting your valuable time.</i>\n\n" \
                     "<b>Credits:</b><a href='https://github.com/m4mallu/mediaBuddy'><b> @M4Mallu</b></a>"
    HELP_UPDATE_TXT = "<b>Add chat to the master list</b>\n\n<i>In some situations, when bot is failed to get some " \
                      "of your media chat ids, you can manually add them with a simple command like the below " \
                      "example.</i>\n\n<b>/update -100xxxxxxxxxx</b><i>\n\nWhere 'xxxxxxxxxx' is your media " \
                      "chat id. The same can be obtained by using any available chat id finding bots.\n\nNote: " \
                      "For private chats, session user need to be a member to add the chat to the maser list.</i>\n\n" \
                      "<b>Credits:</b><a href='https://github.com/m4mallu/mediaBuddy'><b> @M4Mallu</b></a>"
    HELP_DELETE_TXT = "<b>Delete chat from the master list</b>\n\n<i>If you are no longer a member of a chat and the " \
                      "chat id is present in your master list, you need to reindex the master list at this time. " \
                      "The same can be done by a running a simple command as mentioned below.</i>\n\n<b>/delete " \
                      "-100xxxxxxxxx</b>\n\n<i>Where 'xxxxxxxxx' is the chat id you want to remove from the list. " \
                      "The same can be obtained by using any available chat id finding bots.</i>\n\n" \
                      "<b>Credits:</b><a href='https://github.com/m4mallu/mediaBuddy'><b> @M4Mallu</b></a>"
    HELP_INDEX_TXT = "<b>Index your media chats</b>\n\n<i>When some cases like you have some media chats and indexed " \
                     "the same once, later you have left some chats and joined another. In this situation, you need " \
                     "to index your media chats manually by running the below command as a pm to the bot.</i>\n\n<b> " \
                     "/index</b>\n\n<i>When this command executed, bot will list the latest media chat ids and " \
                     "uses the same or searching your queries.</i><b><u>When you have joined or left from your media " \
                     "chats, you need to run this command once to update your master media chat id list for the " \
                     "smooth functioning of this bot.</u></b>\n\n" \
                     "<b>Credits:</b><a href='https://github.com/m4mallu/mediaBuddy'><b> @M4Mallu</b></a>"
    HELP_VIEW_TXT = "<b>View your media chats</b>\n\n<i>You can view your current configured media chat list using " \
                    "command.</i>\n\n<b>/view</b>\n\n<i>When this command is being executed, the bot will fetch all " \
                    "configured media chats and delivers a message with mentioned chat names.</i>\n\n" \
                    "<b>Credits:</b><a href='https://github.com/m4mallu/mediaBuddy'><b> @M4Mallu</b></a>"
