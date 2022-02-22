import os
from pyrogram.types import InlineKeyboardButton

class Config(object):
	"""docstring for Config"""

	TOKEN = os.environ.get("TOKEN","")
	
	MONGODB = os.environ.get("MONGODB","")

	API_ID = int(os.environ.get("API_ID",""))

	API_HASH = os.environ.get("API_HASH","")




	ERROR = "An Errror Occured Please try again"

	START_TEXT = "ሰላም ይህ የ12ኛ ክፍል ውጤት Bot ነው።\nHi This is Grade12 Result Bot"

	ERROR_INVALID = "Invalid Registration ID"

	START_BUTTON = [[InlineKeyboardButton(text="⚙️ Developer ⚙️",url="https://t.me/Nahom_d54"),InlineKeyboardButton(text="ℹ️ Source Code",url="https://t.me/notGonnahappenman")],
		[InlineKeyboardButton(text="🆘 Help",callback_data="help_in_need"),InlineKeyboardButton(text="🗑 Close",callback_data="Close")]]

	HELP = "ፒስ ነው ብራዘር \nውጤት ለማወቅ ዝም ብለህ Registration number መላክ ነው::\nJust Send Your Registration Number."

	HELP_BUTTON = [[InlineKeyboardButton(text="⚙️ Developer ⚙️",url="https://t.me/Nahom_d54"),InlineKeyboardButton(text="ℹ️ Source Code",url="https://t.me/notGonnahappenman")],
		[InlineKeyboardButton(text="🗑 Close",callback_data="Close")]]


	STICKER_ID = "CAACAgQAAxkBAAIsCGIUxCB7W2E21X-jfMmpPus2HhDmAAJPCwACGtCpUIrVnFss_RXPIwQ"
