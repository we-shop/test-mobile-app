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
		PRODUCT_ID = str(random.randint(1000, 10000000))

		# product creation step 1 (search)
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		recommend_product_click = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		add_first_product_click = xpath_click(driver, ADD_FIRST_PRODUCT_PLUS_INPUT)
		search_product_for_post = id_keys(driver, SEARCH_PRODUCT_POST_CREATION, "Samsung")
		driver.keyevent(66) # additional execution: send_enter_key_adb(driver)
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
		# generating random id for question title
		QUESTION_ID = str(random.randint(1000, 10000000))

		# question creation step 1 (question title)
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		ask_question_click = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)
		fill_question_text = id_keys(driver, QUESTION_TEXT_STEP_ONE, f"Test question number {QUESTION_ID}")
		click_next_btn = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# asserting step 2
		bread_crumbs_text_step_2 = el_id(driver, QUESTION_BREAD_CRUMBS).text
		assert bread_crumbs_text_step_2 == "2"

		# question creation step 2 (customize background)
		popular_designs_click = id_click(driver, QUESTION_UPLOAD_FROM_DESIGNS)
		all_backgrounds = elems_xpath(driver, CUSTOM_BACKGROUND_ITEMS)
		random_background_click = all_backgrounds[random.randint(0, 5)].click()
		save_btn_background_lst_click = id_click(driver, SAVE_BTN_BACKGROUND_ITEMS)

		all_texts = elems_xpath(driver, ALL_TEXT_STYLES)
		random_text_style_click = all_texts[random.randint(0, 5)].click()
		switch_to_text_colour_tab = acc_id_click(driver, BACKGROUND_TEXT_COLOUR_TAB)
		all_text_clrs = elems_xpath(driver, ALL_TEXT_COLOURS)
		random_clrs_click = all_text_clrs[random.randint(0, 8)].click()

		done_btn_click = id_click(driver, STEP_BTN_ADD_PRODUCT)
		next_btn_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# asserting step 3
		bread_crumbs_text_step_3 = el_id(driver, QUESTION_BREAD_CRUMBS).text
		assert bread_crumbs_text_step_3 == "3"
	
		# question creation step 3 (add product)
		click_in_srch_field = id_click(driver, SEARCH_PRODUCT_POST_CREATION) # probably temporary step, because of bug
		search_product_for_question = id_keys(driver, SEARCH_PRODUCT_POST_CREATION, "Xiaomi")
		driver.keyevent(66) # additional execution: send_enter_key_adb(driver)
		fill_radio_btn_product_one = xpath_click(driver, SEARCH_RESULT_PRODUCT_ONE)
		fill_radio_btn_product_two = xpath_click(driver, SEARCH_RESULT_PRODUCT_TWO)
		fill_radio_btn_product_three = xpath_click(driver, SEARCH_RESULT_PRODUCT_THREE)
		click_done_step_btn = id_click(driver, STEP_BTN_ADD_PRODUCT)
		next_btn_step_click = id_click(driver, STEP_BTN_ADD_PRODUCT)

		# asserting step 4
		bread_crumbs_text_step_4 = el_id(driver, QUESTION_BREAD_CRUMBS).text
		assert bread_crumbs_text_step_4 == "4"

		# question creation step 4 (add caption and publish)
		enter_text_to_caption_input_field = id_keys(driver, CAPTION_INPUT_FIELD, f"Test caption for question number {QUESTION_ID}")
		publish_btn_click = id_click(driver, PUBLISH_BTN_ADD_PRODUCT)

		# check if question created (checking title/caption in feed)
		get_correct_text_by_id(driver, FEED_POST_DESCRIPTION, QUESTION_ID)
