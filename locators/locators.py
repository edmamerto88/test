from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class LoginPageLocators(object):
  USERNAME      = (By.ID, 'username')
  PASSWORD      = (By.ID, 'password')
  SUBMIT_BUTTON = (By.NAME, 'submit')

class DashboardPageLocators(object):
  MAP           = (By.ID, 'map-canvas')

class UserPageLocators(object):
  USER_TAB            = (By.XPATH, '//ul/li[4]')
  ADD_USER_BUTTON     = (By.XPATH, '//*[@id="page-wrapper"]/div[2]/div[1]/a[2]')
  USER_FORM_HEADING   = (By.XPATH, '//*[@id="upload"]/div[1]')
  USERNAME            = (By.ID, 'username')
  EMAIL               = (By.ID, 'email')
  PASSWORD            = (By.XPATH, '//*[@id="upload"]/div[2]/div[1]/input[3]')
  FIRST_NAME          = (By.ID, 'first_name')
  LAST_NAME           = (By.ID, 'last_name')
  PHONE               = (By.ID, 'phone')
  SECONDARY_PHONE     = (By.ID, 'secondary_phone')
  ADDRESS             = (By.ID, 'address')
  PROFILE_PHOTO       = (By.ID, 'profile_photo')
  PREFERRED_DRIVER_ID = (By.ID, 'preferred_driver_id')
  ACTIVE              = (By.ID, "1")
  # SAVE_BUTTON         = (By.CLASS, "save")



