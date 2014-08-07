def euclidean(number1, number2):	
	
	q = (number1/number2)
	r = number1 % number2
	
	if r == 0:
		return "GCD is %d" % number2
	return euclidean(number2, r)

