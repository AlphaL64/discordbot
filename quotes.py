def getquote():
	import random, inspirobot
	from googletrans import Translator
	x = Translator()
	quote = x.translate(random.choice(inspirobot.flow()), dest="it").text
	quote = f'"_{quote}_"\n\n\t\t- ' + random.choice(BOOK_AUTHORS + QUOTE_AUTHORS)
	return quote
QUOTE_AUTHORS = [
	"Barack Obama",
	"Sun Tsu",
	"Socrate",
	"Aristotele",
	"Napoleone Bonaparte",
	"Abramo Lincoln",
	"Mahatma Ghandi",
	"Giulio Cesare",
	"John F. Kennedy",
	"Micheal Jackson",
	"Hirohito",
	"Nelson Mandela",
	"Martin Luther King",
	"Winston Churchill",
	"Bill Gates",
	"Madre Teresa",
	"Cristoforo Colombo",
	"Albert Einstein",
	"Charles Darwin",
	"Regina Elisabetta II",
	"George Orwell",
	"Leo Tolstoy",
	"Vladimir Lenin",
	"Elon Musk",
	"Cleopatra",
	"Steve Jobs",
	"Sigmund Freud",
	"Mao Zedong",
	"Silvio Berlusconi",
	"Marco Aurelio",
	"Karl Marx",
	"William Shakespeare",
	"Barbiere di Siviglia",
	"Dante Alighieri",
	"Virgilio",
]
BOOK_AUTHORS = [
	"Sun Tsu, in \"L'Arte della Guerra\"",
	'Platone, in "La Repubblica"',
	'Leo Tolstoy, in "Guerra e Pace"',
	'Marco Aurelio, in "Meditazioni"',
	'George Orwell, in "1984"',
	'Karl Marx, in "Il Capitale"',
	"Charles Darwin, in \"L'Origine delle Specie\"",
	'Albert Einstein, "La Teoria della Relatività"',
	"Laerte, in Amleto",
	"Virgilio, nella Divina Commedia",
]