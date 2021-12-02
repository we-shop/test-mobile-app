from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.product_detail_locators import *



class ProductDetailPage:
	def add_product_to_wishlist(self, driver):
		# add product to wishlist
		click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
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
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"
			
			# remove product from wishlist
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
			assert get_remove_btn_text == "Remove"	

			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		else:
			# remove product from wishlist
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			get_remove_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text
			assert get_remove_btn_text == "Remove"

			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"

	def add_product_to_wishlist_and_check_in_profile(self, driver):
		# add product to wishlist
		GET_PRODUCT_NAME = el_id(driver, PRODUCT_NAME_TITLE).text
		WISHLIST_NAME = []
		click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
		get_add_btn_text = el_xpath(driver, ADD_BUTTON_IN_WISHLIST).text

		is_removed = None

		if get_add_btn_text == "Remove":
			is_removed = True
			WISHLIST_NAME.append(el_id(driver, NAME_OF_WISHLIST_PRODUCT_PAGE).text)
			click_on_remove_from_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_removed = get_toast_msg(driver)
			assert toast_msg_wishlist_removed == "Product removed from your wishlist!"
		elif get_add_btn_text == "Add":
			WISHLIST_NAME.append(el_id(driver, NAME_OF_WISHLIST_PRODUCT_PAGE).text)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"	
		else:
			print(get_add_btn_text)
			print(f"{ERROR}")

		if is_removed:
			# add product to wishlist
			click_on_star_btn = id_click(driver, WISHLIST_STAR_BUTTON)
			click_on_add_to_wishlist_btn = xpath_click(driver, ADD_BUTTON_IN_WISHLIST)
			toast_msg_wishlist_added = get_toast_msg(driver)
			assert toast_msg_wishlist_added == "Product added to your wishlist!"
			
		# going back to profile
		click_on_back_btn = acc_id_click(driver, BACK_BTN)
		profile_footer_icon_click = id_click(driver, PROFILE_FOOTER_ITEM)
		wishlist_profile_click = id_click(driver, WISHLIST_PROFILE_CLICK)

		# checking if item was indeed added to correct wishlist
		# Note: can't avoid try/except block, because of java error (stale element exception > unknown DOM issue)
		try:
			list_of_all_wishlists = elems_xpath(driver, WISHLIST_ITEMS_TITLE_LIST)
			click_on_wishlist_with_correct_name = [i.click() for i in list_of_all_wishlists if i.text == WISHLIST_NAME[0]]
		except:
			pass

		list_of_all_items_inside_wishlist = elems_xpath(driver, LIST_OF_ITEMS_INSIDE_WISHLIST)
		click_on_correct_product_name_inside_wishlist = [x.click() for x in list_of_all_items_inside_wishlist if x.text == GET_PRODUCT_NAME]

		get_product_name_from_product_detail_page = el_id(driver, PRODUCT_NAME_TITLE).text

		# checking correctness of added product to checklist
		assert get_product_name_from_product_detail_page == GET_PRODUCT_NAME

	def future_test(self, driver):
		pass
		