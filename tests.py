import os
import unittest

from oplab import Client
c = Client()
c.login(os.environ['USER'], os.environ['PASSWORD'])
# getting orders
class TestOrderMethods(unittest.TestCase):

    def test_get_portfolio_orders(self):
        """
        Portfolio orders should return an array
        """
        orders = c.get_portfolio_orders(14915)
        self.assertIsInstance(orders, list)

class TestHistoricalDataMethods(unittest.TestCase):

    def test_get_historical_data(self):
        """
        Should return last 252 days of historical data
        """
        data = c.get_historical_data('PETR4', 252)
        self.assertEqual(len(data['data']), 252)

class TestOrderMethods(unittest.TestCase):
    def test_create_order(self):
        """
        Should return a newly created order with the same symbol
        """
        created_order = c.create_order({'symbol': 'PETR4', 'price': 20, 'amount': 100, 'direction': 'buy', 'order_type': 'test', 'status': 'executed' }, 14915)
        self.assertEqual(created_order['symbol'], 'PETR4' ) 

class TestPortfoliosMethods(unittest.TestCase):

    def test_get_portfolios(self):
        """
        Should return an array of portfolios
        """
        portfolios = c.get_portfolios()
        self.assertIsInstance(portfolios, list)
    
    def test_get_portfolio(self):
        """
        Should return a portfolio
        """
        portfolios = c.get_portfolios()
        portfolio_id = portfolios[0]['id']
        portfolio = c.get_portfolio(portfolio_id)
        print(portfolio)
        self.assertIsInstance(portfolio, dict)

if __name__ == '__main__':
    unittest.main()