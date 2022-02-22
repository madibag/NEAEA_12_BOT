from config import Config
from datab import insert_into
from pypter import pyppter
import asyncio 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import json
import os


@Client.on_message(filters.command(["start"])& filters.private)
async def start(context,message):
	#print(message)
	chat_id = message.chat.id
	message_id = message.message_id

	await context.send_message(chat_id=chat_id,
						reply_to_message_id = message_id,
						text=Config.START_TEXT,
						reply_markup = InlineKeyboardMarkup(Config.START_BUTTON))


	#if update.message.entities:

@Client.on_message(filters.text& filters.private)
async def registration(context,message):

	chat_id = message.chat.id
	user_name = message.chat.username
	first_name = message.chat.first_name
	#sent_text = 

	reg_id = message.text

	if not (6 <= len(reg_id) <= 8):
		return

	try:
		int(reg_id)
	except:
		return
	#make procesing a stiker
	a = await context.send_sticker(chat_id=chat_id,
							sticker = Config.STICKER_ID)

	try:
		Json,pic = await pyppter(reg_id)

		print(0,type(Json))

		if Json["m"] == "NO Captcha":
			#raise Exception
			await context.delete_messages(chat_id=chat_id,message_ids=a.message_id)
			await context.send_message(chat_id=chat_id,
									text=Config.ERROR)
			return

		print(Json)

		caption = f"Name - {Json['s']['fn']}\n ______ Subjects ______ \n"
			
		for key,value in Json['m'].items():
			caption+=f"{key} - {value}\n"
		await context.delete_messages(chat_id=chat_id,message_ids=a.message_id)
		await context.send_photo(
			photo=pic,
			chat_id=chat_id,
			caption=caption+f"\n🧠By : : @{a.from_user.username}")
		os.remove(pic)

	except Exception as e:
		await context.delete_messages(chat_id=chat_id,message_ids=a.message_id)
		await context.send_message(chat_id=chat_id,
			text=Config.ERROR)
		return
		print(e)

	#Delete a stiker

	

	insert_into(first_name,chat_id,Json['s']['fn'],user_name,reg_id)


async def Contact(context,message):
	update.message.reply_text(Config.THE_DEV)



