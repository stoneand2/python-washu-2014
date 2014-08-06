import unittest
import lab3

class Lab3Test(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_shout(self):
		self.assertEqual("I'M FULL!", lab3.shout("i'm full."))
	
	def test_another_shout(self):
		self.assertEqual("TRY MY BURGER!", lab3.shout("Try my burger?"))
		
	def test_third_shout(self):
		self.assertEqual("NOT ALL CAPS!!!", lab3.shout("nOt aLL caps..."))
	
	def test_reverse(self):
		self.assertEqual("I'm full.", lab3.reverse(".lluf m'I"))
		
	def test_another_reverse(self):
		self.assertEqual(".sdrawkcab etirw ot ;drah s'tI", lab3.reverse("It's hard; to write backwards."))

	def test_reversewords(self):
		self.assertEqual(".full I'm", lab3.reversewords("I'm full."))

	def test_reverse_word_letters(self):
		self.assertEqual("m'I lluf.", lab3.reversewordletters("I'm full."))
	
	def test_piglatin(self):
		self.assertEqual("esttay", lab3.piglatin("test"))
		
if __name__ == '__main__': # run the test for us
	unittest.main()	