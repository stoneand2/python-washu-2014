def sqrt(number, guess):
	new_guess = guess - ((guess**2 - number)/(2 * guess))
	return new_guess
	
def find_sqrt(number, guess, desired_precision=.001, max_steps=100):
	guess = float(guess)
	number = float(number)
		
	current_precision = 1
	steps = 0
	
	while (current_precision > desired_precision) and (steps < max_steps):
		 new_guess = sqrt(number, guess)
		 current_precision = abs(new_guess - guess)
		 print "Step {0}: Current guess is {1} and precision is {2}".format(
		 	steps, new_guess, current_precision
		 )
		 guess = new_guess
		 steps += 1
	return guess

find_sqrt(422, 25)
