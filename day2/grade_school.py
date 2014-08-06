class School(object):
	
	class_dictionary = {}

	def __init__(self, name): #initialize the school
		self.name = name
		print name
	
	def add(self, name, year): # adding a student to the dictionary
		self.name = name
		self.year = year

		self.class_dictionary.setdefault(self.year, [])
		self.class_dictionary[self.year].append(self.name)
		
		return self.class_dictionary
		
	def db(self): # the dictionary for the school
		return self.class_dictionary
		
	def grade(self, year_of_school):
		self.year_of_school = year_of_school
		
		if self.year_of_school in self.class_dictionary:
			print self.class_dictionary[self.year_of_school]
		else:
			print None
"""	
	def sort(self):
		print self.class_dictionary.sorted()
"""
		
		
"""		
		namelist = []
		
		if self.grade in self.class_dictionary:
			self.class_dictionary[self.name].append(self.)
		else:
			self.class_dictionary[self.grade] = self.name
		
		if self.grade in self.class_dictionary:
			self.class_dictionary[self.grade].append(self.grade)
		else:
			self.class_dictionary[self.grade] = self.name
			
		self.class_dictionary[self.grade] = [self.name]
		
		print self.class_dictionary
"""	
		
		
	
school = School("Haleakala Hippy School")
school.db()
school.sort()