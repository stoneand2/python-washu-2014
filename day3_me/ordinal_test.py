import unittest
import ordinal

class OrdinalTest(unittest.TestCase):
	
	def setup(self): # this will run before each of our tests
		pass
	
	def test_zero(self):
		self.assertEqual("0th", ordinal.ordinal(0))
	
	def test_first(self):
		
		# assert equal to name of method within our ordinal script 
		#(two ordinals). When give input 1, expect output first
		
		self.assertEqual("1st", ordinal.ordinal(1)) 
	
	def test_second(self):
		
		self.assertEqual("2nd", ordinal.ordinal(2))
	
	def test_third(self):
		
		self.assertEqual("3rd", ordinal.ordinal(3))
	
	def test_fourth(self):
		
		self.assertEqual("4th", ordinal.ordinal(4))
		
	def test_eleventh(self):
		
		self.assertEqual("11th", ordinal.ordinal(11))
	
	def test_twelfth(self):
		self.assertEqual("12th", ordinal.ordinal(12))
	
	def test_one_thousand_and_two(self):
		self.assertEqual("1002nd", ordinal.ordinal(1002))
	
	def test_negative_one(self):
		self.assertEqual("-1st", ordinal.ordinal(-1))
	
	def test_decimal(self):
		self.assertEqual("1st", ordinal.ordinal(1.0))
		
	def test_bad_string_input(self):
		self.assertEqual("Improper input", ordinal.ordinal("1 2"))
		self.assertEqual("Improper input", ordinal.ordinal("abc"))
		self.assertEqual("Improper input", ordinal.ordinal("1*2"))

if __name__ == '__main__': # run the test for us
	unittest.main()		