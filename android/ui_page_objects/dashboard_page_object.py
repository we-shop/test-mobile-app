from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from locators.search_locators import *
from locators.product_detail_locators import *
from locators.dashboard_locators import *
from locators.profile_locators import *


class DashboardPage:
	def wenews_check(self, driver):
		# open dashboard > wenews
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)
		go_to_wenews_tab = acc_id_click(driver, DASHBOARD_WENEWS_TAB)

		# open first news item
		read_first_post_title = el_id(driver, DASH_WENEWS_POST_TITLE).text
		first_news_item_read_more_click = id_click(driver, DASH_WENEWS_READ_MORE_BTN)
		read_post_title_inside = el_xpath(driver, DASH_WENEWS_READ_MORE_POST_TITLE).text

		# check that title from preview is the same as inside post
		assert read_first_post_title == read_post_title_inside


	def new_acc_check(self, driver):
		# open dashboard > wenews
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)

		# check weshares tab stubs for new account
		assert el_id(driver, DASH_WESHARES_EMPTY_STUB_IMG).is_displayed()
		assert el_id(driver, DASH_WESHARES_EMPTY_STUB_TITLE).is_displayed()
		assert el_id(driver, DASH_WESHARES_EMPTY_STUB_TEXT).is_displayed()
		assert el_id(driver, DASH_WESHARES_BOTTOM_HINT).is_displayed()
		 
		# check transactions tab stubs for new account
		go_to_transactions_tab = acc_id_click(driver, DASHBOARD_TRANSACTIONS_TAB)
		assert el_id(driver, DASH_TRANS_EMPTY_PURCHASES_STUB).is_displayed()
		assert el_id(driver, DASH_TRANS_EMPTY_INFLUENCE_SALES_STUB).is_displayed()
		assert el_id(driver, DASH_TRANS_EMPTY_REFERRALS_STUB).is_displayed()
		assert el_id(driver, DASH_TRANS_ALERT_CONTAINER).is_displayed()


	def existing_acc_check(self, driver):
		# open dashboard > wenews
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)

		# check weshares tab stubs for new account
