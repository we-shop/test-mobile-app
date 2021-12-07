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


class PostPage:
	def recommend_product(self, driver):
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		recommend_product_click = xpath_click(driver, FOOTER_ITEM_REC_PRODUCT)
		time.sleep(2)


	def ask_question(self, driver):
		click_on_footer_new_post_btn = acc_id_click(driver, FOOTER_ITEM_NEW_POST)
		ask_question_click = xpath_click(driver, FOOTER_ITEM_ASK_QUESTION)
		time.sleep(2)