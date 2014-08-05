class BiologicalThing(object):
	def alive(self):
		return True

class Animal(BiologicalThing):
	def __init__(self, age):
		self.age = age

	def gets_energy_from_the_sun(self):
		return False

class Plant(BiologicalThing):
	def gets_energy_from_the_sun(self):
		return True

class Mammal(Animal):
	def __init__(self, age, sex):
		Animal.__init__(self, age) #go to the superclass and initialize as an Animal, take care of the animal stuff you need to do
		self.sex = sex # but Animal doesn't handle sex, so we will here

	def has_hair(self):
		return True
	
	def has_live_births(self):
		return True	

class Human(Mammal): #class definition, Human inherits from object
	def __init__(self, age, sex, name): #initializer
		Mammal.__init__(self, age, sex)
		self.name = name
	
	def speak(self, words):
		if self.sex=="Male":
			return words.upper()
		else:
			return words
			
	def introduce(self):
		return self.speak("Hello, I'm %s" % self.name)


andy = Human(21, "Male", "Andy")
print andy.introduce()
print andy.gets_energy_from_sun() # goes to Human, no info. Goes to Mammal, no info. Goes to Animal, there's the info
print dir(andy) # lists all methods possible for the andy instance (including those inherited from Object)

betul = Human("impolite to ask", "Female", "Betul")
print betul.introduce()		