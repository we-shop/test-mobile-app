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



class ProfilePage:
	def add_product_to_wishlist(self, driver):
		# add product to wishlist
		click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
		get_add_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text

		is_removed = None

		if get_add_btn_text == "Remove":
			is_removed = True
			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		elif get_add_btn_text == "Add":
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"	
		else:
			print(get_add_btn_text)
			print(f"{ERROR}")

		if is_removed:
			# add product to wishlist
			click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"
			
			# remove product from wishlist
			click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
			get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
			assert get_remove_btn_text == "Remove"	

			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		else:
			# remove product from wishlist
			click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
			get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
			assert get_remove_btn_text == "Remove"

			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"

	def add_product_to_wishlist_and_check_in_profile(self, driver):
		# add product to wishlist
		click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
		get_add_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text

		is_removed = None

		if get_add_btn_text == "Remove":
			is_removed = True
			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		elif get_add_btn_text == "Add":
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"	
		else:
			print(get_add_btn_text)
			print(f"{ERROR}")

		if is_removed:
			# add product to wishlist
			click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"
			
		# 	# remove product from wishlist
		# 	click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
		# 	get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
		# 	assert get_remove_btn_text == "Remove"	

		# 	click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
		# 	toast_msg_wishlist_removed = get_toast_msg(driver)
		# 	assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		# else:
		# 	# remove product from wishlist
		# 	click_on_star_btn = id_click(driver, WISHLIST_START_BUTTON)
		# 	get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
		# 	assert get_remove_btn_text == "Remove"

		# 	click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
		# 	toast_msg_wishlist_removed = get_toast_msg(driver)
		# 	assert toast_msg_wishlist_removed == "Product removed from your wishlist!"



