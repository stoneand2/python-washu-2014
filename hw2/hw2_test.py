import unittest
import hw2_4

class PortfolioTest(unittest.TestCase):
	
	def setup(self): # this will run before each test
		pass
	
	def test_addCash(self):  # tests if the portfolio adds cash correctly
		self.assertEqual(300.50, hw2_4.portfolio.addCash(300.50))
	
	def test_createStock(self):  # tests if a stock can be added to the investments dict
		s = hw2_4.Stock(20, "HFH")
		self.assertTrue("stocks" in hw2_4.dict_of_investments)
		self.assertTrue("HFH" in hw2_4.dict_of_investments["stocks"])
	
	def test_createMutualFund(self):
		mf1 = hw2_4.MutualFund("BRT")
		self.assertTrue("mutual funds" in hw2_4.dict_of_investments)
		self.assertTrue("BRT" in hw2_4.dict_of_investments["mutual funds"])
	
	def test_createBond(self):
		bond1 = hw2_4.Bond("XYZ")
		self.assertTrue("bonds" in hw2_4.dict_of_investments)
		self.assertTrue("XYZ" in hw2_4.dict_of_investments["bonds"])
		
	def test_buyStock(self):  # tests if a stock can be purchased and added to the portfolio my_investments dict
		hw2_4.portfolio.buyStock(5, hw2_4.Stock(20, "HFH"))
		self.assertTrue("stocks" in hw2_4.portfolio.my_investments)
		self.assertTrue("HFH" in hw2_4.portfolio.my_investments["stocks"])
		self.assertEqual(5, hw2_4.portfolio.my_investments["stocks"]["HFH"])
		
	def test_buyMutualFund(self):
		hw2_4.portfolio.buyMutualFund(10.3, hw2_4.MutualFund("BRT"))
		self.assertTrue("mutual funds" in hw2_4.portfolio.my_investments)
		self.assertTrue("BRT" in hw2_4.portfolio.my_investments["mutual funds"])
		self.assertEqual(10.3, hw2_4.portfolio.my_investments["mutual funds"]["BRT"])
	
	def test_buyBond(self):
		hw2_4.portfolio.buyBond(11, hw2_4.Bond("XYZ"))
		self.assertTrue("bonds" in hw2_4.portfolio.my_investments)
		self.assertTrue("XYZ" in hw2_4.portfolio.my_investments["bonds"])
		self.assertEqual(11, hw2_4.portfolio.my_investments["bonds"]["XYZ"])

	def test_sellStock(self):  # tests if the correct amount of stock can be removed from the my_investments dict
		hw2_4.portfolio.sellStock("HFH", 2)
		self.assertEqual(3, hw2_4.portfolio.my_investments["stocks"]["HFH"])
		
	def test_sellMutualFund(self):
		hw2_4.portfolio.sellMutualFund("BRT", 3)
		self.assertEqual(7.3, hw2_4.portfolio.my_investments["mutual funds"]["BRT"])
		
	def test_sellBond(self):
		hw2_4.portfolio.sellBond("XYZ", 7)
		self.assertEqual(4, hw2_4.portfolio.my_investments["bonds"]["XYZ"])
		
	def test_printPortfolio(self): # tests if the print command works
		self.assertTrue("cash: " in hw2_4.portfolio.__str__())
		self.assertTrue("stocks: " in hw2_4.portfolio.__str__())
		self.assertTrue("mutual funds: " in hw2_4.portfolio.__str__())
		self.assertTrue("bonds: " in hw2_4.portfolio.__str__())
		self.assertTrue("HFH" in hw2_4.portfolio.__str__())
		self.assertTrue("BRT" in hw2_4.portfolio.__str__())
		self.assertTrue("XYZ" in hw2_4.portfolio.__str__())
		
	def test_history(self): # tests if the history log compiles the correct log of transactions
		log = hw2_4.portfolio.history_log
		self.assertTrue("Added" in log)
		self.assertTrue("initialized" in log)
		self.assertTrue("Insufficient funds" not in log)
			
	def test_withdrawCash(self): # tests if the portfolio withdraws cash correctly
 		self.assertEqual((hw2_4.portfolio.cash_value - 50), hw2_4.portfolio.withdrawCash(50))
	
if __name__ == '__main__': # runs the tests for us
	unittest.main()	