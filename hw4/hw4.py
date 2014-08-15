class Node:
	def __init__(self, _value=None, _next=None):
		self.value = _value
		self.next = _next 
	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self, value):						# this is O(constant?)
		self.head = Node(value)						# self.head will remain the initialized value
		self.how_long = 1							# length counter
	
	def addNode(self, new_node):					# this is O(n?)
		new_node = Node(new_node)					# preserves the new node's next value as None
		holder = self.head							# the holder starts out at the initialized head value
		while holder.next is not None:				# while the pointer of the holder doesn't point to None
			holder = holder.next					# make the holder the next node in the list
		holder.next = new_node						# after reaching final node, make the next value the new node we add at the end
		self.how_long += 1
	
	def addNodeAfter(self, new_node, after_node):	# this is O(n) at worst case
		holder = self.head							# makes the holder start at the head value
		while str(holder) != str(after_node):		# as long as we haven't reached the after node yet
			if holder is None:						# if node you want to insert after isn't in list
				print "Node to insert after isn't in list."
				return None
			holder = holder.next 					# progress to the next node
		holder.next = Node(new_node, holder.next) 	# when reaching the after node, make the after value point to new node, 
													# which then points to the old next node from the after node
		self.how_long += 1
		
	def addNodeBefore(self, new_node, before_node):	# this is O(n) at worst case
		holder = self.head							# makes the holder start at the head value
		current = holder							# need for case when you want to add before head node
		while str(holder) != str(before_node): 		# as long as not at node want to replace before
			if holder.next is None:					# if node you want to replace before isn't in list
				print "Node to insert before isn't in list."
				return None
			current = holder
			holder = holder.next
		if holder == self.head:							# if you want to add before the head node
			holder = Node(new_node, current)
			self.head = holder
			self.how_long += 1
			return self.head
		current.next = Node(new_node, current.next)		# otherwise, links old node before w/ new node, which links to the holder
		self.how_long += 1
			
	def __str__(self):										# this is O(n)
		what_to_print = "Your linked list: "				# printing done string format
		holder = self.head					
		what_to_print += str(holder)						# makes the printing start at the head value
 		while holder.next is not None:						# keeps printing until last value
 			what_to_print += ", " + str(holder.next)
 			holder = holder.next
 		return what_to_print
	
	def removeNode(self, node_to_remove):					# this is O(constant?)
		holder = self.head
		if (str(node_to_remove)==str(holder)) and holder.next is None: # doesn't allow making the list empty
			return "Can't remove this node--list would be empty."
		if str(node_to_remove) == str(holder):				# if want to remove head node
 			holder = Node(holder.next, holder.next.next)	# make second node new head 
 			self.head = holder
 			self.how_long -= 1
 			return holder
		
		while str(holder.next) != str(node_to_remove):		
			if holder.next is None:									# if what you want to remove isn't in list
				return "Node to remove isn't in list!"
			holder = holder.next
		holder.next = holder.next.next								# jumps over removed value
		self.how_long -= 1
	
	def removeNodesByValue(self, value):							# this is O(a lot0)
		holder = self.head
		if (str(value)==str(holder)) and (holder.next is None):		# doesn't allow making the list empty
			return "Can't remove this node--list would be empty."		
		elif str(value) == str(holder):								# if want to remove head node
			holder = Node(holder.next, holder.next.next)			# make second node new head
			self.head = holder
			self.how_long -= 1
			return self.removeNodesByValue(value)					# recursive (to check for other nodes of same value)
		while str(holder.next) != str(value):						# while not at node you want to replace
			if holder.next is None:									# if at end
				return "All of the '%s' nodes are removed!" % (value)
			holder = holder.next
		holder.next = holder.next.next								# jump over removed value
		self.how_long -= 1
		self.removeNodesByValue(value)								# recursive
	
	def reverse(self):								# this is O(n). best possible i can think of
		holder = self.head							# start at head
		temporary = holder							# holds current node to be switched
		holder = Node(temporary)					# replace old holder w/ new node (like starting a new list)
		
		while temporary.next is not None:			# as long as not at end
			temporary = temporary.next				# move to next node to be switched
			holder = Node(temporary, holder)		# replace holder w/ new node to be switched & link it
		self.head = holder							# make final node new head node
		return holder
	
	def length(self):								# this is O(constant), best possible
		return self.how_long
	
# instance = LinkedList(4)
# instance.addNode(11)
# instance.addNode(11)
# instance.addNode(400)
# instance.addNodeAfter(12, 4)
# instance.addNodeBefore(222, 4)
# instance.removeNode(4)
# instance.removeNodesByValue(11)
# instance.reverse()
# print(instance)
# print "Your list is", instance.length(), "node(s) long."




