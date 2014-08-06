class School(object):

	def __init__(self, name): #initialize the school
		self.name = name		
		self.db = {}
	
	def add(self, name, year): # adding a student to the dictionary
		self.name = name
		self.year = year

		self.db.setdefault(self.year, set([self.name])) # adds student to grade key/ set combo
		self.db[self.year].add(self.name) #this adds a student to the set if already a duplicate key
		
		return self.db 
		
	def grade(self, year_of_school):
		self.year_of_school = year_of_school
		
		if self.year_of_school in self.db: # if grade passed in as argument is in the dictionary as a key, returns the students in that grade
			return self.db[self.year_of_school]
		return None # if no grade as key, returns None
"""
	def sort(self):
		print sorted(self.class_dictionary.items())
"""		
		
school = School('Happy School')
print school.add("James", 2)
print school.add("Blair", 2)
print school.add("Paul", 2)