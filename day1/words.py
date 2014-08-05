#file = open('words.txt')

# for line in file:
#	word = line.strip()
#	for letter in word:
#		print letter
		
#def has_no_e(word):
#	return "e" not in word

def has_no_e(word):
#	list_word = list(word) # print list_word to check it made a list
	
#	if 'e' in list_word:
#		return False
#	else:
#		return True

	if 'e' in word:
		return False
	else:
		return True

def uses_only(string, allowed_letters):

	for any_letter in string:
		if not any_letter in allowed_letters:
			return False
	return True

def uses_all(string, all_letters):
	
	for any_letter in all_letters:
		if not any_letter in string:
			return False
	return True
	
def is_abecedarian(letter_combo):
	
	sorted_letters = sorted(letter_combo)
	print sorted_letters
	
	rejoined_letters = "".join(sorted_letters)
	print rejoined_letters
	
	if rejoined_letters == letter_combo:
		return True
	else:	
		return False


is_abecedarian('xxyz')












#def uses_only(word, available):
#	for letter in word:
#		if not letter in available:
#			return False
#	return True
	
	
##	
	

