class Portfolio():
	
	def __init__(self, name, value):
		self.name = name
		self.value = value
	
	def stockinfo(self):
		print self.name, self.value
	
class InvestmentTypes(Portfolio):
	
	def __init__(self, value, name):
		self.value = value
		self.name = name
	
	def secondprint(self, classname):
		classname.stockinfo() # This is portfolio.printtest



portfolio = Portfolio("NKG", 50.0)
# portfolio.printtest()

type1 = InvestmentTypes("v", "Tim")
type1.secondprint(portfolio)
	