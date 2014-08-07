import unittest
import bob_lab

class BobTest(unittest.TestCase):
	
	def setup(self): # this will run before each of our tests
		pass
	
	def test_question(self):
		self.assertEqual("Sure.", bob_lab.response("How are you?"))
		self.assertEqual("Sure.", bob_lab.response("HOW ARE YOU?"))
	
	def test_yell(self):
		self.assertEqual("Woah, chill out!", bob_lab.response("HOW COULD YOU!"))
		self.assertEqual("Woah, chill out!", bob_lab.response("HOW COULD YOU"))

		
	def test_say_nothing(self):
		self.assertEqual("Fine. Be that way!", bob_lab.response(""))
	
	def test_anything_else(self):
		self.assertEqual("Whatever.", bob_lab.response("This is something else."))
		self.assertEqual("Whatever.", bob_lab.response("This is something else!"))
		self.assertEqual("Whatever.", bob_lab.response("112"))
		
if __name__ == '__main__': # run the test for us
	unittest.main()	