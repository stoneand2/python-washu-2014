global big_list   # works with very specific parameters only
global new_list
big_list = []
new_list = list(range(3,122))

def sieve(prime):
		
	big_list.append(prime)
	
	while len(new_list) >= 1:
		big_list.append(prime)
		
		for number in new_list:
			if (number % prime) == 0 and number != prime:
				new_list.remove(number)
				
		next_round_prime = new_list.pop(0)
 		return sieve(next_round_prime)
 	
 	return big_list

print sieve(2)

# trying to make it work with a more relaxed set of assumptions. Unsuccessful so far

# class SieveClass():
# 	
# 	def __init__(self, maximum):
# 		self.maximum = maximum
# 		self.new_list = list(range(2, maximum+1))
# 		self.primes_list = []
# 	
# 	def sieve(self):
# 		
# 		while len(self.new_list) != 0:
# 			working_value = self.new_list[0]
# 	
# 		for number in self.new_list:
# 			if (number % working_value) == 0 and number != working_value:
# 				self.new_list.remove(number)
# 			elif number == working_value:
# 				self.primes_list.append(working_value)
# 				self.new_list.pop(0)
# 		
# 				next_round_working_value = self.new_list.pop(0)
# 		
# 		return self.sieve()
# 		
# 		return self.primes_list
# 			
# call = SieveClass(121)
# print call.sieve()