import cleverbotfree
from googletrans import Translator
from excFormatter import Format

translator = Translator()

async def getresponse(input):
	try:
		print("\t\tgenerating response for:", input)

		#lingua del messaggio originale
		msglanguage = translator.detect(input).lang
		print("\t\tmessage received in language:", msglanguage)

		#dato che il bot è usato in Italiano. in teoria funziona anche per altre lingue
		input = translator.translate(input, src=msglanguage).text
		print("\t\ttranslated input:", input)

		#ottiene la risposta
		print("\t\t\tgetting p_w...")
		async with cleverbotfree.async_playwright() as p_w:
			print("\t\t\tgetting c_b...")
			c_b = await cleverbotfree.CleverbotAsync(p_w)
			print("\t\t\tgetting response...")
			response = await c_b.single_exchange(input)
			print("\t\t\tclosing c_b...")
			await c_b.close()
		print("\t\tresponse:", response)

		if response == "": response = "i couldn't process the question, sorry"

		#per mantenere continuità, il bot risponde nella stessa lingua in cui gli scrivi
		response = translator.translate(response, dest=msglanguage).text
		print("\t\ttranslated response:", response)
	except Exception as e:
		print("\t\tan error occured:", e)
		response = Format(e)

	return response
