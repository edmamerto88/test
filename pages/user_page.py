from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
# import users
from selenium.webdriver.support.ui import WebDriverWait
import time


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class UserPage(Page):

	def __init__(self, context):
		Page.__init__(
			self,
			context.browser,
			base_url='https://platform.operr.com/admin/index.php')

	def visit_user_page(self):
		self.find_element(*UserPageLocators.USER_TAB).click()
		add_user_button = self.find_element(*UserPageLocators.ADD_USER_BUTTON)
		assert(add_user_button)
		self.browser.implicitly_wait(5)

	def visit_user_form(self):
		self.find_element(*UserPageLocators.ADD_USER_BUTTON).click()
		self.browser.implicitly_wait(5)

	def assert_user_form(self):
		user_form_heading = self.find_element(*UserPageLocators.USER_FORM_HEADING)
		assert(user_form_heading)
		self.browser.implicitly_wait(5)

	def enter_username(self, username):
		self.find_element(*UserPageLocators.USERNAME).send_keys(username)

	def enter_email(self, email):
		self.find_element(*UserPageLocators.EMAIL).send_keys(email)

	def enter_password(self, password):
		self.find_element(*UserPageLocators.PASSWORD).send_keys(password)

	def enter_first_name(self, first_name):
		self.find_element(*UserPageLocators.FIRST_NAME).send_keys(first_name)

	def enter_last_name(self, last_name):
		self.find_element(*UserPageLocators.LAST_NAME).send_keys(last_name)

	def enter_phone(self, phone_number):
		self.find_element(*UserPageLocators.PHONE).send_keys(phone_number)

	def enter_secondary_phone(self, secondary_phone_number):
		self.find_element(*UserPageLocators.SECONDARY_PHONE).send_keys(secondary_phone_number)

	def enter_address(self, address):
		self.find_element(*UserPageLocators.ADDRESS).send_keys(address)
		time.sleep(10)


