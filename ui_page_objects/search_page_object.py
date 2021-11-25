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


class SearchPage:
	def search_and_clear_field(self, driver):
		# search request
		make_request_in_search_field = driver.find_element(By.ID, SEARCH_INPUT_FIELD).send_keys("Adidas")
		select_suggested_search_item = driver.find_element(MobileBy.XPATH, SELECT_SUGGESTED_ITEM_SEARCH).click()

		# verify that we have search result
		first_item_in_search_result_text = driver.find_element(MobileBy.XPATH, FIRST_ITEM_NAME_SEARCH).text

		assert "Adidas" in first_item_in_search_result_text

		# clear search result
		clear_field = driver.find_element(By.ID, CLEAR_SEARCH_BTN).click()
		
		# asserting recent search name
		recent_search_item_text = driver.find_element(By.ID, RECENT_SEARCH_ITEM_TEXT).text
		assert recent_search_item_text == "Adidas"


	def search_extended(self, driver):
		pass

	def search_negative(self, driver):
		pass
