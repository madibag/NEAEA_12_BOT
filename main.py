from pyrogram import Client
import asyncio
from config import Config


app = Client(
	"Grade12",
	bot_token=Config.TOKEN,
	api_id=Config.API_ID,
	api_hash=Config.API_HASH,
	plugins=dict(root="plugins")
	)

app.run()



