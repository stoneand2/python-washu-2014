def ordinal(n): # handle 0-100
	negative = False
	try: # try to do whatever is in this block. if an exception gets raised, do something else
		n = int(n)	
	except:
		return "Improper input"
	
	if n < 0:
		n = abs(n)
		negative = True
	
	last_digit = n % 10
	second_to_last_digit = n % 100 / 10 
		
	endings = {1 : "st", 2 : "nd", 3 : "rd"}
	
	if second_to_last_digit == 1:
		ending = "th"
	elif last_digit in endings.keys():
		ending = endings[last_digit]
	else:
		ending = "th"
	if negative == True:
		n = -n
	
	return str(n) + ending
	
