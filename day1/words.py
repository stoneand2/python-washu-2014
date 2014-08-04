#file = open('words.txt')

#for line in file:
#  		word = line.strip()
#  		print word
  

def has_no_e(word):
	
	separated_word = list(word)
	
	if 'e' in separated_word:
		print "False"
	else:
		print "True"
		
has_no_e('') 
		