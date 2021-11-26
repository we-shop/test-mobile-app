#from selenium.webdriver.common.by import By
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
from locators.search_locators import *
from locators.debug_locators import *
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction



class LoginPage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD

	def login_only(self, driver):
		# making login
		login_field = driver.find_element(By.ID, LOG_FIELD).send_keys(self.LOGIN)
		password_field = driver.find_element(By.ID, PASS_FIELD).send_keys(self.PASSWORD)
		sign_in_btn_click = driver.find_element(By.ID, SIGN_IN_BTN).click()

	def login_with_assert(self, driver):
		# making login
		login_field = driver.find_element(By.ID, LOG_FIELD).send_keys(self.LOGIN)
		password_field = driver.find_element(By.ID, PASS_FIELD).send_keys(self.PASSWORD)
		sign_in_btn_click = driver.find_element(By.ID, SIGN_IN_BTN).click()

		# going to profile settings
		click_on_profile_footer_item = driver.find_element(MobileBy.ACCESSIBILITY_ID, PROFILE_FOOTER_MENU).click()

		# verify profile first and last name + username
		profile_first_n_last_name_text = driver.find_element(By.ID, PROFILE_FIRST_N_LAST_NAMES).text
		profile_username_name_text = driver.find_element(By.ID, PROFILE_USERNAME).text

		assert profile_first_n_last_name_text == "Mike Pastushenko"
		assert profile_username_name_text == f"@{self.LOGIN}"

	def login_to_prod(self, driver):
		# making login to production (without debug step)
		already_have_acc_btn_click = driver.find_element(By.ID, ALREADY_HAVE_ACC_LINK).click()
		login_field = driver.find_element(By.ID, LOG_FIELD).send_keys(self.LOGIN)
		password_field = driver.find_element(By.ID, PASS_FIELD).send_keys(self.PASSWORD)
		sign_in_btn_click = driver.find_element(By.ID, SIGN_IN_BTN).click()

		# commented, because can be various scenarios
		# # going to profile settings
		# click_on_profile_footer_item = driver.find_element(MobileBy.ACCESSIBILITY_ID, PROFILE_FOOTER_MENU).click()

		# # verify profile first and last name + username
		# profile_first_n_last_name_text = driver.find_element(By.ID, PROFILE_FIRST_N_LAST_NAMES).text
		# profile_username_name_text = driver.find_element(By.ID, PROFILE_USERNAME).text

		# assert profile_first_n_last_name_text == "Mike Pastushenko"
		# assert profile_username_name_text == f"@{self.LOGIN}"

		# click_on_settings_btn = driver.find_element(By.ID, SETTINGS_BTN_PROFILE).click()

	def login_with_incorrect_creds(self, driver):
		# making login with incorrect creds
		login_field = driver.find_element(By.ID, LOG_FIELD).send_keys("qatestqa")
		password_field = driver.find_element(By.ID, PASS_FIELD).send_keys("qatestpassqa")
		sign_in_btn_click = driver.find_element(By.ID, SIGN_IN_BTN).click()

		toast_msg_incorrect_config = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.Toast").text # need to change it in future	

		# asserting toast incorrect credentials message
		assert toast_msg_incorrect_config == "No user is matching these credentials"

	def logout(self, driver):
		# sign out
		click_on_settings_btn = driver.find_element(By.ID, SETTINGS_BTN_PROFILE).click()
		driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		sign_out_btn_click = driver.find_element(MobileBy.XPATH, SIGN_OUT_BTN).click()
		click_yes_in_logout_modal = driver.find_element(By.ID, ACCEPT_MODAL_BTN_LOGOUT).click()
		
		# verify login screen title (means that you are successfully logged out)
		login_screen_title_text = driver.find_element(By.ID, LOGIN_SCREEN_TITLE).text
		assert login_screen_title_text == "We’re so glad to have you around."

	def logout_from_main_screen(self, driver):
		# sign out
		click_on_profile_footer_item = driver.find_element(MobileBy.ACCESSIBILITY_ID, PROFILE_FOOTER_MENU).click()
		click_on_settings_btn = driver.find_element(By.ID, SETTINGS_BTN_PROFILE).click()
		driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		sign_out_btn_click = driver.find_element(MobileBy.XPATH, SIGN_OUT_BTN).click()
		click_yes_in_logout_modal = driver.find_element(By.ID, ACCEPT_MODAL_BTN_LOGOUT).click()
		
		# verify login screen title (means that you are successfully logged out)
		login_screen_title_text = driver.find_element(By.ID, LOGIN_SCREEN_TITLE).text
		assert login_screen_title_text == "We’re so glad to have you around."




