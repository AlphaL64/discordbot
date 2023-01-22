from typing import Callable, Any

#variables
__INDENT_LEVEL  = 0
__INDENT_STRING = "\t"
__OUTPUT_CHANNELS: list[tuple[Callable[[str], Any], str, bool]] = []

#settings
def output_channels_add(function: Callable[[str], Any], indent_str:str=-1, do_indent=True):
	"""
	Adds an output channel.

	All future log messages will be printed via this function as well as all the previously set functions.
	
	`function`:   the function that will be called every time the `log` function is invoked.
	`indent_str`: the string that will be used in indentation; if none is specified, it will use the default.
	`do_indent`:  if false, this output channel will not indent when printing.
	"""
	__OUTPUT_CHANNELS.append((function, (indent_str if indent_str != -1 else __INDENT_STRING), do_indent))
def output_channels_get(index=-1):
	"""Get all output channels, or the one with the given `index` if specified."""
	if index == -1:
		return __OUTPUT_CHANNELS
	else:
		return __OUTPUT_CHANNELS[index]

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

def indent_string_set(new_str: str):
	"""Set the string that will be used when indenting."""
	global __INDENT_STRING
	__INDENT_STRING = str(new_str)
def indent_string_get() -> str:
	"""Get the string being used when indenting."""
	return __INDENT_STRING

# def indent_full_get() -> str:
# 	"""Returns a string with the current amount of indentation, indented using the indentation string."""
# 	return (indent_string_get()) * (indent_level_get())


#END settings

#FUNCS

#TODO: priority system
def log(message: str, do_indent=True):
	"""logs a message to all output channels"""
	for channel in output_channels_get():
		func = channel[0]
		indent_str = channel[1]
		do_indent = (channel[2] and do_indent)

		indentation = (indent_str * indent_level_get()) if do_indent is True else ""
		func(indentation + str(message))
