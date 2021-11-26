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

class DebugPage:
	def switch_to_uat(self, driver):
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

	def switch_to_int(self, driver):
		debug_btn_click = id_click(driver, DEBUG_BTN)
		change_configuration_menu_click = xpath_click(driver, CHANGE_CONFIG_MENU)
		change_env_to_int_click = xpath_click(driver, INT_ENV_RADIO_BTN)
		toast_msg_env_config = get_toast_msg(driver)
		
		# asserting toast env config message
		assert toast_msg_env_config == "Webapp configuration switched to int"

		change_api_to_int_click = xpath_click(driver, INT_API_RADIO_BTN)
		toast_msg_api_config = get_toast_msg(driver)

		# asserting toast api config message
		assert toast_msg_api_config == "API configuration switched to int"

		go_to_login_screen_click = id_click(driver, GO_TO_LOG_SCR)


