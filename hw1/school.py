class School(object):

	def __init__(self, name): 					
		self.name = name		
		self.db = {}  							# a blank dictionary
		self.new_dict = {}  					# a blank dictionary to be used for sorting (test 7)
	
	def add(self, name, year): 					
		self.db.setdefault(year, set([name])) 	# sets a student to key/ value combo (where the value is a set-type datastructure)
		self.db[year].add(name) 				# if grade already exists, adds the student to the set with that key
		
	def grade(self, year_of_school):
		if year_of_school in self.db: 			# if the grade passed in as argument exists in the dictionary as a key, returns the students in that grade (the values of the dictionary corresponding to that key)
			return self.db[year_of_school]
		return None 							# if the grade passed isn't a key in the dictionary, returns None

	def sort(self):
		dict_values = self.db.values()  		# access the values of the existing db dictionary
		dict_keys = self.db.keys()				# access the keys of the existing db dictionary
		new_list = []							# a blank list to store the values when changed from set to tuples
		length_values = len(dict_values)		# how many values there are at the beginning, so when popping below all values will be popped off
		
		for i in range(length_values):							
			what_to_append = tuple(list(dict_values.pop()))		# pops the last value from dict_values, makes it a list, makes the list a tuple
			new_list.append(what_to_append)		# appends the new tuples to a list

		new_list.reverse()						# in line 25 tuples get appended in reverse order to the list from where they initially were, so this fixes them
		
		dict_values = new_list					# overwrites dict_values to be the newly tupled values
		
		self.new_dict = dict(zip(dict_keys, dict_values))		# makes the new dictionary from the existing keys and new tuple values
 		return self.new_dict					# returns the new sorted dictionary