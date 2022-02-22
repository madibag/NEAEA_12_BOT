from pyrogram import Client, filters
from config import Config
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


@Client.on_callback_query(filters.regex('help_in_need'))
async def help(c,m):

    chat_id = m.from_user.id

    await c.send_message(
        chat_id=chat_id,
        text=Config.HELP,
        reply_markup=InlineKeyboardMarkup(Config.HELP_BUTTON)
        )

@Client.on_callback_query(filters.regex('Close'))
async def close(c,m):
    chat_id = m.from_user.id
    await c.delete_messages(chat_id=chat_id,message_ids=m.message.message_id)