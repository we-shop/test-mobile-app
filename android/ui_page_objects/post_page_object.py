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
		# generating random id for product title/caption
		PRODUCT_ID = random.randint(1000, 10000000)

		# product creation step 1 (search)
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		recommend_product_click = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		add_first_product_click = xpath_click(driver, ADD_FIRST_PRODUCT_PLUS_INPUT)
		search_product_for_post = id_keys(driver, SEARCH_PRODUCT_POST_CREATION, "Samsung")
		send_enter_key_adb(driver)
		fill_radio_btn_product_one = xpath_click(driver, SEARCH_RESULT_PRODUCT_ONE)
		fill_radio_btn_product_two = xpath_click(driver, SEARCH_RESULT_PRODUCT_TWO)
		fill_radio_btn_product_three = xpath_click(driver, SEARCH_RESULT_PRODUCT_THREE)
		done_btn_search_product_result_click = id_click(driver, STEP_BTN_ADD_PRODUCT)
		acc_id_click(driver, PRODUCT_ADD_FOOTER_ITEM_MEDIA)

		# media step
		click_use_product_image = id_click(driver, MEDIA_IMAGE_FROM_PRODUCT)
		next_btn_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# caption step and publish
		enter_text_to_caption_input_field = id_keys(driver, CAPTION_INPUT_FIELD, f"Test caption for new product number {PRODUCT_ID}")
		publish_btn_click = id_click(driver, PUBLISH_BTN_ADD_PRODUCT)

		# check if product created (checking title/caption in feed)
		get_correct_text_by_id(driver, FEED_POST_DESCRIPTION, PRODUCT_ID)


	def ask_question(self, driver):
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		ask_question_click = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)
		time.sleep(2)