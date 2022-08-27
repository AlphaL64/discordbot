import discord
import os
import sys as sus
from threading import Thread
import asyncio

with open("TOKEN") as f:
	TOKEN = f.read(-1)

#from stayingalive import keep_alive

from botTalk import getresponse
# from stringOps import replace
from timecheck import TimeCheckLoop, AddNewReminder, SetReminderFunction
from quotes import getquote

from er import er as er
from er import ID10T_Exception
import random
from excFormatter import Format


#define the client
client = discord.Client(
	intents=discord.Intents.all()
)

def shell():
	while True:
		inp = input(">>> ")
		if inp == "exit": break
			
		os.system(inp)

#TODO: qualcosa che quando qualcuno manda un link tenor chiede se vuoi aggiungerlo ai comandi e se sì lo fa automaticamente


#funcs
def GetChannel(name : str) -> discord.TextChannel:
	for channel in client.get_all_channels():
		if channel.name == name:
			return channel
	return None
def GetUser(name : str) -> discord.User:
	for user in client.get_all_members():
		if user.name == name:
			return user
	return None
def GetEmote(name : str) -> discord.Emoji:
	for emote in client.emojis:
		if emote.name == name:
			return emote
	return None

def GetPing(name : str) -> str:
	return "<@!" + str(GetUser(name).id) + ">"
def GetChannelLink(name : str) -> str:
	return GetChannel(name).mention

async def SendLog(message):
	await GetChannel(BOT_LOG_CHANNEL).send(message)

async def PingBorse(channel):
	await channel.send(GetPing("Borsez"))

def exit():
	sus.setrecursionlimit(10**8)
	exit()


#constants
SELF_PING : str

BOT_LOG_CHANNEL = "bot-log"

with open("reactions.txt") as rfile:
	import ast
	_ = "{" + "".join(rfile.readlines(-1)) + "}"
	REACTIONS = ast.literal_eval(_)

COMMAND_PREFIX = "!"
HELP_MSG  = f"""
i comandi si scrivono con "{COMMAND_PREFIX}".
comandi:
	informazioni:
	help			- mi chiedo cosa faccia questo comando
	info			- informazioni sul di me

	roba:
	echo msg		- ripete il messaggio, cancellando il tuo automaticamente
	ping [i]		- manda un ping a {"@"} "i" volte (una volta di default)
	remindme time [; msg]	- ti manderò un promemoria alla data richiesta. se non aggiungi un messaggio, ti manderò un link al tuo post
	quote			- frase ispirazionale generata al momento
	sus				- sus

	debug:
	channel			- scrive il nome e l'ID del canale in cui sei
	user			- scrive nome e ID di chi ha scritto il messaggio

	reazioni:
"""#qui non funzionano i ping perché il client non è ancora attivo
for command in REACTIONS:
	HELP_MSG += f"\t{command}\n"
HELP_MSG_2 = f'i comandi si scrivono con "{COMMAND_PREFIX}". per una lista di comandi usa il comando "help"'
BOT_INFO = f"""
sono un bot programmato da @L, il proprietario del server, e sono fatto in Python usando l'API ufficiale di discord. sono appena stato creato quindi non ho molti comandi, ma sono in continua espansione. se hai suggerimenti, non esitare a mandarli in {"#"}!
"""#'''

SUPERUSER_PREFIX = "superuser "
SUPERUSER_IDS = [ 487601580539904000 ]
INVALID_SUPER_ID = [#messaggi da mandare quando l'ID che richiede permessi superuser non è valido
	"..._but nothing happened_",
	"eh! volevi!",
	f"ti credi intelligente? ascolto solo il mio padrone, <@!{SUPERUSER_IDS[0]}>!",
	"non sei degno di questo potere!",
	"https://tenor.com/view/sora-lella-tie-gif-7741962"
]

CHINESE_ANSWERS = [
	"哔哔生菜",
	"台湾是中国",
	"我爱中国",
	"你没有脑子",
	"请中青虫",
]
RISPOSTE_GRAZIE = [
	"di nulla",
	"non c'è di che",
	"è un piacere esserti utile",
	"a volte è dura essere benevolo quanto me",
	"non per vantarmi, ma merito decisamente la tua gratitudine",
]
PYTHON_ANSWERS = [
	"C++ > Python",
	"immagina un linguaggio in cui un errore di battitura ti viene fatto notare",
	"*laughs in clearly superior C++*",
]
SUS_ANS = [
	"""
. 　　　。　　　　•　 　ﾟ　　。 　　.

　　　.　　　 　　.　　　　　。　　 。　. 　

.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•

　　ﾟ　　 Red was not An Impostor.　 。　.

　　'　　　 1 Impostor remains 　 　　。

　　ﾟ　　　.　　　. ,　　　　.　 .
""",
	"""
➖➖🟥🟥🟥
➖🟥🟥🟦🟦🟦
🟥🟥🟥🟦🟦🟦
🟥🟥🟥🟦🟦🟦
🟥🟥🟥🟥🟥🟥
➖🟥🟥🟥🟥🟥
➖🟥🟥➖🟥🟥
➖🟥🟥➖🟥🟥""",
	"ඞ",
]

#per l'aggiunta di reazioni tenor
waiting_for_conf = False
confirm_event = asyncio.Event()
	

#events
@client.event
async def on_ready():
	print(f'succesfully logged in as {client.user}')
	#set this
	global SELF_PING
	SELF_PING = GetPing(client.user.name)
	from time import time
	random.seed(time())

	#aggiunge un collegamento a generale alle info del bot. non possiamo settarlo insieme al resto del messaggio perché il client non è attivo
	global BOT_INFO
	BOT_INFO = BOT_INFO.replace("#", GetChannelLink("bot-tests"))
	global HELP_MSG
	HELP_MSG = HELP_MSG.replace("@", GetPing("Borsez"))

	await SendLog("online!")

@client.event
async def on_message(message: discord.Message):
	#è
	try:
		#we were waiting for tenor link adding confirmation
		if waiting_for_conf is True:
			if message.content == "aggiungi":
				confirm_event.set()

		if message.author.id == 886477323812110356:
			await message.channel.send(random.choice(["shut up", "dumbass", "fuck off", "i'll ban you", f"imagine being {message.author.mention}", "learn to write idiot", "", "i'll fucking turn you off if you don't shut up now", f"\"{message.author.mention}\" means 'idiot' in ancient Latin", "excuse me, i couldn't find any sign of intelligence in your message"]))
			return

		with message.channel.typing():
			if message.author == client.user:
				return
		
			print("received message:\n\t" + message.content + "\n")
		
			channel : discord.TextChannel = message.channel
			contl: str = message.content.lower()
			
			#if we get a ping we call cleverbot chat
			if SELF_PING in message.content or client.user.mention in message.content:
				#await channel.send(random.choice(PING_ANSWERS) if random.randint(0, len(PING_ANSWERS) + 1) != 0 else message.author.mention)
				print("\t" "initiating chat")
				msg: str = message.content
		
				#cambiamo dal ping a un nome generico, in modo che quella stringa di numeri non mandi in palla l'IA
				if client.user.mention in msg:
					msg = msg.replace(client.user.mention, "")
				else:	#if either of the two always
					msg = msg.replace(SELF_PING, "")
		
				response = await getresponse(msg)
				print("\t" "out of getresponse function")
		
				await message.reply(response, mention_author=False)
				return
		
			if contl.startswith("https://tenor.com/view/") or contl.startswith("https://c.tenor.com/"):
				await AddLink(message)
				return

			#these are absolutely necessary
			import re
			if re.search(u'[\u4e00-\u9fff]+', message.content) is not None:
				await channel.send(random.choice(CHINESE_ANSWERS))
			if "python" in contl:
				await channel.send(random.choice(PYTHON_ANSWERS))#TODO: più frasi belle lmao
			if "gatt" in contl:
				await PingBorse(channel)
			if "grazie" in contl:
				await message.reply(random.choice(RISPOSTE_GRAZIE))
			if "1984" in contl and not contl.startswith(COMMAND_PREFIX):
				await channel.send("https://c.tenor.com/KpzU7TGzfEcAAAAM/1984-skander.gif")
		
			#aiuto a parte il comando
			if contl in ["help", "aiuto"]:
				await channel.send(HELP_MSG_2)
		
			#se è un comando normale
			if message.content.startswith(COMMAND_PREFIX):
				await NormalCommands(message)
			#se è un comando superuser
			if message.content.startswith(SUPERUSER_PREFIX):
				await SuperuserCommands(message)
		#END WITH
	#invalid commando
	except ID10T_Exception:
		await channel.send(er())
	#un altro problemo
	except Exception as e:
		await channel.send(er())
		await SendLog(f"il seguente messaggio ha causato un problema:\n{message.content}\n\nl'errore:\n" + Format(e))

async def NormalCommands(message: discord.Message):
	channel: discord.TextChannel = message.channel
	msg: str = message.content[len(COMMAND_PREFIX):]	#teniamo solo il comando in se in modo che non dobbiamo preoccuparci del prefisso se cambia
	
	if msg == "help":
		await channel.send(HELP_MSG)
			
	elif msg == "info":
		await channel.send(BOT_INFO)
		
	elif msg.startswith("echo"):
		await channel.send(msg[4:])
		await message.delete()
			
	elif msg.startswith("ping"):
		print("\t" "comedy genius")
		if msg == "ping":	#no parameters
			await PingBorse(channel)
		else:
			tot = int(msg[4:])
			if tot < 1: raise
			for i in range(tot):
				await PingBorse(channel)

	elif msg == "quote":
		await channel.send(getquote())
	
	elif msg.startswith("remindme"):
		user = message.author.name
		time = msg[9:msg.index(";")] if ";" in msg else msg[9:]
		mesg  = msg[msg.index(";") + 1:] if ";" in msg else message.jump_url
		AddNewReminder(time, user, mesg)
		await channel.send("promemoria salvato!")

	elif msg == "user":
		await channel.send(f"{message.author.display_name} ({message.author.id})")
	elif msg == "channel":
		await channel.send(f"{message.channel} ({message.channel.id})")

	elif msg == "sus":
		await channel.send("ඞ")

	elif msg in REACTIONS:
		await channel.send(REACTIONS[msg])

	else:
		raise ID10T_Exception
#END commands
async def SuperuserCommands(message : discord.Message):
	try:
		print("\t" "in superuser function")

		channel: discord.TextChannel = message.channel
		msg: str = message.content[len(SUPERUSER_PREFIX):]

		shutdown = lambda: os.system("shutdown /s")
		reboot = lambda: os.system("shutdown /r /t 1")

		if message.author.id not in SUPERUSER_IDS:
			await channel.send(random.choice(INVALID_SUPER_ID))
			await SendLog(f"{message.author} tried executing a superuser command")
			return
		
		print("\t" "executing superuser command")
		await SendLog(f"{message.author} executing superuser command:\n\t" + message.content)

		if msg == "reboot":
			await SendLog("restarting...")
			cmd = "\""
			for i in sus.argv:
				cmd += i + " "
			cmd = cmd[:-1] + "\""
			os.system(cmd)
			exit()
		elif msg == "shutdown":
			await SendLog("shutting down...")
			exit()
		elif msg.startswith("exec"):
			print("\t" "executing:\n\t" + msg[5:])
			exec(msg[5:])
		elif msg.startswith("pm("):
			username = GetUser(msg[3:msg.index(",")])
			emssage = eval(msg[msg.index(",")+1:msg.index(")")])
			await pm(username, emssage)
		elif msg.startswith("ban"):
			await GetUser(msg[4:]).ban()
		elif msg.startswith("kick"):
			await GetUser(msg[5:]).kick()

	except Exception as e:
		await SendLog(f"Errore nell'uso del comando superuser {msg}:\n" + Format(e))
#END superuser

async def pm(user, message):
	await user.send(message)

async def AddLink(msg : discord.Message):
	global waiting_for_conf
	waiting_for_conf = True
	await msg.channel.send("ho rilevato un link tenor. scrivi 'aggiungi' se vuoi aggiungerlo alla lista di reazioni veloci")
	await confirm_event.wait()
	#resetta i flag
	confirm_event.clear()
	waiting_for_conf = False
	#aggiungi il link
	#TODO: nome


@client.event
async def on_member_join(member: discord.User):
	await GetChannel("generale").send("@everyone è arrivato " + member.mention)
@client.event
async def on_member_remove(member: discord.User):
	None()

#TODO: non funziona
# async def start_coros():
#     # ensure_future -> create_task in Python 3.7
#     tasks = [asyncio.ensure_future(coro()) for coro in (coro1, coro2)]
#     await asyncio.wait(tasks)
def SendReminder(user, message):
	import asyncio
	asyncio.run(GetChannel("promemoria").send(GetUser(user).mention + "\n" + message))


#main
import platform		#cpcls
os.system("cls" if platform.system() == "Windows" else "clear")

print("starting...")
# keep_alive()

try:
	SetReminderFunction(SendReminder)
	timecheckthread = Thread(target=TimeCheckLoop)
	timecheckthread.start()

	#main client
	client.run(TOKEN)
except Exception as e:
	raise e
	#idk probabilmente quello sotto è una cosa no buona da fare sul computer
	with open(".log", "w") as txt:
		txt.write(Format(e) + "\n\n\n\n")
	os.system("kill 1")
	client.run(TOKEN)