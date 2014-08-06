class School(object):
	

	def __init__(self, name): #initialize the school
		self.name = name
		print name
		
		self.db = {}
	
	def add(self, name, year): # adding a student to the dictionary
		self.name = name
		self.year = year

		self.db.setdefault(self.year, set([]))
		print self.db

school = School("Happy")
school.add("Aimee", 2)