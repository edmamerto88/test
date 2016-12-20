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
  ACTIVE              = (By.ID, '1')
  # SAVE_BUTTON         = (By.CLASS, "save")

  class DriverPageLocators(object):
  #Driver Info
  FLEET_NUM               = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[1]/input[1]')
  FIRST_NAME              = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[1]/input[2]')
  LAST_NAME               = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[1]/input[3]')
  USERNAME                = (By.ID, 'username')
  EMAIL                   = (By.ID, 'email')
  PASSWORD                = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[1]/input[6]')
  PHONE                   = (By.ID, 'phone')
  SECONDARY_PHONE         = (By.ID, 'secondary_phone')
  DATE_OF_BIRTH           = (By.ID, 'driver_dob')
  GENDER                  = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[1]/select[1]')
  COUNTRY_OF_ORIGIN       = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[1]/select[2]')
  DRIVING_EXPERIENCE      = (By.ID, 'driving_experience')
  DRIVER_TYPE             = (By.ID, '//*[@id="form_driver"]/div[2]/div[1]/select[3]')
  PREFERRED_DRIVER_ID     = (By.ID, 'preferred_driver_id')
  AFFILIATED_COMPANY_NAME = (By.ID, 'company_id')
  AFFILIATED_BASE_NAME    = (By.ID, 'base_id')
  ALLOW_PETS              = (By.ID, 'c1')
  ALLOW_WHEELCHAIR        = (By.ID, 'c2')
  LANGUAGE                = (By.XPATH, '//*[@value="Mandarin"]')
  BASE_PERCENT            = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[2]/input[3]')
  DRIVER_PERCENT          = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[2]/input[4]')
  RESERVE_PERCENT         = (By.XPATH, '//*[@id="form_driver"]/div[2]/div[2]/input[5]')
  BASE_APPROVED           = (By.ID, '1')
  DRIVER_PROFILE_UPLOAD_BUTTON      = (By.NAME, 'profile_photo')
  SIGNATURE_UPLOAD_BUTTON           = (By.NAME, 'signature')
  #Driver License/TLC Info
  DRIVER_LICENSE_NUM                = (By.XPATH, '//*[@id="form_driver"]/div[6]/div[1]/input[1]')
  DRIVER_LICENSE_CLASS              = (By.XPATH, '//*[@id="form_driver"]/div[6]/div[1]/input[2]')
  DRIVER_LICENSE_STATE              = (By.XPATH, '//*[@id="form_driver"]/div[6]/div[1]/select')
  DRIVER_LICENSE_START_DATE         = (By.ID, 'driver_license_start')
  DRIVER_LICENSE_EXP_DATE           = (By.ID, 'driver_license_expire')
  DRIVER_TLC_FHV_NUM                = (By.XPATH, '//*[@id="form_driver"]/div[6]/div[2]/input[1]')
  DRIVER_TLC_FHV_LICENSE_START_DATE = (By.ID, 'driver_tlc_fhv_license_start')
  DRIVER_TLC_FHV_EXP_DATE           = (By.ID, 'driver_tlc_fhv_license_expire')
  #Background Check Info
  BACKGROUND_CHECK_START_DATE       = (By.ID, 'background_check_start')
  BACKGROUND_CHECK_EXP_DATE         = (By.ID, 'background_check_expire')
  BACKGROUND_CHECK_UPLOAD_BUTTON    = (By.NAME, 'background_check')
  #Driving Record Info
  DRIVING_RECORD_START_DATE         = (By.ID, 'driving_record_start')
  DRIVING_RECORD_EXPIRE             = (By.ID, 'driving_record_expire')
  DRIVING_RECORD_UPLOAD_BUTTON      = (By.ID, 'driving_record')
  #Drug Screen Info
  DRUG_SCREEN_START_DATE            = (By.ID, 'drug_screen_start')
  DRUG_SCREEN_EXP_DATE              = (By.ID, 'drug_screen_expire')
  DRUG_SCREEN_UPLOAD_BUTTON         = (By.ID, 'drug_screen')
  #Vehicle Info
  CURRENT_VEHICLE                   = (By.ID, 'vehicle_id')
  #Cross County
  CROSS_COUNTY                      = (By.XPATH, '//*[@id="form_driver"]/div[25]/div/input[2]')
  SAVE_BUTTON                       = (By.ID, 'save_driver')
  # SAVE_BUTTON         = (By.CLASS, "save")




