class ID10T_Exception(Exception):
	pass

def er() -> str:
	ERROR_MSGS = [
		"ERROR: NullReferenceException: 'brain' was null",
		"Error 404 (Neurons not found)",
		"IIE - Intelligence Interface Exception: no intelligence was found",
		"PICNIC error: Problem In Chair Not In Computer",
		"DKO error: Defective Keyboard Operator",
		"LAYER 8 ISSUE: BIOLOGICAL INTERFACE ERROR",
		"ID-10-T ERROR: NO FURTHER DETAILS GIVEN",
	]

	import random
	import time
	random.seed(time.time())

	return random.choice(ERROR_MSGS)