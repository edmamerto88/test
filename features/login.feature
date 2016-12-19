Feature: Operr login

Scenario: valid user can login operr site
	Given a valid user name and password
	When a valid user clicking on the login button after typing in user name and password
	Then map should display