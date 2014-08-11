import numpy as np

stock_dict = {}
stock_dict["KGB"] = 2
print stock_dict

def sellStock(name_of_stock, number_of_shares_to_sell):
	value_of_stock = stock_dict[name_of_stock]
	print value_of_stock
	
 	sell_price = np.random.uniform(0.5* value_of_stock, 1.5* value_of_stock, size = 1)
	sell_price = "%.1f" % sell_price
	print sell_price


sellStock("KGB", 1)