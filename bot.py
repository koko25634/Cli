# UPDATED UPTO 14/05/2021 9:03 AM

import sys
import json
import requests
import re
from bs4 import BeautifulSoup
from os import system, remove
from time import sleep
from colorama import init
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.sync import TelegramClient, events
import os
from urllib.request import urlopen
import time
from telethon import functions, types
import browser_cookie3
import webbrowser
import subprocess
import traceback

init(convert=True)

api_id = "2429918"
api_hash = "7676a671ed69de73011d6bf3c9ffac64"
chrome = "chromedriver.exe"

ref = [
	"DGC : https://t.me/Dogecoin_click_bot?start=",
	"LTC : https://t.me/Litecoin_click_bot?start=",
	"BCH : https://t.me/BCH_clickbot?start=",
	"ZEC : https://t.me/Zcash_click_bot?start=",
	"BTC : https://t.me/BitcoinClick_bot?start="
]

bot_ids = [
	715510199, "@Litecoin_click_bot",
	"@BCH_clickbot", "@Zcash_click_bot", "@BitcoinClick_bot"
]

bot_ids2 = [
	"@Dogecoin_click_bot", "@Litecoin_click_bot",
	"@BCH_clickbot", "@Zcash_click_bot", "@BitcoinClick_bot"
]
bot_tag = ['DGC', "LTC", "BCH", "ZEC", "BTC"]

press = '\x1b[1;34;40m' + "Press enter to back to the menu" + '\x1b[0m'
print(
	5*"\n", '\x1b[1;31;40m',
	"""
		█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   █▀▄ █▀▀ █   ▀█▀ ▄▀█   █▀▀ █▀█ █▀█ █ █ █▀█
		█▄▄ █▀▄ ██▄ █▀█  █  ██▄ █▄▀   █▄█  █    █▄▀ ██▄ █▄▄  █  █▀█   █▄█ █▀▄ █▄█ █▄█ █▀▀

									Tᴇʟᴇɢʀᴀᴍ: @ᴅᴇʟᴛᴀ_ʙᴄᴄ
	""",
	'\x1b[0m',
	5*"\n"
)
for x in range(0, 4):
	b = "Loading" + "." * x
	print(b, end="\r")
	sleep(0.5)

earned = []
acc_b = []
tasks = [0]
ex = ['🤣 😂 Funny Jokes Memes Comedy Videos','Telethon Chat', 'telethon offtopic','Rayez ID','Updatesc','Otp sakti']
cg = []

header = {"User-Agent":	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}

# os.chdir(os.path.dirname(__file__))
# with open ('cookie.txt') as f:
# 	# global id
# 	# global clearance
# 	x = f.read()
# 	y = x.split('; ')
# 	for i in y:
# 		# print (i)
# 		a = i.split('=')
# 		if a[0] == '__cfduid':
# 			id = a[1]
# 		elif a[0] == 'cf_clearance':
# 			clearance = a[1]
			



# cookies_jar = requests.cookies.RequestsCookieJar()
# # cookies_jar.set('cf_chl_2', 'fb09ac28863c231', domain='doge.click', path='/')
# # cookies_jar.set('cf_chl_prog', 'a10', domain='doge.click', path='/')
# cookies_jar.set('cf_clearance', clearance, domain='doge.click', path='/')

# -------------BRAVE BROWSER----------------------------------------------------------
# chromecookies = r"C:\\Users\\PRASHANT\AppData\\Local\BraveSoftware\Brave-Browser\\User Data\Default\\Cookies"
# chromecookies = r"C:\\Users\\PRASHANT\AppData\\Roaming\brave\\Cookies"

# ------------------CHROMIUM BROWSER---------------------------------------------------------------------

def cookie_maker():
	#chromecookies = r"/.config/chromium/Default/Cookies"
	# firefoxcookies = r"/.mozilla/firefox/ivhxz967.default/cookies.sqlite"
	browser1 = browser_cookie3.firefox(domain_name='doge.click')
	cookies_jar = []
	cookies_jar.clear()
	cookies_jar.append(browser1)

	cookies_jar2 = requests.cookies.RequestsCookieJar()
	for cookie in cookies_jar[0]:
		a = str(cookie)
		b = a.split(" ")
		c = b[1].split("=")
		if c[0] == 'cf_clearance':
			cookies_jar2.set('cf_clearance', c[1], domain='.doge.click', path='/')
	print(cookies_jar2)
	return cookies_jar2

# cookies_jar2 = requests.cookies.RequestsCookieJar()
# cookies_jar2.set('cf_clearance', '54645', domain='.doge.click', path='/')

def browser_open():
	try:
		#path = r'/usr/bin/chromium-browser --no-sandbox --disable-dev-shm-usage https://doge.click/vc/abc'
		path = r'firefox https://doge.click/vc/abc'
		p = subprocess.Popen([path], shell=True)
		sleep(30)
		p1 = subprocess.Popen([path], shell=True)
		sleep(30)
		os.system('pkill firefox')
	except Exception as e:
		traceback.print_exc()


def did():
	n = tasks[0] + 1
	tasks.clear()
	tasks.append(n)


def counter(tag):
	try:
		j = 0
		for i in earned:
			i = i.split("You earned ", 1)[1]
			if 'DOGE' in i:
				i = i.split(" DOGE")[0]
			else:
				sp = " " + tag
				i = i.split(sp)[0]
			i = float(i)
			j += i
		j = "{:.8f}".format(float(j))
		earned.clear()
		print('\x1b[1;32;40m', "You earned ", j,
			  tag, " From tasks today", '\x1b[0m')
		j = 0
	except:
		pass
	for i in acc_b:
		i = float(i)
		j += i
	j = "{:.8f}".format(float(j))
	print("\n", '\x1b[1;32;40m', "All money :", j, tag, '\x1b[0m', "\n")
	acc_b.clear()



def countdown(t):
	while (t):
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(f"\033[1;30m#\033[1;32mPlease stay on the site for at least {timer} \033[1;32m seconds... ", end="\r")
		time.sleep(1)
		t -= 1
	print("\n")

def send(number, bot_id, tag, wallet, choose):
	session = "session//" + number
	if not os.path.exists("session"):
		os.mkdir("session")

	skip_bot = ['n']
	print('\x1b[1;36;40m' + "starting on " + number + '\x1b[0m')
	try:
		client = TelegramClient(session, api_id, api_hash)
		client.connect()
		client.sign_in(session)
		# client.start(session)
		if not client.is_user_authorized:
			print("Code Required")
			sys.exit("Code Required")


# ------------VISIT CODE START-------------------------------------------------------------------
		async def visit(bot_id):
			await client.send_message(bot_id, '/cancel')
			sleep(1)
			while True:
				await client.send_message(bot_id, '/visit')
				sleep(2)
				messages = await client.get_messages(bot_id)
				if 'In order to use this bot' in messages[0].message:
					url2 = messages[0].reply_markup.rows[0].buttons[0].url
					# await hello[0].click(0,0)
					r = requests.get(url2)
					await messages[0].click(1,0)
					await client.send_message(bot_ids[0], '/settings')
					print('\x1b[1;32;40m' + "Allowing NSFW....." + '\x1b[0m')
					sleep(1)
					messages = await client.get_messages(bot_ids[0])
					if 'Choose a setting' in messages[0].message:
						# print(event.raw_text)
						await messages[0].click(0)
					sleep(1)
					response = await client.get_messages(bot_ids[0])
					if 'disabled' in response[0].message:
						await response[0].click(0)
					else:
						pass
				if 'no longer valid' in messages[0].message:
					if '/visit' in messages[0].message:
						print('\x1b[1;31;40m' + "Sorry, that task is no longer valid, skipping..." + '\x1b[0m')
						await client.send_message(bot_id, '/visit')
					else:
						pass
				elif 'In the past hour, you earned' in messages[0].message:
					await client.send_message(bot_id, '/visit')
				elif 'no new ads available' in messages[0].message:
					print('\x1b[0;33;40m' + messages[0].message + '\x1b[0m')
					break
				try:
					url = messages[0].reply_markup.rows[0].buttons[0].url
					print('\x1b[1;37;40m' +'------------------------------[ visit ]' + '\x1b[0m')

					
					# r = requests.get(url, headers=header, cookies=cookies_jar)
					# print(cookies_maker())
					try:
						r = requests.get(url, headers=header, cookies=cookie_maker())
						if (r.status_code <= 204):
							soup = BeautifulSoup(r.content, "html.parser")
							captcha = soup.find('div', {'class': 'g-recaptcha'})
							if captcha is not None:
								print('\x1b[1;36;40m' +
									  'Captcha detected! Skipping ads...\n' + '\x1b[0m')
								messages = await client.get_messages(bot_id)
								await messages[0].click(2)
							else:
								for div in soup.find_all('div', id="headbar"):
									timer = int(div['data-timer'])
									try:
										if soup.find("div", id="headbar") is not None:
											for dat in soup.find_all("div", class_="container-fluid"):
												code = dat.get("data-code")
												timer = dat.get("data-timer")
												tokena = dat.get("data-token")
												countdown(int(timer))
												r = requests.post(
													"https://dogeclick.com/reward",
													data={"code": code, "token": tokena},
													headers=header,
													timeout=15,
													allow_redirects=True,
												)

									except Exception as e:
										print(e)
										messages = await client.get_messages(bot_id)
										# await messages[0].click(2)
										print('\x1b[3;37;40m' + "Invalid link skipping" + '\x1b[0m')
						else:
							messages = await client.get_messages(bot_id)
							# await messages[0].click(2)
							print('\x1b[1;31;40m' + "Skipping... CloudFlare System" + '\x1b[0m')
							sleep(1)

							browser_open()
							# cookies_jar.clear()
							# browser2 = browser_cookie3.chrome(cookie_file=chromecookies, domain_name='.doge.click')
							# cookies_jar.append(browser2)
							# # for cookie in cookies_jar:
							# # 	a = str(cookie)
							# 	b = a.split(" ")
							# 	c = b[1].split("=")
							# 	if c[0] == 'cf_clearance':
							# 		cookies_jar2.update(c[1])
					except requests.exceptions.TooManyRedirects:
						traceback.print_exc()
						await messages[0].click(2)
					except AttributeError:
						traceback.print_exc()
						browser_open()
					except browser_cookie3.BrowserCookieError or ValueError:
						traceback.print_exc()
						os.system('rm -rf /.config/chromium/Default/Cookies')
						browser_open()
					except Exception:
						traceback.print_exc()

				except:
					pass
				messages2 = await client.get_messages(bot_id, limit=2)
				if 'Please stay on the site' in messages2[0].message:
					x = messages2[0].message.split("Please stay on the site for at least ")
					y = x[1].split(" seconds...")
					countdown(int(y[0]))
					messages3 = await client.get_messages(bot_id, limit=2)
					if "You earned" in messages3[1].message:
						print('\x1b[1;33;40m' + "3:-" +messages3[1].message + '\x1b[0m')
						earned.append(messages3[1].message)
						did()
					else:
						print('\x1b[1;33;40m' + "3:-" +messages3[0].message + '\x1b[0m')
						earned.append(messages3[0].message)
						did()


				elif "You earned" in messages2[0].message:
					print('\x1b[1;33;40m' + "2:-" +messages2[0].message + '\x1b[0m')
					earned.append(messages2[0].message)
					did()

		with client:
			client.loop.run_until_complete(visit(bot_id))
# ------------VISIT CODE END-------------------------------------------------------------------




# -----------MESSAGE CODE START--------------------------------------------------------------------------------

		async def message(bot_id):
			while True:
				await client.send_message(bot_id, '/bots')
				sleep(2)
				messages = await client.get_messages(bot_id)
				if 'no longer valid' in messages[0].message:
					if '/visit' in messages[0].message:
						print('\x1b[1;31;40m' + "Sorry, that task is no longer valid, skipping..." + '\x1b[0m')
						await client.send_message(bot_id, '/visit')
					else:
						pass
				elif 'You must stay' in messages[0].message:
					print('\x1b[1;33;40m' + messages[0].message + '\x1b[0m')
					did()
				elif 'In the past hour, you earned' in messages[0].message:
					await client.send_message(bot_id, '/visit')
			
				elif 'no new ads available' in messages[0].message:
					print('\x1b[0;33;40m' + messages[0].message + '\x1b[0m')
					break
				try:
					url = messages[0].reply_markup.rows[0].buttons[0].url
					print("\n", '\x1b[1;37;40m' + "----------------------------[ msg bot ]" + '\x1b[0m')
					try:
						r = requests.get(url, headers=header, cookies=cookie_maker())
						if skip_bot[0] == "skip":
							skip_bot.clear()
							skip_bot.append('n')
							print('\x1b[2;34;40m' + "bot not respond skipping" + '\x1b[0m')
							messages = await client.get_messages(bot_id)
							await messages[0].click(2)
						elif (r.status_code <= 204):
							soup = BeautifulSoup(r.content, "html.parser")
							captcha = soup.find('div', {'class': 'g-recaptcha'})
							if captcha is not None:
								print('\x1b[1;36;40m' + 'Captcha detected! Skipping ads...\n' + '\x1b[0m')
								messages = await client.get_messages(bot_id)
								await messages[0].click(2)
							else:
								for link in soup.findAll('meta', attrs={'content': re.compile("https://t.me/")}):
									J = str(link.get('content')).replace("https://t.me/", "@")
								try:
									await client.send_message(J, '/start')
								except:
									print('bot not found ......')
									skip_bot.clear()
									skip_bot.append('skip')
								sleep(4)
								try:
									messages = await client.get_messages(J)
									if messages[0].message == '/start':
										print('\x1b[2;34;40m' + "bot not respond" + '\x1b[0m')
										messages = await client.get_messages(bot_id)
										await messages[0].click(2)
										print('\x1b[2;34;40m' + "Skipping..." + '\x1b[0m')
									else:
										await client.forward_messages(bot_id, messages[0], J)
										sleep(2)
								except:
									print('\x1b[2;34;40m' + "bot not respond" + '\x1b[0m')
									messages = await client.get_messages(bot_id)
									await messages[0].click(2)
									print('\x1b[2;34;40m' + "Skipping..." + '\x1b[0m')
						else:
							messages = await client.get_messages(bot_id)
							# await messages[0].click(2)
							print('\x1b[1;31;40m' + "Skipping... CloudFlare System" + '\x1b[0m')
							sleep(1)
							browser_open()
					except requests.exceptions.TooManyRedirects:
						traceback.print_exc()
						await messages[0].click(2)
					except AttributeError:
						traceback.print_exc()
						browser_open()
					except browser_cookie3.BrowserCookieError or ValueError:
						traceback.print_exc()
						os.system('rm -rf /.config/chromium/Default/Cookies')
						browser_open()
					except Exception:
						traceback.print_exc()
				except:
					pass
				messages1 = await client.get_messages(bot_id, limit=2)
				if "You earned" in messages1[1].message:
					print('\x1b[1;33;40m' + messages1[1].message + '\x1b[0m')
					earned.append(messages1[1].message)
					did()
				
		with client:
			client.loop.run_until_complete(message(bot_id))


# -----------MESSAGE CODE END--------------------------------------------------------------------------------




# -----------JOIN CHANNEL CODE START--------------------------------------------------------------------------------

		async def join():
			while True:
				await client.send_message(bot_id, '/join')
				sleep(2)
				messages = await client.get_messages(bot_id)
				try:
					url = messages[0].reply_markup.rows[0].buttons[0].url
					print("\n", '\x1b[1;37;40m' + "-------------------------------[ join ]" + '\x1b[0m')
					try:
						r = requests.get(url, headers=header, cookies=cookie_maker())
						if skip_bot[0] == "skip":
							skip_bot.clear()
							skip_bot.append('n')
							print('\x1b[2;34;40m' + "Error: Group or channel not found skipping..." + '\x1b[0m')
							await client.send_message(bot_id, '/join')
							sleep(1.5)
							messages = await client.get_messages(bot_id)
							await messages[0].click(3)
						elif (r.status_code <= 204):
							messages = await client.get_messages(bot_id)
							soup = BeautifulSoup(r.content, "html.parser")
							for link in soup.findAll('meta', attrs={'content': re.compile("https://t.me/")}):
								J = str(link.get('content')).replace("https://t.me/", "@")
							try:
								await client(JoinChannelRequest(J))
								await messages[0].click(1)
								sleep(1)
							except:
								print('\x1b[1;31;40m' + "Try join in 2 hours later" + '\x1b[0m')
								break
						else:
							messages = await client.get_messages(bot_id)
							# await messages[0].click(3)
							print('\x1b[1;31;40m' + "Skipping... CloudFlare System" + '\x1b[0m')
							sleep(1)
							browser_open()
						messages2 = await client.get_messages(bot_id, limit=2)
						try:
							if 'You must stay' in messages2[1].message:
								print('\x1b[1;33;40m' + messages2[1].message + '\x1b[0m')
								did()
							elif 'We cannot find' in messages2[0].message:
								await messages[0].click(1,1)
								print('\x1b[1;31;40m' + messages2[0].message + '\x1b[0m')
							elif 'no longer valid' in messages2[0].message:
								print('\x1b[1;31;40m' + "Sorry, that task is no longer valid, skipping..." + '\x1b[0m')
						except:
							break
					except requests.exceptions.TooManyRedirects:
						traceback.print_exc()
						await messages[0].click(2)
					except AttributeError:
						traceback.print_exc()
						browser_open()
					except browser_cookie3.BrowserCookieError or ValueError:
						traceback.print_exc()
						os.system('rm -rf /.config/chromium/Default/Cookies')
						browser_open()
					except:
						traceback.print_exc()
						break
				except:
					break
				# async for message in client.iter_messages(bot_id):
   				# 	print(message.id, message.text)
		with client:
			client.loop.run_until_complete(join())


# -----------JOIN CHANNEL CODE END--------------------------------------------------------------------------------

# --------------WITHDRAW CODE START---------------------------------------------------------------------------
		async def withdraw():
			await client.send_message(bot_id, '/balance')
			sleep(2)
			messages = await client.get_messages(bot_id)
			print(messages[0].message)
			if 'Available balance' in messages[0].message:
				print("\n", '\x1b[1;37;40m' + "---------------------------[ withdraw ]" + '\x1b[0m')
				money = messages[0].message.split("Available balance: ", 1)[1]
				if 'DOGE' in money:
					balance = money.split(" DOGE")[0]
					limit = 1.3
				else:
					sc = " " + tag
					balance = money.split(sc)[0]
					if tag == 'BTC':
						limit = 0.00005
					elif (tag == 'LTC' or tag == 'ZEC'):
						limit = 0.0003
					elif tag == 'BCH':
						limit = 0.0001
				b = float(balance)
				acc_b.append(balance)
				if (b < limit):
					print('\x1b[1;32;40m' + money + '\x1b[0m')
				else:
					await client.send_message(bot_id, '/withdraw')
					sleep(5)
					await client.send_message(bot_id, wallet)
					sleep(5)
					await client.send_message(bot_id, balance)
					sleep(5)
					await client.send_message(bot_id, '/Confirm')
					sleep(5)
					print('\x1b[1;32;40m' + "Successfully withdraw " + '\x1b[0m', balance, " ", tag)
		
		
		
		with client:
			client.loop.run_until_complete(withdraw())
# --------------WITHDRAW CODE END---------------------------------------------------------------------------



	except Exception as e:
		print(e)
		print('\x1b[1;31;40m' + "Client Disconnected !" + '\x1b[0m')
		print('\x1b[1;31;40m' + "-------------------------------" + '\x1b[0m')

# ---------ADD NUMBER CODE START-----------------------------------------------------------------------------------------

def addnumber(number):
	text = '\x1b[1;36;40m' + "Please type Your phone number with country code\nexample: +172565135485\n?:" + '\x1b[0m'
	
	# print(2*"\n", '\x1b[1;36;40m' + "Please type it again >>>> (Just your phone number with country code!)" + '\x1b[0m')
	try:
		if not os.path.exists("session"):
			os.mkdir("session")
		client = TelegramClient("session//"+number, api_id, api_hash)
		client.start(number)

		async def main():
			txt = open("ref.txt", 'r')
			for i in range(5):
				code = txt.readline()
				msg = '/start ' + code
				bot = bot_ids2[i]
				await client.send_message(bot, msg)
				# messages = await client.get_messages(bot, from_user=bot)
				# print(messages.text)
				print('\x1b[1;32;40m' + "Successfully join " + bot_tag[i] + " bot with your link" + '\x1b[0m')
			
			await client.send_message(bot_ids2[0], '/start')
			#@client.on(events.NewMessage(chats=bot_ids2[0]))
			#async def handler(event):
				# print(event.raw_text)
			sleep(1)
			hello = await client.get_messages(bot_ids2[0])
			if 'In order to use this bot' in hello[0].message:
				url2 = hello[0].reply_markup.rows[0].buttons[0].url
				# await hello[0].click(0,0)
				r = requests.get(url2)
				await hello[0].click(1,0)
			await client.send_message(bot_ids2[0], '/settings')
			print('\x1b[1;32;40m' + "Allowing NSFW....." + '\x1b[0m')
			sleep(1)
			messages = await client.get_messages(bot_ids2[0])
			if 'Choose a setting' in messages[0].message:
				# print(event.raw_text)
				await messages[0].click(0)
			sleep(1)
			response = await client.get_messages(bot_ids2[0])
			if 'disabled' in response[0].message:
				await response[0].click(0)
				await client.disconnect()
			else:
				await client.disconnect()
			#await client.run_until_disconnected()
		with client:
			client.loop.run_until_complete(main())
		print(2*"\n", '\x1b[1;32;40m' + "Please Add your number into list.txt (+1504...)" + '\x1b[0m')
	except Exception as e:
		print("\n", '\x1b[1;31;40m' + "Please check Your phone number is Correct or try again" + '\x1b[0m')
		print(number)
		traceback.print_exc()
	# os.chdir(r"session\\")
	# os.rename('.session',number+'.session')

# ---------ADD NUMBER CODE END-----------------------------------------------------------------------------------------

# ---------PROGRESSBAR CODE START-----------------------------------------------------------------------------------------


def progressbar(it, prefix="", size=60, file=sys.stdout):
	count = len(it)
	def show(j):
		x = int(size*j/count)
		file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
		file.flush()
	show(0)
	for i, item in enumerate(it):
		yield item
		show(i+1)
	file.write("\n")
	file.flush()

# ---------PROGRESSBAR CODE END-----------------------------------------------------------------------------------------

def leave(number):
	try:
		session = "session//" + number
		client = TelegramClient(session, api_id, api_hash)
		client.connect()
		client.sign_in(session)
		async def g():
			async for m in client.iter_dialogs():
				if m.is_group or m.is_channel:
					cg.append(m.title)
					# print(cg)
		#----------- filter excluded groups or channels and get new list -----------------
			for i in ex:
				if i in cg:
					cg.remove(i)
				else:
					pass
		# ------------------ PRINT CHANNELS OR GROUPS IN ORDER-----------------------
			for i in range(len(cg)):
				print(cg[i])
			print("\n\n")
		# ----------------LEAVE CHANNELS OR GROUPS-------------------------------
			for i in cg:
				try:
					print("leaved :- "+i)
					# await client(LeaveChannelRequest(i))
					# await client.delete_dialog(i)
					await client.delete_dialog(i)
				except:
					print("Not a member of group or channel :- "+i)
			cg.clear()
		client.loop.run_until_complete(g())
	except:
		print("not working")

def start():
	# os.chdir(os.path.dirname(__file__))
	print(5*"\n", '\x1b[1;36;40m' + "Choose:" + '\x1b[0m')
	print(
		'\x1b[1;35;40m',
		"""
1. Your Numbers
2. Add your New account to list and Auto refferal
3. Change refferal links
4. Change your wallet Address
5. Auto Withdraw
6. Auto view, Msg bot, Join and Withdraw
7. Auto Leave Channels, Groups and Bots
8. Help
9. Donate :)
10. auto view, msg bot, Join and withdraw in loop
11. leave 
		""",
		'\x1b[0m'
	)
	while True:
		try:
			choose = int(input("Number: "))
			if (1 <= choose <= 12):
				break
			else:
				print('\x1b[1;31;40m' + "Please type 1-9" + '\x1b[0m')
		except:
			print('\x1b[1;31;40m' + "Invalid data please type 1-9" + '\x1b[0m')

	sleep(0.5)
	system('cls||clear')
	if choose == 1:
		txt = open("list.txt", 'r')
		count = 0
		for i in txt.readlines():
			count += 1
			print(i, end='')
		txt.close()
		print(2*"\n", '\x1b[1;37;40m' +
			  f"You have {str(count)} Numbers" + '\x1b[0m')
		print("\n", press)
		input("")
	elif choose == 3:
		ref_txt = 'ref.txt'
		txt = open(ref_txt, 'r')
		print('\x1b[1;36;40m' + "Your refferal links:" + '\x1b[0m', "\n")
		count = 0
		for i in txt.readlines():
			print('\x1b[1;36;40m' + ref[count] + i + '\x1b[0m')
			count += 1
		txt.close()
		print("\n", '\x1b[1;34;40m' +
			  "Would you like to change refferal links? y/n" + '\x1b[0m')
		Y_N = input(": ")
		if Y_N == "y":
			remove(ref_txt)
			txt = open(ref_txt, "w")
			for i in range(5):
				text = "Enter Your " + ref[i][0:3] + " refferal link: "
				ref_link = input(text)
				link = ref_link.split("=", 1)[1]
				if i == 0:
					txt.writelines(link)
				else:
					txt.writelines("\n")
					txt.writelines(link)
			txt.close()
			print('\x1b[0;34;40m' +
				  "Saved! back to the menu in 5 second" + '\x1b[0m')
			sleep(5)
		elif Y_N == "n":
			print("wait...")
		else:
			print('\x1b[1;31;40m' + "Invalid requests" + '\x1b[0m')
			sleep(1)
	elif choose == 4:
		print("Please change value in wallet.json file")
		print(press)
		input("")
	elif choose == 8:
		print("Join our group")
		print("\n", press)
		input("")
	elif choose == 9:
		print("My LTC wallet address")
		print("\n", press)
		input("")
	elif choose == 7:
		print(3*"\n", '\x1b[1;31;40m' + "Sorry, Use rayez source" + '\x1b[0m')
		print("\n", press)
		input("")
	elif choose == 2:
		number = input("Enter your number:")
		addnumber(number)
		print(press)
	elif (choose == 5 or choose == 6):
		print('\x1b[1;36;40m' + "Choose:" + '\x1b[0m')
		print(
			'\x1b[1;35;40m',
			"""
1. Doge
2. LTC
3. BCH
4. ZEC
5. BTC
			""",
			'\x1b[0m'
		)
		while True:
			try:
				coin_bot = int(input("Number: "))
				if (1 <= coin_bot <= 5):
					break
				else:
					print('\x1b[1;31;40m' + "Please type 1-5" + '\x1b[0m')
			except:
				print('\x1b[1;31;40m' +
					  "Invalid Number please type 1-5" + '\x1b[0m')
		cb = coin_bot - 1
		bot_id = bot_ids[cb]
		tag = bot_tag[cb]
		system('cls||clear')
		print(3*"\n")
		contsu = '\x1b[1;37;40m' + "Connecting: " + '\x1b[0m'
		for j in progressbar(range(100), contsu, 50):
			sleep(0.05)
		sk = True
		with open("wallet.json") as json_file:
			wallet = json.load(json_file)
			wallet = wallet[tag]
		print('\x1b[1;36;40m' + "Your " + tag +
			  " Wallet Address" + '\x1b[0m', wallet)
		print(15*" ", '\x1b[1;32;40m' +
			  "<<< --- $$$ --- >>>" + '\x1b[0m', "\n")
		txt = open("list.txt", "r")
		for i in txt.readlines():
			if '+' not in i:
				print(
					'\x1b[1;31;40m' + "Please check list.txt file or You haven't yet add your phone number" + '\x1b[0m')
				sk = False
				break
			else:
				if "\n" in i:
					i = i.replace("\n", "")
				send(i, bot_id, tag, wallet, choose)
				sleep(5)
		if sk is True:
			print(3*"\n", '\x1b[1;31;40m' +
				  "<<< The work has been finished >>>" + '\x1b[0m')
		txt.close()
		print('\x1b[1;35;40m', "did ", tasks[0], " Tasks today!", '\x1b[0m')
		tasks.clear()
		tasks.append(0)
		counter(tag)
		print(2*"\n", press)
		input('')
	elif (choose == 10):
		print('\x1b[1;36;40m' + "Choose:" + '\x1b[0m')
		print(
			'\x1b[1;35;40m',
			"""
1. Doge
2. LTC
3. BCH
4. ZEC
5. BTC
			""",
			'\x1b[0m'
		)
		while True:
			try:
				coin_bot = int(input("Number: "))
				if (1 <= coin_bot <= 5):
					break
				else:
					print('\x1b[1;31;40m' + "Please type 1-5" + '\x1b[0m')
			except:
				print('\x1b[1;31;40m' +
					  "Invalid Number please type 1-5" + '\x1b[0m')

		def run():
			cb = coin_bot - 1
			bot_id = bot_ids[cb]
			tag = bot_tag[cb]
			system('cls||clear')

			print(3*"\n")
			contsu = '\x1b[1;37;40m' + "Connecting: " + '\x1b[0m'
			for j in progressbar(range(100), contsu, 50):
				sleep(0.05)
			sk = True
			with open("wallet.json") as json_file:
				wallet = json.load(json_file)
				wallet = wallet[tag]
			print('\x1b[1;36;40m' + "Your " + tag +
				  " Wallet Address" + '\x1b[0m', wallet)
			print(15*" ", '\x1b[1;32;40m' +
				  "<<< --- $$$ --- >>>" + '\x1b[0m', "\n")
			txt = open("list.txt", "r")
			for i in txt.readlines():
				if '+' not in i:
					print(
						'\x1b[1;31;40m' + "Please check list.txt file or You haven't yet add your phone number" + '\x1b[0m')
					sk = False
					break
				else:
					if "\n" in i:
						i = i.replace("\n", "")
					send(i, bot_id, tag, wallet, choose)
					sleep(5)
			if sk is True:
				print(3*"\n", '\x1b[1;31;40m' +
					  "<<< The work has been finished >>>" + '\x1b[0m')
			txt.close()
			print('\x1b[1;35;40m', "did ", tasks[0],
				  " Tasks today!", '\x1b[0m')
			tasks.clear()
			tasks.append(0)
			counter(tag)
		def loop():
			for i in range(30):
				def countdown(t):
					while (t):
						mins, secs = divmod(t, 60)
						timer = '{:02d}:{:02d}'.format(mins, secs)
						print(f"WAIT {timer} TO RESTART", end="\r")
						time.sleep(1)
						t -= 1
				run()
				print("Round :- ",i)
				countdown(7200)
		while True:
			loop()
			time.sleep(10)
			# txt = open("list.txt", "r")
			# for i in txt.readlines():
			# 	if '+' not in i:
			# 		print('\x1b[1;31;40m' + "Please check list.txt file or You haven't yet add your phone number" + '\x1b[0m')
			# 		sk = False
			# 		break
			# 	else:
			# 		if "\n" in i:
			# 			i = i.replace("\n", "")
			# 			print('leaving')
			# 			print(i)
			# 			leave(i)
			# txt.close()
			sleep(5)
	
	elif (choose == 11):
		txt = open("list.txt", "r")
		for i in txt.readlines():
			if '+' not in i:
				print('\x1b[1;31;40m' + "Please check list.txt file or You haven't yet add your phone number" + '\x1b[0m')
				sk = False
				break
			else:
				if "\n" in i:
					i = i.replace("\n", "")
					print('leaving')
					print(i)
					leave(i)
					sleep(2)
		txt.close()

while 1 == 1:
	# system('cls||clear')
	start()
