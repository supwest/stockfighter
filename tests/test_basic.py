import unittest
import os
from .context import stockfighter
from stockfighter import trader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class StockfighterAPITest(unittest.TestCase):

    def setUp(self):
        self.test_trader = stockfighter.trader.Trader()


    def test_trader_driver_is_firefox(self):
        
        self.assertEqual(self.test_trader.driver.name, "firefox")

    def test_trader_checks_page_request_return_code(self):
        status = self.test_trader._check_page_status('https://www.stockfighter.io/')
        self.assertIn(status, [True, False])

    def test_trader_gets_page(self):
        self.test_trader.driver.get('https://www.stockfighter.io/')
        self.assertIn("Stockfighter", self.test_trader.driver.title)

    def test_trader_checks_api_is_up(self):
        response = self.test_trader._check_api_status()        
        self.assertIn(response, [True, False])

    def test_trader_logs_in(self):
        self.test_trader._login()
        self.assertEqual('https://www.stockfighter.io/ui/account', self.test_trader.driver.current_url)
    
    def test_trader_gets_trading_account(self):
        self.test_trader._get_trading_account("Chock A Block")
        self.assertEquals(self.test_trader.account, "MSB81053722")

    def tearDown(self):
        self.test_trader.driver.close()
