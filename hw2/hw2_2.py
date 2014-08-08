class Stock():
	
	def __init__(self, name, value):
		self.name = name
		self.value = value
	
	def printname(self):
		print self.name
	

class Portfolio(Stock):
	
	def __init__(self, cash_value = 0.0):
		self.cash_value = cash_value
	
	def what_will_change(self, number, stockname):
		stockname.printname()
		
stock1 = Stock("KGB", 2)
portfolio = Portfolio()
portfolio.what_will_change(2, stock1)