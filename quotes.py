def getquote():
	import random, inspirobot
	from googletrans import Translator
	x = Translator()
	
	#this whole thing is to prevent quotes about "keep breathing" because they're everywhere and they're boring
	quote = None
	for q in inspirobot.flow():
		if "breath" in q.quote:
			continue
		quote = q.quote
		break
	if quote is None: quote = getquote()

	quote = x.translate(quote, dest="it").text
	quote = f'"_{quote}_"\n\n\t\t- ' + random.choice(BOOK_AUTHORS + QUOTE_AUTHORS)
	return quote
QUOTE_AUTHORS = [

	#imprenditori
	"Bill Gates",
	"Elon Musk",
	"Steve Jobs",
	
	#politici
	"Hirohito",
	"Winston Churchill",
	"Regina Elisabetta II",
	"Cleopatra",
	"Mao Zedong",
	"Silvio Berlusconi",
	"Josif Stalin",
	"Matteo Renzi",
	"Mario Draghi",
	"Vladimir Lenin",
	"Xi Jinping",
	"Giuseppe Garibaldi",
	"Barack Obama",
	"Napoleone Bonaparte",
	"Abramo Lincoln",
	"Giulio Cesare",
	"John F. Kennedy",
	"Benito Mussolini",
	"Matteo Salvini",
	"Andrea di Piero",
	
	#filosofi
	"Albert Einstein",
	"Charles Darwin",
	"Sigmund Freud",
	"Marco Aurelio",
	"Karl Marx",
	"Immanuel Kant",
	"Sun Tsu",
	"Socrate",
	"Aristotele",

	#scrittori, poeti, cantanti
	"George Orwell",
	"Leo Tolstoy",
	"William Shakespeare",
	"Dante Alighieri",
	"Virgilio",
	"Giuseppe Ungaretti",
	"Giacomo Leopardi",
	"Micheal Jackson",

	#gente varia
	"Cristoforo Colombo",
	"Martin Luther King",
	"Madre Teresa",
	"Nelson Mandela",
	"Mahatma Ghandi",
	
	#cagate
	"Barbiere di Siviglia",
	"Gosig Ratta",
	"Leo Mesi",
	"Rocktopus",
]
BOOK_AUTHORS = [
	"Sun Tsu, in \"L'Arte della Guerra\"",
	'Platone, in "La Repubblica"',
	'Leo Tolstoy, in "Guerra e Pace"',
	'Marco Aurelio, in "Meditazioni"',
	'George Orwell, in "1984"',
	'Karl Marx, in "Il Capitale"',
	'Karl Marx, in "Il Manifesto Comunista"',
	"Charles Darwin, in \"L'Origine delle Specie\"",
	'Albert Einstein, "La Teoria della Relatività"',
	"Laerte, in Amleto",
	"Virgilio, nella Divina Commedia",
	"Immanuel Kant, in \"Critica alla ragion pura\"",
	"Giuseppe Garibaldi al suo esercito, prima di iniziare la spedizione dei mille",
]