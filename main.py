from pyrogram import Client,idle
import asyncio
from config import Config
from pyppeteer import launch
from pypter import brows

app = Client(
	"Grade12",
	bot_token=Config.TOKEN,
	api_id=Config.API_ID,
	api_hash=Config.API_HASH,
	plugins=dict(root="plugins")
	)


async def main_a():
	await app.start()

	browser = await brows()

	await idle()

	
app.run(main_a())


