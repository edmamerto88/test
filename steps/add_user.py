from behave import *
import time
from selenium import webdriver
import config
from pages import *

@given('a user is logged in')
def step_impl(context):
	page = LoginPage(context)
	page.visit_login_page("https://platform.operr.com/admin/index.php")
	page.enter_credentials(config.username,config.password)
	pass

@then('user is on the User page')
def step_impl(context):
	page = UserPage(context)
	page.visit_user_page()
	pass

@when('user clicks the add-new-user-button')
def step_impl(context):
	page = UserPage(context)
	page.visit_user_form()
	pass

@then('user should land on the add-user-form')
def step_impl(context):
	page = UserPage(context)
	page.assert_user_form()
	pass

@then('user enters a username "{username}"')
def step_impl(context, username):
	page = UserPage(context)
	page.enter_username(username)
	pass

@then('user enters an email "{email}"')
def step_impl(context, email):
	page = UserPage(context)
	page.enter_email(email)
	pass

@then('user enters a password "{password}"')
def step_impl(context, password):
	page = UserPage(context)
	page.enter_password(password)
	pass

@then('user enters a first name "{first_name}"')
def step_impl(context, first_name):
	page = UserPage(context)
	page.enter_first_name(first_name)
	pass

@then('user enters a last name "{last_name}"')
def step_impl(context, last_name):
	page = UserPage(context)
	page.enter_last_name(last_name)
	pass

@then('user enters a phone number "{phone_number}"')
def step_impl(context, phone_number):
	page = UserPage(context)
	page.enter_phone(phone_number)
	pass

@then('user enters a secondary phone number "{secondary_phone_number}"')
def step_impl(context, secondary_phone_number):
	page = UserPage(context)
	page.enter_secondary_phone(secondary_phone_number)
	pass

@then('user enters an address "{address}"')
def step_impl(context, address):
	page = UserPage(context)
	page.enter_address(address)
	pass




