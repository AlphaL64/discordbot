import datetime as __dt
import time as __time
from typing import Callable as _func

#file dove sono salvati i reminder se il bot si spegne
__FILENAME = "reminders.tmk"
#promemoria attivi (la stringa è l'user che ha richiesto e il messaggio)
reminders=[]#: list[tuple[__dt.date, str, str]] = []
#tempo tra un check e l'altro di cui viene rallentato manualmente il programma
LAMP = 0
#messaggio da mandare come promemoria
MESSAGE_STRING = "ecco il tuo promemoria:\n%m"

#come si scrive sul file
__FILE_FORMAT = "%t\n%u\n%m\n\n"
__LINE_COUNT = __FILE_FORMAT.count("\n")	#serve quando cancelli il coso dal file

def AddNewReminder(time : str, user : str, msg : str):
	reminders.append(
		(__FormatDate(time), user, msg)
	)
	#probably very stupid, but this way if the file is inaccessible we don't do a bad thing
	while True:
		try:
			with open(__FILENAME, "a") as file:
				string = __FILE_FORMAT
				string = string.replace("%t", str(time))
				string = string.replace("%u", user)
				string = string.replace("%m", msg)
				file.write(string)
			break
		except:
			pass

def TimeCheckLoop():
	"""loops forever checking if the current time is equal to any of the ones we're waiting for"""
	__init()

	while True:
		for tup in reminders:
			date = tup[0]
			if __dt.datetime.now() >= date:
				__SendReminder(tup[1], tup[2])	#user, message
				__RemoveReminder(tup)

		__time.sleep(LAMP)

def __RemoveReminder(reminder):
	reminders.remove(reminder)

	with open(__FILENAME, "r") as ifile:
		lines = ifile.readlines()
	#adesso si toglie la data dalle linee lette
	#non usiamo for perché while in questo caso da più libertà
	i = 0
	while i < len(lines):
		print(lines[i], reminder[0])
		#se abbiamo trovato la data giusta rimuovi tutte le linee
		if lines[i] == str(reminder[0]) + "\n":
			for i in range(__LINE_COUNT):
				lines.pop(i)
			#i'm too scared to do break
			i = len(lines)
		#se no vai alla prossima linea che contiene una data
		else:
			i += __LINE_COUNT
	#riscrivi le linee cambiate
	with open(__FILENAME, "w") as ofile:
		ofile.writelines(lines)

def __FormatDate(date : str) -> __dt.datetime:
	#tutti i formati di data che verranno provati
	formats = [
		"%H:%M, %d/%m/%y",
		"%H:%M, %d/%m/%Y",
		"%d/%m/%Y",
		"%d/%m/%y",
	]
	#quello che non causa problemi è quello giusto
	for format in formats:
		try:
			retval = __dt.datetime.strptime(date, format)
			break
		except:
			pass

	try:
		return retval
	except:
		raise ValueError(f"date ({date}) is in invalid format")

def __init():
	#legge dal file e aggiunge alla lista
	with open(__FILENAME) as file:
		lines = file.readlines()
	for i in range(0, len(lines), __LINE_COUNT):
		date = __FormatDate(lines[i + 0][:-1])
		usr = lines[i + 1]
		msg = lines[i + 2]
		reminders.append(
			(date, usr, msg)
		)


#here just because
def __SendReminder(user, message):
	raise NotImplementedError("function SendReminder was not assigned")

def SetUp(lamp=LAMP, message_string=MESSAGE_STRING):
	global LAMP, MESSAGE_STRING
	LAMP = lamp
	MESSAGE_STRING = message_string
def SetReminderFunction(function : _func[[str, str], None]):
	global __SendReminder
	__SendReminder = function
