import pytest
import os
import time
from ui_page_objects.functions import *
from locators.login_locators import *
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction



# Read from file function
def get_data(data):
	return data.split("#")[0]

# Open settings file
f = open("credentials.txt", "r")
lines = f.readlines()
LOGIN = get_data(lines[0])
PASSWORD = get_data(lines[1])
LOGIN_URL = get_data(lines[2])
f.close()



def test_login_and_logout(selenium):
	# making login
	already_have_acc_btn_click = selenium.find_element(By.ID, ALREADY_HAVE_ACC_LINK).click()
	login_field = selenium.find_element(By.ID, LOG_FIELD).send_keys(LOGIN)
	password_field = selenium.find_element(By.ID, PASS_FIELD).send_keys(PASSWORD)
	sign_in_btn_click = selenium.find_element(By.ID, SIGN_IN_BTN).click()

	# going to profile settings
	click_on_profile_footer_item = selenium.find_element(MobileBy.ACCESSIBILITY_ID, PROFILE_FOOTER_MENU).click()

	# verify profile first and last name + username
	profile_first_n_last_name_text = selenium.find_element(By.ID, PROFILE_FIRST_N_LAST_NAMES).text
	profile_username_name_text = selenium.find_element(By.ID, PROFILE_USERNAME).text

	assert profile_first_n_last_name_text == "Mike Patushenko"
	assert profile_username_name_text == f"@{LOGIN}"

	click_on_settings_btn = selenium.find_element(By.ID, SETTINGS_BTN_PROFILE).click()

	# sign out
	selenium.swipe(start_x=94, start_y=2422, end_x=64, end_y=975, duration=650)
	sign_out_btn_click = selenium.find_element(MobileBy.XPATH, SIGN_OUT_BTN).click()
	click_yes_in_logout_modal = selenium.find_element(By.ID, ACCEPT_MODAL_BTN_LOGOUT).click()
	
	# verify login screen title (means that you are successfully logged out)
	login_screen_title_text = selenium.find_element(By.ID, LOGIN_SCREEN_TITLE).text
	assert login_screen_title_text == "We’re so glad to have you around."

	time.sleep(1.5) # just to see results, can be removed


def test_search(selenium):
	# making login
	already_have_acc_btn_click = selenium.find_element(By.ID, ALREADY_HAVE_ACC_LINK).click()
	login_field = selenium.find_element(By.ID, LOG_FIELD).send_keys(LOGIN)
	password_field = selenium.find_element(By.ID, PASS_FIELD).send_keys(PASSWORD)
	sign_in_btn_click = selenium.find_element(By.ID, SIGN_IN_BTN).click()

	# search request
	make_request_in_search_field = selenium.find_element(By.ID, SEARCH_INPUT_FIELD).send_keys("Adidas")
	select_suggested_search_item = selenium.find_element(MobileBy.XPATH, SELECT_SUGGESTED_ITEM_SEARCH).click()

	# verify that we have search result
	first_item_in_search_result_text = selenium.find_element(MobileBy.XPATH, FIRST_ITEM_NAME_SEARCH).text
	
	assert "Adidas" in first_item_in_search_result_text

	# clear search result
	clear_field = selenium.find_element(By.ID, CLEAR_SEARCH_BTN).click()

	time.sleep(2.5) # just to see results, can be removed

