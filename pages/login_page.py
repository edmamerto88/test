from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
# import users
from selenium.webdriver.support.ui import WebDriverWait
import time


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class LoginPage(Page):

	def __init__(self, context):
		Page.__init__(
			self,
			context.browser,
			base_url='https://platform.operr.com/admin/index.php')

	def visit_login_page(self, url):
		self.browser.get(url)

	def enter_credentials(self,username,password):
		self.find_element(*LoginPageLocators.USERNAME).send_keys(username)
		self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
		self.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
		self.browser.implicitly_wait(5)

	def assert_login(self):
		map = self.find_element(*DashboardPageLocators.MAP)
		assert(map)
		self.browser.implicitly_wait(5)
		time.sleep(5)