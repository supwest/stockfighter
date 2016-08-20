import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Trader(object):
    '''
    Define a Trader object to be execute trades
    '''

    def __init__(self):
        '''
        Intializes Trader class for stockfighter trading session
        '''
        self.api_key = os.environ['SF_API_KEY']
        self.main_url = 'https://www.stockfighter.io/'
        self.driver = webdriver.Firefox()
        #self.driver.get(self.main_url)
        self.account = self._get_trading_account()

    def _check_page_status(self, page):
        '''
        Input: string
        Output: boolean

        Returns True if page request returns status 200
        Returns False otherwise
        '''
        response = requests.get(page)
        return response.ok


    def _check_api_status(self):
        '''
        Input: None
        Output: Boolean
        
        
        Returns True if Stockfighter API is available
        Returns False if Stockfighter API is not available or if
        API page request does not return status 200
        '''
        page = 'https://api.stockfighter.io/ob/api/heartbeat'
        page_status = self._check_page_status(page)
        if page_status:
            self.driver.get(page)
            response = json.loads(self.driver.find_element_by_tag_name('body').text)['ok']
            return response
        else:
            return page_status

    def _login(self):
        self.driver.get(self.main_url)
        username = self.driver.find_element_by_name('session[username]')
        password = self.driver.find_element_by_name('session[password]')
        username.send_keys(os.environ['SF_USERNAME'])
        password.send_keys(os.environ['SF_PASSWORD'])
        button = self._get_login_submit_button()
        button.click()
        
    def _get_login_submit_button(self):
        buttons = self.driver.find_elements_by_tag_name('button')
        for button in buttons:
            if button.text == 'Login':
                return button
            else:
                return None

    def _get_trading_account(self):
        '''
        Need to wait unti the description pops up, then close it and get
        acct info
        '''

        
        #self.driver.get("https://www.stockfighter.io/")
        #self._login()
        
        #print self.driver.current_url
        #chock_a_block = self.driver.find_element_by_xpath("//div[@class='panel-body']//ul[@class='list-group']//li[@class='list-group-item']//ul//li//b//a")
        #chock_a_block = self.driver.find_element_by_link_text("Chock A Block")
        #chock_a_block.click()
        #acct_string = driver.find_elements_by_css_selector('strong')[2].text
        #acct_num = acct_string.split()[1]
        #return acct_num
        pass

if __name__ == '__main__':
    pass
