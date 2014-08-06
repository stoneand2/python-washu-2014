"""def reversewords1(txt):
  if isinstance(txt, str) == False:
    return ""
  
  new_text = ""
  reversed_sentences = []
    
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(". ")
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  
  last_sentence = sentences[len(sentences) - 1]
  if last_sentence[len(last_sentence) - 1] == ".":
    sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
  
  for sentence in sentences:
    words = sentence.split()
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      new_text = "." + new_text
    
  return new_text
"""  
  
def reversewords(txt):
	if isinstance(txt, str) == False:
		return ""
	
	existing_punctuation = ["!", ".", "?"]
	for punctuation in existing_punctuation:
		if punctuation in txt:
			remember = punctuation
		else:
			pass
	new_txt = txt.replace(remember, " ")
	new_txt = new_txt.split()
	new_txt = ' '.join(new_txt[::-1])
	return remember + new_txt

print reversewords("The string?")