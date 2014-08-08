class Portfolio():
	
	def __init__(self, cash_level = 0.00):
		self.cash_level = cash_level
		self.stocks_dict = {}
		self.mutualfunds_dict = {}
	
	def addCash(self, value_to_add):
		self.cash_level += value_to_add
		return self.cash_level
	
	def buyStock(self, number_of_shares, type_of_stock):
		return type_of_stock

class Stock():
	
	def __init__(self, price, ticker_symbol):
		self.price = price
		self.ticker_symbol = ticker_symbol
	
	def info_print(self):
		print "The stock % s has a price of %d." % (self.ticker_symbol, self.price)

portfolio = Portfolio()
print portfolio.addCash(300.50)

s = Stock(20, "HFH")
s.info_print()

print portfolio.buyStock(5, s)



