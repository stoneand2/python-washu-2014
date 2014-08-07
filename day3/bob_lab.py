def response(speak):
	
	if "?" in speak:
		return "Sure."
	elif speak == speak.upper() and len(speak) != 0: # could be 'if' cause the previous one returns so it breaks anyways
		return "Woah, chill out!"
	elif speak == "":
		return "Fine. Be that way!"
	else:
		return "Whatever."

