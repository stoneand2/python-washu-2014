import unittest
from hw4 import LinkedList

class LinkedListTest(unittest.TestCase):
	
	def setUp(self): # this will run before each test
		self.instance = LinkedList(4)
		
	def test_init(self):
		self.assertEqual(1, self.instance.how_long)
		self.assertEqual(4, self.instance.head.value)
		self.assertEqual(None, self.instance.head.next)
 	
 	def test_length(self):
 		self.assertEqual(1, self.instance.length())
 	
	def test_add_node(self):
		self.instance.addNode(7)
		self.assertEqual("Your linked list: 4, 7", self.instance.__str__())
		self.assertEqual(2, self.instance.length())
		
	def test_add_after_node(self):
		self.instance.addNode(7)
		self.instance.addNodeAfter(9, 7)
		self.assertEqual("Your linked list: 4, 7, 9", self.instance.__str__())
		self.assertEqual(3, self.instance.length())
		self.assertEqual(None, self.instance.addNodeAfter(2, 55))
	
	def test_add_before_node(self):
		self.instance.addNode(7)
		self.instance.addNodeBefore(2, 7)
		self.assertEqual("Your linked list: 4, 2, 7", self.instance.__str__())
		self.assertEqual(3, self.instance.length())
		self.instance.addNodeBefore(1, 4)
		self.assertEqual("Your linked list: 1, 4, 2, 7", self.instance.__str__())
		self.assertEqual(4, self.instance.length())
		self.assertEqual(None, self.instance.addNodeBefore(2, 100))
		
	def test_remove_single(self):
		self.instance.addNode(7)
		self.instance.removeNode(4)
		self.assertEqual("Your linked list: 7", self.instance.__str__())
		self.assertEqual(1, self.instance.length())
		self.instance.addNode(7)
		self.instance.addNode(7)
		self.instance.addNode(7)
		self.instance.removeNode(7)
		self.assertEqual("Your linked list: 7, 7, 7", self.instance.__str__())
	
	def test_remove_single_edge_cases(self):
		self.assertEqual("Can't remove this node--list would be empty.", self.instance.removeNode(4))
		self.assertEqual("Node to remove isn't in list!", self.instance.removeNode(11))
		
	def test_remove_all_value(self):
		self.instance.addNode(7)
		self.instance.addNode(7)
		self.instance.addNode(7)
		self.assertEqual("Your linked list: 4, 7, 7, 7", self.instance.__str__())
		self.instance.removeNodesByValue(7)
		self.assertEqual("Your linked list: 4", self.instance.__str__())
		self.instance.addNode(4)
		self.instance.addNode(7)
		self.instance.addNode(7)
		self.instance.removeNodesByValue(4)
		self.assertEqual("Your linked list: 7, 7", self.instance.__str__())
		
	def test_remove_all_value_edge_cases(self):
		self.assertEqual("Can't remove this node--list would be empty.", self.instance.removeNodesByValue(4))
		self.assertEqual("Your linked list: 4", self.instance.__str__())
		self.assertEqual("All of the '11' nodes are removed!", self.instance.removeNodesByValue(11))

	def test_reverse(self):
		self.instance.addNode(7)
		self.instance.addNode(11)
		self.instance.addNode(99)
		self.assertEqual("Your linked list: 4, 7, 11, 99", self.instance.__str__())
		self.instance.reverse()
		self.assertEqual("Your linked list: 99, 11, 7, 4", self.instance.__str__())
	
	def test_reverse_edge_case(self):
		self.assertEqual("Your linked list: 4", self.instance.__str__())
		self.instance.reverse()
		self.assertEqual("Your linked list: 4", self.instance.__str__())

if __name__ == '__main__': # runs the tests for us
	unittest.main()	