
def replace(original, find, replace):
	return original[:original.index(find)] + replace + original[original.index(find) + len(find):]
