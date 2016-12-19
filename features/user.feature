Feature: User can create, read, update and delete users 

Scenario: User can add a new user
	Given a user is logged in 
	Then user is on the User page
	When user clicks the add-new-user-button
	Then user should land on the add-user-form
	Then user enters a username "Tester123"
	Then user enters an email "tester@test.com"
	Then user enters a password "123456"
	Then user enters a first name "foo"
	Then user enters a last name "bar"
	Then user enters a phone number "888 888 8881"
	Then user enters a secondary phone number "888 888 880"
	Then user enters an address "16743 Apple Street South Hills California 8888"
	



