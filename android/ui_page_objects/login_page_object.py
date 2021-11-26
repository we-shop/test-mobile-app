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
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

	def login_with_assert(self, driver):
		# making login
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# going to profile settings
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)

		# verify profile first and last name + username
		profile_first_n_last_name_text = el_id(driver, PROFILE_FIRST_N_LAST_NAMES).text
		profile_username_name_text = el_id(driver, PROFILE_USERNAME).text

		assert profile_first_n_last_name_text == "Mike Pastushenko"
		assert profile_username_name_text == f"@{self.LOGIN}"

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

		# assert profile_first_n_last_name_text == "Mike Pastushenko"
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
		driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
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




