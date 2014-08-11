import numpy as np

class InvestmentType(object):
	global hist_log, items_dict
	hist_log = []
	items_dict = {}
	
	def __init__(self):
		pass
		
 	def selling(self, name, number, type):
 		if type == "Stock":
 			
 			sell_price = np.random.uniform(0.5 * items_dict[name], 1.5 * items_dict[name], size = 1)
 			sell_price = float("%.2f" % sell_price)
 			
 			self.cash_value += (sell_price * number)
 			self.cash_value = float("%.2f" % self.cash_value)
 			hist_log.append("Sold %r shares of %s stock at %r per share. Account balance: %r" % (number, name, sell_price, self.cash_value))
 		
 		else:
 			sell_price = np.random.uniform(0.9, 1.2, size = 1)
			sell_price = float("%.2f" % sell_price)
			
			self.cash_value += (sell_price * number)
			self.cash_value = float("%.2f" % self.cash_value)
			hist_log.append("Sold %r shares of %s mutual fund at %r per share. Account balance: %r" % (number, name, sell_price, self.cash_value))
	
	def history_log(self, string_to_add):
		hist_log.append(string_to_add)
	
	def history(self):
		print hist_log
	
	def items_dictionary(self, investment_name, cost):
		items_dict[investment_name] = cost
		
	def stringing(self):
		print self.cash_value
	
class Stock(InvestmentType):
	def __init__(self, value, name):
		self.name = name
		self.value = value		

class MutualFund(InvestmentType):
	def __init__(self, name):
		self.name = name
		self.value = 1

class Transactions(InvestmentType):
	def __init__(self, cash_value):
		self.cash_value = cash_value
		
	def addCash(self, value_to_add):
		self.cash_value += value_to_add
		super(Transactions, self).history_log("Added %r dollars. Account balance: %r" % (value_to_add, self.cash_value))
		
	def withdrawCash(self, value_to_withdraw):
		self.cash_value -= value_to_withdraw
		super(Transactions, self).history_log("Withdrew %r dollars. Account balance: %r" % (value_to_withdraw, self.cash_value))
	
	def addInvestment(self, number_of_shares, investment_instance):
		self.cash_value -= (investment_instance.value * number_of_shares)
		super(Transactions, self).history_log("Added %r shares of %s. Account balance: %r" % (number_of_shares, investment_instance.name, self.cash_value))
		super(Transactions, self).items_dictionary(investment_instance.name, investment_instance.value)

	def sellInvestment(self, investment_instance, number_of_shares, type):		
		super(Transactions, self).selling(investment_instance, number_of_shares, type)
	
	def string(self):
		super(Transactions, self).stringing()

class Portfolio(Transactions):
	def __init__(self):
		self.cash_value = 0.0
			
	def buyStock(self, number_of_shares, investment_instance):
		super(Portfolio, self).addInvestment(number_of_shares, investment_instance)
		
	def buyMutualFund(self, number_of_shares, investment_instance):
		super(Portfolio, self).addInvestment(number_of_shares, investment_instance)
		
	def sellStock(self, investment_instance, number_of_shares, type = "Stock"):
		super(Portfolio, self).sellInvestment(investment_instance, number_of_shares, type)
	
	def sellMutualFund(self, investment_instance, number_of_shares, type = "Mutual Fund"):
		super(Portfolio, self).sellInvestment(investment_instance, number_of_shares, type)
	
	def __str__(self):
		super(Portfolio, self).string()
	
	
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
portfolio.history()
print(portfolio)