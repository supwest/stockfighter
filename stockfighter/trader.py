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
        self.driver = webdriver.Firefox()

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


if __name__ == '__main__':
    pass
