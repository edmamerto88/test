from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, browser, base_url='https://platform.operr.com/admin/index.php'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30
 
    def find_element(self, *locator):
        return self.browser.find_element(*locator)
 
    def open(self,url):
        url = self.base_url + url
        self.browser.get(url)
        
    def get_title(self):
        return self.browser.title
        
    def get_url(self):
        return self.browser.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()