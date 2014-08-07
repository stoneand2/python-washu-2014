import unittest
import euclidean_alg

class EuclideanTests(unittest.TestCase):
	
	def setup(self):
		pass
	
	def test_basic(self):
		self.assertEqual("GCD is 4", euclidean_alg.euclidean(8, 4))
	
	def test_reverse(self):
		self.assertEqual("GCD is 4", euclidean_alg.euclidean(4, 8))
		
	def test_complex(self):
		self.assertEqual("GCD is 3", euclidean_alg.euclidean(84, 3))
	
	def test_float(self):
		self.assertEqual("GCD is 3", euclidean_alg.euclidean(84, 3.0))

if __name__ == '__main__': # run the test for us
	unittest.main()	