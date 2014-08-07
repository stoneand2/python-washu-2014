class School(object):

	def __init__(self, name): #initialize the school
		self.name = name		
		self.db = {}
		self.new_dict = {}
	
	def add(self, name, year): # adding a student to the dictionary
		self.db.setdefault(year, set([name])) # adds student to grade key/ set combo
		self.db[year].add(name) #this adds a student to the set if already a duplicate key
		
	def grade(self, year_of_school):
		if year_of_school in self.db: # if grade passed in as argument is in the dictionary as a key, returns the students in that grade
			return self.db[year_of_school]
		return None # if no grade as key, returns None

	def sort(self):
		dict_values = self.db.values()
		dict_keys = self.db.keys()
		new_list = []
		
		x = [2,1,0]	
		
		for x in dict_values:
			what_to_append = tuple(list(dict_values.pop()))
			new_list.append(what_to_append)
			print new_list
		
		dict_values = tuple(new_list)
		
		self.new_dict = dict(zip(dict_keys, dict_values))
 		return self.new_dict

# 		
# 		
# 		item1_list_tuple = tuple(item1_list)
# 			
# 		dict_values.append(item1_list_tuple)
# 		
# 		return dict_values
			
		
# 		item1 = dict_values.pop()
# 		item1_list = list(item1)
# 		item1_list_tuple = tuple(item1_list)
# 		
# 		item2 = dict_values.pop()
# 		item2_list = list(item2)
# 		item2_list_tuple = tuple(item2_list)
# 		
# 		item3 = dict_values.pop()
# 		item3_list = list(item3)
# 		item3_list_tuple = tuple(item3_list)
# 		
# 		dict_values.append(item3_list_tuple)
# 		dict_values.append(item2_list_tuple)
# 		dict_values.append(item1_list_tuple)
# 				
# 		self.new_dict = dict(zip(dict_keys, dict_values))
# 		return self.new_dict

			
school = School('Happy School')
school.add("Jennifer", 4)
school.add("Kareem", 6)
school.add("Christopher", 4)
school.add("Kyle", 3)
print school.sort()