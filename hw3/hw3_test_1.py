import unittest
import random
import hw3

class SortTest(unittest.TestCase):
	
	def setup(self):
		pass
	
	def test_merge_sort(self):
		merge_list = hw3.merge_sort(random.sample(xrange(1000000), 1000))
		
		self.assertTrue(merge_list[98] <= merge_list[99])
		self.assertTrue(merge_list[338] <= merge_list[339])
		self.assertTrue(merge_list[498] <= merge_list[499])
		self.assertTrue(merge_list[998] <= merge_list[999])
			
	def test_selection_sort(self):
		selection_list = hw3.selection_sort(random.sample(xrange(1000000), 1000))
		
		self.assertTrue(selection_list[1] <= selection_list[2])
		self.assertTrue(selection_list[44] <= selection_list[45])
		self.assertTrue(selection_list[45] <= selection_list[46])
		self.assertTrue(selection_list[998] <= selection_list[999])
			
	def test_quick_sort(self):
		quick_list = hw3.quick_sort(random.sample(xrange(1000000), 1000))
		
		self.assertTrue(quick_list[1] <= quick_list[2])
		self.assertTrue(quick_list[44] <= quick_list[45])	
		self.assertTrue(quick_list[99] <= quick_list[100])	
		self.assertTrue(quick_list[998] <= quick_list[999])

if __name__ == '__main__':
	unittest.main()