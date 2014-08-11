import numpy as np

class Portfolio(object):
	
	def __init__(self, cash_value = 0.0):
		self.cash_value = cash_value
		self.my_investments = {} # a dict to hold all current investments the user has
		self.history_log = "User's portfolio iniitialized.\n"
	
	def addCash(self, value_to_add):
		self.cash_value += value_to_add
		self.history_log += ("Added $%r to portfolio, now have $%r in portfolio." % (value_to_add, self.cash_value))
		return self.cash_value
	
	def withdrawCash(self, value_to_withdraw):
		self.cash_value -= value_to_withdraw
		self.history_log += ("\nWithdrew $%r from portfolio, now have $%r in portfolio." % (value_to_withdraw, self.cash_value))
		return self.cash_value
	
	def makeInvestment(self, number, what_investment, type = ""):
		if self.cash_value < (number * what_investment.price): # won't let user make an investment if they don't have enough money
			print "Insufficient funds to complete transaction."
			return None
		
		self.cash_value = self.cash_value - (number * what_investment.price)
		self.history_log += ("\nAdded %r shares of %s to portfolio, now have $%r in portfolio." % (number, what_investment.name, self.cash_value))
		
		if type not in self.my_investments:  # adds the investment type (e.g. stocks),  name, and how many to the user's investment dict
			self.my_investments[type] = {} 
			(self.my_investments[type])[what_investment.name] = number
			return dict_of_investments  
		(self.my_investments[type])[what_investment.name] = number # if investment type already in dict, just adds the name and how many
		
	def sellInvestment(self, what_investment, number, bottom = 0.9, top = 1.2, x = 1, type = ""): # default selling values are for the mut. funds
		
		selling_random = np.random.uniform(bottom * x, top * x, size=1)  # uniformly draws the price from range
 		(self.my_investments[type])[what_investment] = float("%.2f" %(((self.my_investments[type])[what_investment]) - number))  # updates the amount of a investment the user has
			
 		self.cash_value = self.cash_value + (number * (selling_random))
		self.cash_value = float("%.2f" % self.cash_value)
		self.history_log += ("\nSold %d shares of %s, now have $%r in portfolio." % (number, what_investment, self.cash_value))
	
	def buyStock(self, number, what_stock, type = "stocks"): # moves up to the more abstract makeInvestment with its stock-specific type information
		self.makeInvestment(number, what_stock, type)
	
	def buyMutualFund(self, number, what_mf, type = "mutual funds"):
		self.makeInvestment(number, what_mf, type)
	
	def buyBond(self, number, what_bond, type = "bonds"):
		self.makeInvestment(number, what_bond, type)
	
	def sellStock(self, what_investment, number):
		self.sellInvestment(what_investment, number, bottom = 0.5, top = 1.5, x = dict_of_investments['stocks'][what_investment], type="stocks") # replaces defined values in sellInvestment with those appropriate for selling stocks
	
	def sellMutualFund(self, what_investment, number):
		self.sellInvestment(what_investment, number, type = "mutual funds")
		
	def sellBond(self, what_investment, number):
		self.sellInvestment(what_investment, number, type = "bonds")
		
	def history(self):
		print self.history_log
	
	def __str__(self):  # the print(portfolio) method
		what_to_print = "cash: $%r \n" % (self.cash_value)
		for type in self.my_investments:
			what_to_print += "%s: " % (type)
			for investment in self.my_investments[type]:
				what_to_print += str((self.my_investments[type][investment])) + " " + str(' '.join(self.my_investments[type])) + "\n"
		return what_to_print

class Investments(object): # a parent class for stocks, mutual funds, bonds

	global dict_of_investments
	dict_of_investments = {} # a dict of all the investment types that have been created

	def __init__(self, price, name, type):
		self.price = price
		self.name = name
		self.type = type
	
	def addToDict(self):
		if self.type not in dict_of_investments:  # adds an investment type (e.g. stocks), investment name and the cost to purchase to the dict
			dict_of_investments[self.type] = {}
			(dict_of_investments[self.type])[self.name] = self.price
			return dict_of_investments
		(dict_of_investments[self.type])[self.name] = self.price # investment type already in the dict, so it just adds the investment name and price
	
class Stock(Investments):
	def __init__(self, price, name, type = "stocks"):
		Investments.__init__(self, price, name, type)
		self.addToDict() 
		
class MutualFund(Investments):
	def __init__(self, name, price = 1, type = "mutual funds"):
		Investments.__init__(self, price, name, type)
		self.addToDict()
		
class Bond(Investments): # introducing bonds isn't hard w/ inheritance, just treat it like stocks and mutual funds. This treats bonds w/ the same rules as mutual funds, but could be altered like for stocks
	def __init__(self, name, price = 1, type = "bonds"):
		Investments.__init__(self, price, name, type)
		self.addToDict()

portfolio = Portfolio()
# portfolio.addCash(300.50)
# s = Stock(20, "HFH")
# portfolio.buyStock(5, s)
# mf1 = MutualFund("BRT")
# mf2 = MutualFund("GHT")
# portfolio.buyMutualFund(10.3, mf1)

