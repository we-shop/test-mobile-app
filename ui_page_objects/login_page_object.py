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


class LoginPage:
	def __init__(self, LOGIN_URL, LOGIN, PASSWORD):
		self.LOGIN_URL = LOGIN_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD

	def login(self, driver):
		driver.implicitly_wait(1.5)
		driver.get(self.LOGIN_URL)

	def logout(self, driver):
		pass



