import numpy as np

class InvestmentType():
	def __init__(self, name, value = 0):
		self.name = name
		self.value = value

class Stock(InvestmentType):
	
	def __init__(self, name, value):
		self.name = name
		self.value = value

class MutualFund(InvestmentType):
	
	def __init__(self, name):
		self.name = name
		self.value = 1

class Portfolio(InvestmentType):
	
	def __init__(self, cash_value = 0.0, stock_dict = {}, mf_dict = {}, history_log = []):
		self.cash_value = cash_value
		self.stock_dict = stock_dict
		self.mf_dict = mf_dict
		self.history_log = history_log
	
	def addCash(self, amount_to_add):
		self.cash_value += amount_to_add
		self.history_log.append("A transaction added %r to your account" % amount_to_add)
		return self.cash_value
		
	def withdrawCash(self, amount_to_withdraw):
		self.cash_value -= amount_to_withdraw
		self.history_log.append("A transaction withdrew %r from your account" % amount_to_withdraw)
		return self.cash_value
	
	def buyStock(self, number_of_shares, investment_instance):
		name_of_investment = investment_instance.name
		cost_per_share = investment_instance.value
		
		print "You have bought %d shares of %s stock." % (number_of_shares, name_of_investment)
		print "At %r dollars per share, this has cost you %r dollars." % (cost_per_share, cost_per_share * number_of_shares)
		
		self.cash_value = self.cash_value - (cost_per_share * number_of_shares)
		print "Your liquid value of cash is now %r." % self.cash_value
		
		self.history_log.append("A transaction bought %d shares of %s stock" % (number_of_shares, name_of_investment))
		
		self.stock_dict[name_of_investment] = cost_per_share
		return self.stock_dict
		
	def sellStock(self, name_of_stock, number_of_shares_to_sell):
		value_of_stock = self.stock_dict[name_of_stock]
				
		sell_price = np.random.uniform(0.5* value_of_stock, 1.5* value_of_stock, size = 1)
		sell_price = float("%.1f" % sell_price)
		print "The selling price per unit of %s is %r." % (name_of_stock, sell_price)
		
		self.history_log.append("A transaction sold %d shares of %s stock" % (number_of_shares_to_sell, name_of_stock))

		
		self.cash_value += (sell_price * number_of_shares_to_sell)
	
	def buyMutualFund(self, number_of_shares, investment_instance):
		name_of_investment = investment_instance.name
		cost_per_share = investment_instance.value
		
		print "You have bought %d shares of %s mutual fund." % (number_of_shares, name_of_investment)
		print "At %r dollar per share, this has cost you %r dollars." % (cost_per_share, cost_per_share * number_of_shares)
		
		self.cash_value = self.cash_value - (cost_per_share * number_of_shares)
		print "Your liquid value of cash is now %r." % self.cash_value
		
		self.history_log.append("A transaction bought %d shares of %s mutual fund" % (number_of_shares, name_of_investment))

		
		self.mf_dict[name_of_investment] = number_of_shares
		return self.mf_dict
		
	def sellMutualFund(self, name_of_mf, number_of_shares_to_sell):
		value_of_mf = self.mf_dict[name_of_mf]
				
		sell_price = np.random.uniform(0.9, 1.2, size = 1)
		sell_price = float("%.1f" % sell_price)
		print "The selling price per unit of %s is %r." % (name_of_mf, sell_price)
		
		self.history_log.append("A transaction sold %d shares of %s mutual fund" % (number_of_shares_to_sell, name_of_mf))		
		
		self.cash_value += (sell_price * number_of_shares_to_sell)
		
	def the_print(self):
		print "cash:", self.cash_value
		print "stock:", self.stock_dict
		print "mutual funds:", self.mf_dict
		
	def history(self):
		print self.history_log
		
		
stock1 = Stock("KGB", 2)
portfolio = Portfolio()
portfolio.buyStock(40, stock1)
portfolio.sellStock("KGB", 1)
mf1 = MutualFund("BRT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.sellMutualFund("BRT", 3)
portfolio.the_print()
portfolio.history()

