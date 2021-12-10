from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.post_locators import *
from locators.profile_locators import *
from appium.webdriver.extensions.android.nativekey import AndroidKey

class PostPage:
	def recommend_product(self, driver):
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		recommend_product_click = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		add_first_product_click = xpath_click(driver, ADD_FIRST_PRODUCT_PLUS_INPUT)
		search_product_for_post = id_keys(driver, SEARCH_PRODUCT_POST_CREATION, "Samsung")
		driver.execute_script('mobile: shell', {'command': 'input keyevent', 'args':'KEYCODE_ENTER'}) # send Enter key example (using adb)
		#.press_keycode(AndroidKey.ENTER)
		#driver.press_keycode(AndroidKey.ENTER)
		#driver.press_keycode(66)


		time.sleep(4)


	def ask_question(self, driver):
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		ask_question_click = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)
		time.sleep(2)