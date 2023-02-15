from typing import Callable, Any

class output_channel:
	def __init__(self, function: Callable[[str], Any], priority_threshold: int = 0, indent_str: str = -1, do_indent: bool = True) -> None:
		self.function = function
		self.indent_str = indent_str if isinstance(indent_str, str) else "\t"
		self.do_indent = do_indent
		self.priority_threshold = priority_threshold

	function: Callable[[str], Any]
	indent_str: str
	do_indent: bool
	priority_threshold: int

	async def output_async(self, message, do_indent, priority):
		if priority < self.priority_threshold:
			return

		indentation = (self.indent_str * indent_level_get()) if (self.do_indent or do_indent) else ""
		message = indentation + str(message)

		from asyncio import iscoroutinefunction
		if iscoroutinefunction(self.function):
			await self.function(message)
		else:
			self.function(message)
#END

#variables
__INDENT_LEVEL  = 0
# __INDENT_STRING = "\t"
__OUTPUT_CHANNELS: list[output_channel] = []

#settings
def output_channels_add(channel: output_channel):
	"""
	Adds an output channel.

	All future log messages will be printed via this function as well as all the previously set functions.
	"""
	__OUTPUT_CHANNELS.append(channel)
def output_channels_get() -> list[output_channel]:
	"""Get all output channels."""
	return __OUTPUT_CHANNELS

def indent_level_push(n=1):
	"""Adds one level of indentation, or `n` levels if `n` is specified."""
	global __INDENT_LEVEL
	__INDENT_LEVEL += n
def indent_level_pop(n=1):
	"""Removes one level of indentation, or `n` levels if `n` is specified."""
	global __INDENT_LEVEL
	if __INDENT_LEVEL < n:
		raise Exception("can't decrease the indentation level to less than zero")
	__INDENT_LEVEL -= n
def indent_level_reset():
	"""Sets the indent level to zero."""
	global __INDENT_LEVEL
	__INDENT_LEVEL = 0
def indent_level_get() -> int:
	"""Get the current indentation level"""
	return __INDENT_LEVEL

# def indent_string_set(new_str: str):
# 	"""Set the string that will be used when indenting."""
# 	global __INDENT_STRING
# 	__INDENT_STRING = str(new_str)
# def indent_string_get() -> str:
# 	"""Get the string being used when indenting."""
# 	return __INDENT_STRING

# def indent_full_get() -> str:
# 	"""Returns a string with the current amount of indentation, indented using the indentation string."""
# 	return (indent_string_get()) * (indent_level_get())


#END settings

#FUNCS

#TODO: better priority system
async def log_async(message: str, priority: int = 0, do_indent=True):
	"""logs a message to all output channels"""
	for channel in output_channels_get():
		try:
			await channel.output_async(message, do_indent, priority)
		except Exception as e:
			print("errr")
		
