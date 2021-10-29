from asyncio import sleep as slp
from pyrogram.errors import FloodWait
from plugins.commands import final_chat_list as channels


async def get_chat(client, search):
    """
    Let's search the messages with the chat id list  and create an output list.
    The chat ids will be obtained from the master list shared globally from the "index" command
    """
    count = int()
    results = []
    filter_docs = ('.mp4', '.mkv', '.avi', '.webp')
    #
    for channel in channels:
        try:
            async for user_messages in client.USER.search_messages(channel, search, filter='document', limit=20):
                messages = await client.USER.get_messages(channel, user_messages.message_id, replies=0)
                if str(messages.document.file_name).lower().endswith(filter_docs):
                    results.append(messages)
                    count += 1
            if count >= 20:
                count = int()
                break
        except FloodWait as e:
            await slp(e.x)
        except Exception:
            pass
    return results
