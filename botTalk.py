from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#yooooooooooooooooo
from selenium_stealth import stealth

from googletrans import Translator
from excFormatter import Format

from time import sleep

translator: Translator    = None
driver: webdriver.Chrome  = None

BOT_LINK = "https://www.cleverbot.com"

_CONFIRM_BTN_PATH = "/html/body/div[1]/div[2]/div[1]/div/div/form/input"
_INPUT_FIELD_PATH = "/html/body/div[1]/div[2]/div[3]/form/input[1]"
_LAST_ANSWER_PATH = "/html/body/div[1]/div[2]/div[3]/p[9]/span[1]"
_ANSWER_DONE_PATH = "/html/body/div[1]/div[2]/div[3]/p[9]/span[2]"

PAUSE_WAIT_TIME = 0.2
WAIT_ITERATIONS = 50


def talkbot_init():
	global translator, driver
	#set up translator
	translator = Translator()

	#set up browser
	chrome_options = Options()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome(options=chrome_options)
	# driver.set_window_size(1,1)

	#prevents us from being blocked by the website
	stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  	)

	#set up website
	driver.get(BOT_LINK)
	driver.find_element(by.XPATH, _CONFIRM_BTN_PATH).click()

	#check the thing works
	driver.find_element(by.XPATH, _INPUT_FIELD_PATH).send_keys("hello this is a test" + "\n")
	sleep(1)
	try:
		if driver.find_element(by.XPATH, _LAST_ANSWER_PATH).text not in [None, ""]:
			print("init successful")
		else:
			raise
	except Exception as e:
		print("init failed:", e, "\n\nyou can still use the bot, but talk functionality won't be available")
		raise
#END

def talkbot_exit():
	driver.quit()
#END


async def _askbot(prompt: str) -> str:
	driver.find_element(by.XPATH, _INPUT_FIELD_PATH).send_keys(prompt + "\n")

	for each in range(WAIT_ITERATIONS):
		sleep(PAUSE_WAIT_TIME)
		#check if the answer is done writing
		try:
			x = driver.find_element(by.XPATH, _ANSWER_DONE_PATH).id
		except NoSuchElementException:
			continue
		else:
			ans = driver.find_element(by.XPATH, _LAST_ANSWER_PATH).text
			return ans
	
	#no answer was ever obtained
	return ""
#END

async def getresponse(prompt: str) -> str:
	try:
		print("\t\tgenerating response for:", prompt)

		#lingua del messaggio originale
		# msglanguage = translator.detect(prompt).lang
		msglanguage = "it"
		print("\t\tmessage received in language:", msglanguage)

		#dato che il bot è usato in Italiano. in teoria funziona anche per altre lingue
		prompt = translator.translate(prompt, src=msglanguage).text
		print("\t\ttranslated input:", prompt)

		#ottiene la risposta
		print("\t\t\tgetting answer...")
		response = await _askbot(prompt)
		print("\t\tresponse:", response)

		if response == "": response = "i couldn't process the question, sorry"

		#per mantenere continuità, il bot risponde nella stessa lingua in cui gli scrivi
		response = translator.translate(response, dest=msglanguage).text
		print("\t\ttranslated response:", response)
	except Exception as e:
		print("\t\tan error occured:", e)		#TODO: log function for both console and channel at same time
		response = Format(e)

	return response
#END


# # old and bad getresponse func which relies on an external library that's always broken for some reason
# async def getresponse(input):
# 	try:
# 		print("\t\tgenerating response for:", input)
#
# 		#lingua del messaggio originale
# 		msglanguage = translator.detect(input).lang
# 		print("\t\tmessage received in language:", msglanguage)
#
# 		#dato che il bot è usato in Italiano. in teoria funziona anche per altre lingue
# 		input = translator.translate(input, src=msglanguage).text
# 		print("\t\ttranslated input:", input)
#
# 		#ottiene la risposta
# 		print("\t\t\tgetting p_w...")
# 		async with cleverbotfree.async_playwright() as p_w:
# 			print("\t\t\tgetting c_b...")
# 			c_b = await cleverbotfree.CleverbotAsync(p_w)
# 			print("\t\t\tgetting response...")
# 			response = await c_b.single_exchange(input)
# 			print("\t\t\tclosing c_b...")
# 			await c_b.close()
# 		print("\t\tresponse:", response)
#
# 		if response == "": response = "i couldn't process the question, sorry"
#
# 		#per mantenere continuità, il bot risponde nella stessa lingua in cui gli scrivi
# 		response = translator.translate(response, dest=msglanguage).text
# 		print("\t\ttranslated response:", response)
# 	except Exception as e:
# 		print("\t\tan error occured:", e)
# 		response = Format(e)
#
# 	return response
