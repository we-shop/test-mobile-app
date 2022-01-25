from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from datetime import datetime
from ui_page_objects.functions import *
from locators.search_locators import *
from locators.product_detail_locators import *
from locators.dashboard_locators import *
from locators.profile_locators import *


class DashboardPage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD, LOGIN_NEW, PASSWORD_NEW):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD
		self.LOGIN_NEW = LOGIN_NEW
		self.PASSWORD_NEW = PASSWORD_NEW


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
		# open dashboard > weshares
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
		CURRENT_DATE = datetime.today().strftime('%d.%m.%y')

		# open dashboard
		go_to_dashboard = acc_id_click(driver, FOOTER_ITEM_DASHBOARD)

		# check weshares tab
		weshares_chart = el_id(driver, DASH_WESHARES_CHART)
		assert weshares_chart.is_displayed()

		last_updated = el_id(driver, DASH_WESHARES_LAST_UPDATED).text.split(", ")[1]
		assert last_updated == CURRENT_DATE
		
		share_price = float(el_id(driver, DASH_WESHARES_SHARE_PRICE).text.split("£")[1])
		assert share_price > 0

		your_weshare_top = float(el_id(driver, DASH_WESHARES_YOUR_WESHARE_TOP).text.split("£")[1])
		assert your_weshare_top > 100

		your_weshare_bottom = float(el_id(driver, DASH_WESHARES_YOUR_WESHARE_BOTTOM).text)
		assert your_weshare_bottom > 100

		# support URL check
		click_on_support_link = id_click(driver, DASH_WESHARES_SUPPORT_LINK)
		select_chrome_browser(driver)
		page_url_support = el_id(driver, BROWSER_URL_BAR).text
		assert page_url_support == "help.we.shop/en/"
		driver.back()

		# switch to transactions tab
		click_on_transactions_tab = acc_id_click(driver, DASHBOARD_TRANSACTIONS_TAB)

		# check purchases
		"com.socialsuperstore:id/youPurchasesLoadMore"
		"com.socialsuperstore:id/dashboardTransactionTitle"
		"com.socialsuperstore:id/dashboardTransactionPrice"
		driver.back()

		# check influenced sales
		"com.socialsuperstore:id/influencedSalesLoadMore"
		"com.socialsuperstore:id/dashboardTransactionTitle"
		"com.socialsuperstore:id/dashboardTransactionPrice"
		driver.back()

		# check refferals
		"com.socialsuperstore:id/friendsReferredLoadMore"
		"com.socialsuperstore:id/referralsHeader"
		"com.socialsuperstore:id/nickInput"
		"com.socialsuperstore:id/dashboardTransactionTitle"
