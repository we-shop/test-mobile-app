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
	def followings_followers_count(self, driver):
		# read count of followers and following
		profile_followers = int(el_id(driver, FOLLOWERS_COUNT).text)
		profile_following = int(el_id(driver, FOLLOWINGS_COUNT).text)

		# going to followers/following and reading real count of followers/following
		click_on_followers_btn = id_click(driver, FOLLOWERS_LABEL_PROFILE)
		total_count_of_existing_followers = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))
		click_on_following_tab = acc_id_click(driver, PROFILE_FOLLOWERS_TAB_FOLLOWINGS_TAB)
		total_count_of_existing_following = len(elems_xpath(driver, PROFILE_FOLLOWERS_TAB_ALL_ITEMS))

		# assertion of real and readed count of followers/following
		assert profile_followers == total_count_of_existing_followers
		assert profile_following == total_count_of_existing_following

	def future_test(self, driver):
		pass
