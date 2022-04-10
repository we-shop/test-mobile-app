from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.login_locators import *

#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import string
import random
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
import pytest
from locators.product_detail_locators import PRODUCT_MODAL_CONTINUE_BTN
from appium.webdriver.common.touch_action import TouchAction


class LoginPage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW, LOGIN_INT, PASSWORD_INT, LOGIN_INT_NEW, PASSWORD_INT_NEW):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD
		self.LOGIN_NEW = LOGIN_NEW
		self.PASSWORD_NEW = PASSWORD_NEW
		self.LOGIN_INT = LOGIN_INT
		self.PASSWORD_INT = PASSWORD_INT
		self.LOGIN_INT_NEW = LOGIN_INT_NEW
		self.PASSWORD_INT_NEW = PASSWORD_INT_NEW

	def login_only(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		# making login
		login_field = id_keys(driver, LOG_FIELD, USERNAME)
		password_field = id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)
		update_temp_file(self.LOGIN)

	def login_only_new_acc(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT_NEW
			PASSWORD = self.PASSWORD_INT_NEW
		elif current_env == "uat":
			USERNAME = self.LOGIN_NEW
			PASSWORD = self.PASSWORD_NEW
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		# making login
		login_field = id_keys(driver, LOG_FIELD, USERNAME)
		password_field = id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)
		update_temp_file(self.LOGIN)

	def login_go_to_profile(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")

		# making login
		login_field = id_keys(driver, LOG_FIELD, USERNAME)
		password_field = id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# going to profile settings
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		update_temp_file(self.LOGIN)

	def login_with_assert(self, driver):
		# configuration for credentials according to env
		current_env = read_data_from_temp_file()[0]
		USERNAME = None
		PASSWORD = None

		if current_env == "int":
			USERNAME = self.LOGIN_INT
			PASSWORD = self.PASSWORD_INT
		elif current_env == "uat":
			USERNAME = self.LOGIN
			PASSWORD = self.PASSWORD
		else:
			print(current_env)
			print(F"{ERROR} Something wrong with current env variable")	
		# making login
		login_field = id_keys(driver, LOG_FIELD, USERNAME)
		password_field = id_keys(driver, PASS_FIELD, PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# going to profile settings
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)

		# verify profile first and last name + username
		profile_first_n_last_name_text = el_id(driver, PROFILE_FIRST_N_LAST_NAMES).text
		profile_username_name_text = el_id(driver, PROFILE_USERNAME).text

		assert profile_username_name_text == f"@{USERNAME}"

	def login_to_prod(self, driver):
		# making login to production (without debug step)
		already_have_acc_btn_click = id_click(driver, ALREADY_HAVE_ACC_LINK)
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# commented, because can be various scenarios
		# # going to profile settings
		# click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)

		# # verify profile first and last name + username
		# profile_first_n_last_name_text = el_id(driver, PROFILE_FIRST_N_LAST_NAMES).text
		# profile_username_name_text = el_id(driver, PROFILE_USERNAME).text

		# assert profile_username_name_text == f"@{self.LOGIN}"

		# click_on_settings_btn = id_click(driver, SETTINGS_BTN_PROFILE)

	def login_with_incorrect_creds(self, driver):
		# making login with incorrect creds
		login_field = id_keys(driver, LOG_FIELD, "qatestqa")
		password_field = id_keys(driver, PASS_FIELD, "qatestpassqa")
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		toast_msg_incorrect_config = get_toast_msg(driver)

		# asserting toast incorrect credentials message
		assert toast_msg_incorrect_config == "No user is matching these credentials"

	def logout(self, driver):
		# sign out
		click_on_settings_btn = id_click(driver, SETTINGS_BTN_PROFILE)
		scroll_down_deep(driver) #driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		sign_out_btn_click = xpath_click(driver, SIGN_OUT_BTN)
		click_yes_in_logout_modal = id_click(driver, ACCEPT_MODAL_BTN_LOGOUT)
		
		# verify login screen title (means that you are successfully logged out)
		login_screen_title_text = el_id(driver, LOGIN_SCREEN_TITLE).text
		assert login_screen_title_text == "We’re so glad to have you around."

	def logout_from_main_screen(self, driver):
		# sign out
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		click_on_settings_btn = id_click(driver, SETTINGS_BTN_PROFILE)
		driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		sign_out_btn_click = xpath_click(driver, SIGN_OUT_BTN)
		click_yes_in_logout_modal = id_click(driver, ACCEPT_MODAL_BTN_LOGOUT)
		
		# verify login screen title (means that you are successfully logged out)
		login_screen_title_text = el_id(driver, LOGIN_SCREEN_TITLE).text
		assert login_screen_title_text == "We’re so glad to have you around."


	def ios_test_example(self, driver):
		time.sleep(1)
		driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='Debug']").click()

		time.sleep(2)
		x = driver.find_elements_by_xpath("//*[@label='UAT']")
		for i in x:
			print(i.text)
			i.click()

		time.sleep(2)

		driver.back()

		driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='Sign in']").click() #("label contains 'Sign in'").click()
		login_field = driver.find_element_by_accessibility_id("loginTextField")
		password_field = driver.find_element_by_accessibility_id("passwordTextField")
		login_field.send_keys("nemesis")
		password_field.send_keys("123456aA#") #(r"ZO2c%omy")
		click_on_sign_in = driver.find_element_by_accessibility_id("continueButton").click()

		time.sleep(2)
		