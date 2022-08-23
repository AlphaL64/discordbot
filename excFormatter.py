import traceback
def Format(e : Exception) -> str:
	return "".join(traceback.format_exception(type(e), e, e.__traceback__))
