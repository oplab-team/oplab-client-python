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

if __name__ == '__main__':
    unittest.main()