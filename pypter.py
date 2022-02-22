from pyppeteer import launch
import asyncio
import time
import json


the_response = ''

async def intercept_on(response):
	#print(response.url)

	global the_response

	if response.url == 'http://result.neaea.gov.et/Home/result':
		print(response.url)

		the_response = await response.json()


async def pyppter(regId):
	browser = await launch(headless=True)

	page = await browser.newPage()

	page.on('response', lambda response: asyncio.ensure_future(intercept_on(response)))

	#two thinings in one stone
	#https://maxiee.github.io/post/PyppeteerCrawlingInterceptResponsemd/

	await page.goto('http://result.neaea.gov.et/',{'waitUntil' : ['domcontentloaded','networkidle0']})

	time.sleep(2)

	await page.type("#Registration_Number",regId)

	await page.click('form button[type=submit]')


	#getCaptcha = await page.evaluate('document.querySelector("#captcha").value', force_expr=True)
	#getverTok = await page.evaluate('document.getElementsByName("__RequestVerificationToken")[0].value', force_expr=True)

	await page.screenshot({'path': f'{regId}.png', 'fullPage': True})

	#print("Here =>",the_response)

	#await page.evaluate("""
	#			var xhr = new XMLHttpRequest();
	#			xhr.open("POST", 'http://result.neaea.gov.et/Home/result', true);
	#			xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	#			xhr.send("Registration_Number={}&__RequestVerificationToken={}&captcha={}");
	#							""".format(regId,getverTok,getCaptcha),force_expr=True)
	time.sleep(1)

	#vll = await page.evaluate('xhr.response', force_expr=True)



	#element = await page.content()

	#print(vll)


	await browser.close()
	

	return the_response,f'{regId}.png'

