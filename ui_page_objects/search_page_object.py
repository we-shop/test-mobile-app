from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
from ui_page_objects.functions import *
from datetime import date
import datetime
import os


class SearchPage:
	def track_1(self, driver):
		print(driver.get_window_size())

	def track_2(self, driver):
		pass

	def negative_track_flow(self, driver):
		pass
