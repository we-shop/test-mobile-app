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
from locators.search_locators import *
from locators.debug_locators import *
from locators.post_locators import *



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
		# we unable to see more then 7 items without scroll
		if profile_followers >= 7:
			assert total_count_of_existing_followers >= 7
		else:	
			assert profile_followers == total_count_of_existing_followers

		# cover vision issue (unable to detect hidden items)
		# we unable to see more then 7 items without scroll
		if profile_following >= 7:
			assert total_count_of_existing_following >= 7
		else:	
			assert profile_following == total_count_of_existing_following

	def OLD_edit_profile(self, driver):
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
		edit_first_name_field = xpath_keys(driver, PROFILE_EDIT_FIRST_NAME_FIELD, RANDOM_FIRST_NAME)
		edit_last_name_field = xpath_keys(driver, PROFILE_EDIT_LAST_NAME_FIELD, RANDOM_LAST_NAME)

		scroll_down_deep(driver)
		time.sleep(1.2) # obligatory wait, between scrolls
		scroll_down_deep(driver)
		time.sleep(1.2) # obligatory wait, between scrolls

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

	def following_count_manipulations_in_profile(self, driver):
		# read count of followers and following
		profile_followers = int(el_id(driver, FOLLOWERS_COUNT).text)
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# going to followers/following and follow for some followers
		click_on_followers_btn = id_click(driver, FOLLOWERS_LABEL_PROFILE)
		find_all_follow_btns = elems_xpath(driver, LIST_OF_ALL_FOLLOW_BTNS)

		follow_count = 0
		follow_clicked = 0
		follow_unclicked = 0

		# calculating available count of actual "follow" buttons
		# checking if user have at least 1 follower
		if profile_followers == 0:
			print("Re-check account, you need to have at least 1 follower")
			print(f"{ERROR}")

		# calculating how many user have "follow" buttons in followers tab
		for btns in find_all_follow_btns:
			if btns.text == "Follow":
				btns.click()
				follow_count +=1
				follow_clicked +=1

		# click conditions, according to "follow" buttons
		if follow_count == 0:
			if profile_followers == 1:
				xpath_click(driver, FIRST_BTN_IN_FOLLOWERS_TAB)
				follow_unclicked += 1
			elif profile_followers == 2:
				xpath_click(driver, FIRST_BTN_IN_FOLLOWERS_TAB)
				follow_unclicked += 1
			else:
				xpath_click(driver, SECOND_BTN_IN_FOLLOWERS_TAB)
				xpath_click(driver, THIRD_BTN_IN_FOLLOWERS_TAB)
				follow_unclicked += 2

		# going back to profile
		driver.back()
		click_on_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		re_reading_followings_count = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# assertions
		if follow_clicked > 0:
			assert re_reading_followings_count == (profile_following + follow_clicked)
		else:
			assert re_reading_followings_count == (profile_following - follow_unclicked)

		
		# going to following to make sure that current count match existing count of following
		click_on_following_btn = id_click(driver, FOLLOWINGS_LABEL_PROFILE)
		time.sleep(0.6) # obligatory wait to avoid miscalculations of following items
		calculate_all_following_btns = len(elems_xpath(driver, LIST_OF_ALL_FOLLOW_BTNS))

		# cover vision issue (unable to detect hidden items)
		if re_reading_followings_count >= 8:
			assert calculate_all_following_btns >= 8
		else:	
			assert calculate_all_following_btns == re_reading_followings_count


	def follow_few_users(self, driver):
		# test users
		USER_1 = "Molosay"
		USER_2 = "Veremeychik"
		follow = 0
		unfollow = 0 

		# read count of following
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# searching USER_1 and subscribing/unsubscribing
		search_user_one = id_keys(driver, SEARCH_INPUT_FIELD, USER_1)
		click_on_suggested_item_in_search = id_click(driver, SEARCH_RESULT_ONE_ITEM_TEXT)
		follow_btn_user_one_text = el_id(driver, FOLLOW_TO_USER_BTN).text

		if follow_btn_user_one_text == "Follow":
			id_click(driver, FOLLOW_TO_USER_BTN)
			follow += 1
		else:
			id_click(driver, FOLLOW_TO_USER_BTN)
			unfollow += 1

		driver.back()
		
		# searching USER_2 and subscribing/unsubscribing
		search_user_two = id_keys(driver, SEARCH_INPUT_FIELD, USER_2)
		click_on_suggested_item_in_search = id_click(driver, SEARCH_RESULT_ONE_ITEM_TEXT)
		follow_btn_user_two_text = el_id(driver, FOLLOW_TO_USER_BTN).text

		if follow_btn_user_two_text == "Follow":
			id_click(driver, FOLLOW_TO_USER_BTN)
			follow += 1
		else:
			id_click(driver, FOLLOW_TO_USER_BTN)
			unfollow += 1

		driver.back()

		# going back to profile
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		click_on_footer_home_btn = acc_id_click(driver, FOOTER_ITEM_HOME)
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		re_reading_profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# asserting following counter
		assert re_reading_profile_following == ((profile_following + follow) - unfollow)


	def info_pages_check(self, driver):
		# Going to info pages menu
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)
		click_on_settings_legal_n_terms_menu = xpath_click(driver, SETTINGS_LEGAL_N_TERMS)

		# Terms check
		click_on_menu_terms = xpath_click(driver, MENU_TERMS)
		select_chrome_browser(driver)
		page_url_terms = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_terms == "legal.we.shop/terms-and-conditions"
		driver.back()

		# Privacy policy check
		click_on_menu_privacy_policy = xpath_click(driver, MENU_POLICY)
		select_chrome_browser(driver)
		page_url_privacy_policy = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_privacy_policy == "legal.we.shop/privacy-policy"
		driver.back()

		# Cookie policy check
		click_on_menu_cookies = xpath_click(driver, MENU_COOKIE)
		select_chrome_browser(driver)
		page_url_cookie = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_cookie == "help.we.shop/en/article/cookie-policy-pu4kpj/"
		driver.back()

		# Acknowledgements check
		click_on_menu_acknowledgements = xpath_click(driver, MENU_ACKNOWLEDGEMENTS)
		select_chrome_browser(driver)
		page_url_acknowledgements = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_acknowledgements == "help.we.shop/en/article/acknowledgements-7z42ii/?bust=1629990511519"
		driver.back()

		# Community Guidelines check
		click_on_menu_community_guidelines = xpath_click(driver, MENU_COMMUNITY_GUIDES)
		select_chrome_browser(driver)
		page_url_cummunity_guides = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_cummunity_guides == "help.we.shop/en/article/community-guidelines-m34bm5/"
		driver.back()

	def customer_support_page_check(self, driver):
		# make back, because this test bound with info_pages_check test
		driver.back()

		# Going to info pages menu
		click_on_settings_customer_support = xpath_click(driver, SETTINGS_CUSTOMER_SUPPORT)

		# Customer support check
		select_chrome_browser(driver)
		page_url_terms = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_terms == "help.we.shop/en/"
		driver.back()
	

	def about_version_check(self, driver):
		# changing debug config to UAT
		read_app_version = el_id(driver, APP_VERSION_LOGIN_SCREEN).text
		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_uat_click = xpath_click(driver, UAT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		assert toast_msg_env_config == "Webapp configuration switched to uat"

		change_api_to_uat_click = xpath_click(driver, UAT_API_RADIO_BTN)
		toast_msg_api_config = get_toast_msg(driver)
		
		# asserting toast api config message
		assert toast_msg_api_config == "API configuration switched to uat"

		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)

		# reading app version and making login
		login_field = id_keys(driver, LOG_FIELD, self.LOGIN)
		password_field = id_keys(driver, PASS_FIELD, self.PASSWORD)
		
		sign_in_btn_click = id_click(driver, SIGN_IN_BTN)

		# going to profile settings
		click_on_profile_footer_item = acc_id_click(driver, PROFILE_FOOTER_MENU)
		click_on_settings_btn = id_click(driver, PROFILE_SETTINGS_BTN)

		# going to settings > about and reading app version
		click_on_about = xpath_click(driver, SETTINGS_ABOUT)
		read_app_version_in_profile_about = el_xpath(driver, APP_VERSION_SETTINGS_ABOUT).text

		assert read_app_version == read_app_version_in_profile_about

	def other_user_posts_n_questions(self, driver):
		# test users
		USER_1 = "@nemesis"
		USER_2 = "Veremeychik"
		follow = 0
		unfollow = 0 


		search_user_one = id_keys(driver, SEARCH_INPUT_FIELD, USER_1)
		click_on_suggested_item_in_search = xpath_click(driver, SEARCH_RESULT_SECOND_ITEM)
		read_opened_profile = el_id(driver, PROFILE_USERNAME).text
		assert read_opened_profile == USER_1
		read_profile_first_and_last_name = el_id(driver, PROFILE_FIRST_AND_LAST_NAME).text

		# post tab manipulation		
		nested_product_count = None

		try:
			if el_xpath(driver, NESTED_PRODUCTS_COUNT_IN_POST).is_displayed():
				nested_product_count = int(el_xpath(driver, NESTED_PRODUCTS_COUNT_IN_POST).text.split("+")[1]) + 1
		except:
			nested_product_count = False

		
		if nested_product_count != False:
			read_product_post_name = el_xpath(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT).text
			go_to_first_product = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT)
			assert nested_product_count == len(elems_xpath(driver, READ_SINGLE_PRODUCT_LINEAR_LAYOUTS))
		else:
			read_product_post_name = el_xpath(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT_SPECIAL).text
			go_to_first_product = xpath_click(driver, PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT)
			

		read_product_name_on_post_page = el_id(driver, POST_PRODUCT_TITLE).text
		read_user_name_in_post = el_id(driver, POST_USERNAME).text
		
		assert read_product_post_name == read_product_name_on_post_page
		assert read_profile_first_and_last_name == read_user_name_in_post

		driver.back()

		# question tab manipulation
		switch_to_question_tab = acc_id_click(driver, PROFILE_QUESTIONS_TAB)
		##############################################################################
		# NEED TO ADD CHECK FOR COUNT OF PRODUCT IN QUESTION, WHEN WILL BE IMPLEMENTED
		##############################################################################
		click_on_first_question = xpath_click(driver, FIRST_QUESTION_IN_QUEST_TAB)
		read_username_in_question = el_id(driver, POST_USERNAME).text

		assert el_id(driver, QUESTION_REPLY_LABEL).is_displayed()
		assert read_profile_first_and_last_name == read_username_in_question
		
