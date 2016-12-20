Feature: User can create, read, update and delete a driver 

Scenario: User can add a Driver Info
	Given a user is logged in 
	Then user is on the Driver page
	When user clicks the add-new-driver-button
	Then user should land on the add-new-driver-form
	Then user enters a fleet number "0123456"
	Then user enters a first name "Tester"
	Then user enters a last name "Tony"
	Then user enters a username "testdriver12"
	Then user enters a email "test@driver.com"
	Then user enters a password "123456"
	Then user enters a phone number "888 888 8881"
	Then user enters a secondary phone number "888 888 880"
	Then user selects a date of birth 
	Then user selects a gender
	Then user selects a country of origin 
	Then user enters number of driving experience "6"
	Then user selects driver type
	Then user selects an affiliated company name
	Then user selects an affiliated base name
	Then user checks allow pets
	Then user checks allow wheelchair
	Then user selects a language
	Then user enters a base percent
	Then user enters a driver percent
	Then user enters a reserve percent
	Then user uploads a driver profile
	Then user uploads a signature 

Scenario: User can add a Driver License/TLC Info
	Given user have filled up Driver Info section
	Then user enters driver's license number "F01293"
	Then user enters driver's license class "classX"
	Then user selects a driver's license state 
	Then user selects a driver's license start date
	Then user selects a driver's license expiration date
	Then user enters a Driver TLC/FHV License number 
	Then user enters a first name "Tester"
	Then user enters a last name "Tony"
	Then user enters a username "testdriver12"
	Then user enters a email "test@driver.com"
	Then user enters a password "123456"
	Then user enters a phone number "888 888 8881"
	Then user enters a secondary phone number "888 888 880"
	Then user selects a date of birth 
	Then user selects a gender
	Then user selects a country of origin 
	Then user enters number of driving experience "6"

	



