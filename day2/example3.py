class Parent():
	def __init__(self, sex, firstname, lastname):
		self.sex = sex
		self.firstname = firstname
		self.lastname = lastname
		self.kids = []
	
	def role(self):
		if self.sex == "Male":
			return "Father"
		else:
			return "Mother"
	
	def have_child(self, name):
		child = Child(self, name)
		print self.firstname, "is having a child named", child.name
		print "They will make a very good", self.role()
		self.kids.append(child)
	
class Child():
	def __init__(self, firstname, parent):
		self.parent = parent
		self.lastname = parent.lastname
		self.firstname = firstname

	def name(self):
		return "%s %s", (self.firstname, self.lastname)

	def introduce(self):
		return "Hi I'm ", name

mom = Parent("Female", "Jane", "Smith")
jill = mom.have_child("Jill")
print jill.introduce()
		
	
#class Child(Parent): # doesn't make sense to inherit from Parent, as not all same as characteristics as Parents
	