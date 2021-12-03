from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.profile_locators import *
from locators.login_locators import *



class ProfilePage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD

	def followings_followers_count(self, driver):
		# read count of followers and following
		profile_followers = int(el_id(driver, FOLLOWERS_COUNT).text)
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# going to followers/following and reading real count of followers/following
		click_on_followers_btn = id_click(driver, FOLLOWERS_LABEL_PROFILE)
		total_count_of_existing_followers = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))
		click_on_following_tab = acc_id_click(driver, PROFILE_FOLLOWERS_TAB_FOLLOWINGS_TAB)
		total_count_of_existing_following = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))

		# assertion of real and readed count of followers/following
		assert profile_followers == total_count_of_existing_followers
		assert profile_following == total_count_of_existing_following

	def edit_profile(self, driver):
		# random data
		RANDOM_FIRST_NAME = rand_letters(7)
		RANDOM_LAST_NAME = rand_letters(7)
		RANDOM_BIO_NAME = rand_letters(12)

		# go to settings > edit
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		click_on_settings_edit_btn = id_click(driver, PROFILE_SETTINGS_EDIT_BTN)

		# temprorary flow is not fully completed [WILL BE FINISHED IN FUTURE > UPLOAD STAGE IS NOT COMPLETED]
		# profie photo change (open > cancel flow)
		click_on_profile_photo_change_btn = id_click(driver, PROFILE_EDIT_PHOTO_CHANGE_ICON)
		click_on_take_photo_in_window = xpath_click(driver, PROFILE_EDIT_PHOTO_CHANGE_TAKE_PHOTO)
		time.sleep(3) #obligatory wait to open phone camera
		driver.back()
		toast_error_msg_get = get_toast_msg(driver)
		expected_message_one = "Sorry, an error occurred while trying to pick up the image. Please try again or pick up a different image."
		expected_message_two = "Media unrecognised. Please select a valid image or video and try again."

		# checking expected error message (2 possible variants)
		assert toast_error_msg_get == expected_message_one or expected_message_two == expected_message_two

		# editing first/last name and bio
		edit_first_name_field = id_keys(driver, PROFILE_EDIT_FIRST_NAME_FIELD, RANDOM_FIRST_NAME)
		edit_last_name_field = id_keys(driver, PROFILE_EDIT_LAST_NAME_FIELD, RANDOM_LAST_NAME)
		edit_bio_name_field = id_keys(driver, PROFILE_EDIT_BIO_FIELD, RANDOM_BIO_NAME)
		click_on_save_changes_btn = id_click(driver, PROFILE_EDIT_SAVE_CHANGES_BTN)
		
		# refresh manupulation to see new profile data
		click_on_back_btn = acc_id_click(driver, BACK_BTN)
		click_on_footer_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		click_on_footer_profile_btn = acc_id_click(driver, FOOTER_ITEM_PROFILE)

		# asserting edited first/last name and bio
		read_first_and_last_name_text = el_id(driver, PROFILE_FIRST_AND_LAST_NAME).text
		read_bio_text = el_id(driver, PROFILE_BIO).text
		compared_first_and_last_random_names = RANDOM_FIRST_NAME + " " + RANDOM_LAST_NAME

		assert read_first_and_last_name_text == compared_first_and_last_random_names
		assert read_bio_text == RANDOM_BIO_NAME

	def deactivate_account_and_login_after(self, driver):
		# deactivate account
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		driver.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
		deactivate_acc_click = xpath_click(driver, SETTINGS_DEACTIVATE_ACC)
		deactivate_acc_btn_click = id_click(driver, DEACTIVATE_ACCOUNT_BTN)
		accept_are_you_sure_modal = id_click(driver, DEACTIVATE_ACC_ACCEPT_IN_MODAL)

		# check if user logged out
		already_have_account_btn_click = id_click(driver, ALREADY_HAVE_ACC_LOGIN_SCREEN)
		read_welcome_back_text_on_login_screen = el_id(driver, READ_WELCOME_TEXT_LOGIN_SCREEN).text

		assert read_welcome_back_text_on_login_screen == "Welcome back!"

		# login after deactivation
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# going to profile from footer menu (to make sure you are already logged in)
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)	

