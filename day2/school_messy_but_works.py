class School(object):

	def __init__(self, name): #initialize the school
		self.name = name		
		self.db = {}
		self.new_dict = {}
	
	def add(self, name, year): # adding a student to the dictionary
		self.db.setdefault(year, set([name])) # adds student to grade key/ set combo
		self.db[year].add(name) #this adds a student to the set if already a duplicate key
		
		# self.new_dict.setdefault(year, []).append(name)
# 		return self.new_dict
		
		
	def grade(self, year_of_school):
		if year_of_school in self.db: # if grade passed in as argument is in the dictionary as a key, returns the students in that grade
			return self.db[year_of_school]
		return None # if no grade as key, returns None

	def sort(self):
		dict_values = self.db.values()  # get the keys too and make a new dictionary
		dict_keys = self.db.keys()
		
		item1 = dict_values.pop()
		item1_list = list(item1)
		item1_list_tuple = tuple(item1_list)
		
		item2 = dict_values.pop()
		item2_list = list(item2)
		item2_list_tuple = tuple(item2_list)
		
		item3 = dict_values.pop()
		item3_list = list(item3)
		item3_list_tuple = tuple(item3_list)
		
		dict_values.append(item3_list_tuple)
		dict_values.append(item2_list_tuple)
		dict_values.append(item1_list_tuple)
				
		self.new_dict = dict(zip(dict_keys, dict_values))
		return self.new_dict