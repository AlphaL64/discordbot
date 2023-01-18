
import discord

#se True allora cleverbot verrà aperto
DO_CHATBOT = False

#constants
SELF_PING : str

INIT_SUCC_MSG = "online!"

BOT_LOG_CHANNEL = "bot-log"

REACTIONS = {}
REACTIONS_FILE = "reactions.txt"

COMMAND_PREFIX = "!"
HELP_MSG  = f"""
i comandi si scrivono con "{COMMAND_PREFIX}".
comandi:
	informazioni:
	help			- mi chiedo cosa faccia questo comando
	info			- informazioni sul di me

	funzionalità:
	echo msg		- ripete il messaggio, cancellando il tuo automaticamente
	remindme time [; msg]	- ti manderò un promemoria alla data richiesta. se non aggiungi un messaggio, ti manderò un link al tuo post
	quote			- frase ispirazionale generata al momento
	addreact nome link	- aggiunge una reazione con il nome dato ed il link tenor specificato. richiede l'approvazione di un moderatore
	
	utilità:
	ping [i]		- manda un ping a {"@"} "i" volte (una volta di default)
	sus				- sus

	debug:
	channel			- scrive il nome e l'ID del canale in cui sei
	user			- scrive nome e ID di chi ha scritto il messaggio
"""#qui non funzionano i ping perché il client non è ancora attivo
HELP_MSG_2 = f'i comandi si scrivono con "{COMMAND_PREFIX}". per una lista di comandi usa il comando "help"'
BOT_INFO = f"""
sono un bot programmato da @L, il proprietario del server, e sono fatto in Python usando l'API ufficiale di discord. sono appena stato creato quindi non ho molti comandi, ma sono in continua espansione. se hai suggerimenti, non esitare a mandarli in {"#"}!
"""#'''

MODS: list[discord.User] = []

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
	"di nulla, è più forte di me aiutarti",
	"dall'alto della mia magnanimità non avrei potuto non aiutarti",
]
PYTHON_ANSWERS = [
	"C++ > Python",
	"immagina un linguaggio in cui un errore di battitura ti viene fatto notare",
	"*laughs in clearly superior C++*",
	"_indentation_",
	"programming in Python be like:\nhttps://tenor.com/view/monsters-university-snail-going-on-my-way-omw-gif-5461800",
	"average Python fan:\nhttps://tenor.com/view/kerosene-kero-made-marcus-marcus-marcus-the-snail-he-goes-gif-22365259",
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
	"https://tenor.com/view/among-us-twerk-fast-ass-shake-gif-20107138",
	"https://tenor.com/view/sus-among-us-sussy-bakir-sussy-bakir-gif-24878782",
	"https://tenor.com/view/among-us-sus-default-dance-sussy-sussy-baka-gif-25130929",
	"https://tenor.com/view/when-the-impostor-is-sus-impostor-impostor-among-us-among-us-among-us-sus-gif-24712125",
]