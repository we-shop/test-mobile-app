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
from locators.inbox_locators import *
from appium.webdriver.common.mobileby import By

class InboxPage:
	# def __init__(self, LOGIN_URL, LOGIN, PASSWORD):
	# 	self.LOGIN_URL = LOGIN_URL
	# 	self.LOGIN = LOGIN
	# 	self.PASSWORD = PASSWORD

	def inbox_check(self, driver):
		# checking inbox page
		is_inbox_messages = None
		go_to_inbox_click = acc_id_click(driver, FOOTER_ITEM_INBOX)
		#getting_all_inbox_message_titles = elems_id(driver, ALL_INBOX_TITLES)
		try:
			el_id_short_wait(driver, ALL_INBOX_TITLES)
			check_msgs = elems_id(driver, ALL_INBOX_TITLES)
			getting_all_inbox_message_titles = [i.text for i in check_msgs]
			is_inbox_messages = True
		except:
			# checking stun "No activity here, yet" in case when activity list is empty
			assert "No activity here, yet" in el_id(driver, NO_CONTENT_TEXT).text

		if is_inbox_messages:
			print(getting_all_inbox_message_titles)
		

		
		
		

		
		
		
		
		