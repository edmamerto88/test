from behave import *
import time
from selenium import webdriver
import config
from pages import *

@given('a valid user name and password')
def step_impl(context):
	global username, password
	username=config.username
	password=config.password

@when('a valid user clicking on the login button after typing in user name and password')
def step_impl(context):
	page = LoginPage(context)
	page.visit_login_page("https://platform.operr.com/admin/index.php")
	page.enter_credentials(username,password)
	pass

@then('map should display')
def step_impl(context):
	page = LoginPage(context)
	page.assert_login()
	

