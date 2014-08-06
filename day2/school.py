class School(object):
	

	def __init__(self, name): #initialize the school
		self.name = name
		print name
		
		self.db = {}
	
	def add(self, name, year): # adding a student to the dictionary
		self.name = name
		self.year = year

		self.db.setdefault(self.year, []) #need to make a set
		self.db[self.year].append(self.name) #can't append to set
		
		return self.db
		
	def grade(self, year_of_school):
		self.year_of_school = year_of_school
		
		if self.year_of_school in self.db:
			return self.db[self.year_of_school]
# don't need. de-dent and just have return None
		return None
"""
	def sort(self):
		print sorted(self.class_dictionary.items())
"""		
		

