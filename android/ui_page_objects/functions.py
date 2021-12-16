#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import string
import random
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
import pytest



# FUCTIONS FOR MOBILE
def id_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, locator))).click()
	except:
		print(f"Element to click by ID: {locator} is not found!")
		print(f"{ERROR}")

def xpath_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.XPATH, locator))).click()
	except:
		print(f"Element to click by XPATH: {locator} is not found!")
		print(f"{ERROR}")

def acc_id_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, locator)))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, locator))).click()
	except:
		print(f"Element to click by ACCESSIBILITY ID: {locator} is not found!")
		print(f"{ERROR}")

def el_id(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
		return driver.find_element(By.ID, locator)
	except:
		print(f"Element to find by ID: {locator} is not found!")
		print(f"{ERROR}")

def el_xpath(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		return driver.find_element(MobileBy.XPATH, locator)
	except:
		print(f"Element to find by XPATH: {locator} is not found!")
		print(f"{ERROR}")

def el_id_short_wait(driver, locator):
	try:
		WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, locator)))
		#return driver.find_element(By.ID, locator)
	except:
		#print(f"Element to find by ID (short wait): {locator} is not found!")
		print(f"{ERROR}")	

def el_acc_id(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, locator)))
		return driver.find_element(MobileBy.ACCESSIBILITY_ID, locator)
	except:
		print(f"Element to find by ACCESSIBILITY ID: {locator} is not found!")
		print(f"{ERROR}")

def elems_xpath(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator)))
		return driver.find_elements(MobileBy.XPATH, locator)
	except:
		print(f"Elements to find by XPATH: {locator} is not found!")
		print(f"{ERROR}")

def elems_id(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
		return driver.find_elements(By.ID, locator)
	except:
		print(f"Elements to find by XPATH: {locator} is not found!")
		print(f"{ERROR}")		

def id_until_gone(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, locator)))
	except:
		print(f"Elements by ID: {locator} is not gone!")
		print(f"{ERROR}")				

def id_keys(driver, locator, keys):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator))).send_keys(keys)
	except:
		print(f"Element to enter value by ID: {locator} is not found!")

def xpath_keys(driver, locator, keys):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, locator))).send_keys(keys)
	except:
		print(f"Element to enter value by XPATH: {locator} is not found!")

def acc_id_keys(driver, locator, keys):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, locator))).send_keys(keys)
	except:
		print(f"Element to enter value by ACCESSIBILITY ID: {locator} is not found!")

def get_toast_msg(driver):
	time.sleep(1.38) # obligatory wait, needed for script pause, between reading of 2 or more toast messages.
	return driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.Toast").text


# random letters
def rand_letters(count):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(count))

# NOT IN USE NOW
def click_few_times(locator, clicks):
	if clicks == 1:
		locator.click()
	else:
		for i in range(clicks):
			locator.click()
			time.sleep(0.3)



# returns found element by xpath using js
def js_by_xpath(driver, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	selenium.execute_script(js_xpath_func)
	elem = driver.execute_script("return getElementByXpath(arguments[0])", locator)
	return elem

# check if checkbox is active (returns True or False)
def js_by_xpath_cbox_status(driver, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	driver.execute_script(js_xpath_func)
	elem = driver.execute_script("return getElementByXpath(arguments[0]).checked", locator)
	return elem

# check if button is active (returns True or False)
def js_by_xpath_button_status(driver, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	driver.execute_script(js_xpath_func)
	elem = driver.execute_script("return getElementByXpath(arguments[0]).disabled", locator)
	return elem


def send_enter_key_adb(driver):
	driver.execute_script('mobile: shell', {'command': 'input keyevent', 'args':'KEYCODE_ENTER'}) # send Enter key example (using adb)

def get_correct_text_by_id(driver, locator, text):
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))

	seconds = 5

	while seconds > 0:
		el = driver.find_element(By.ID, locator).text
		if str(text) in el:
			break
		else:
			seconds -=1

	if seconds == 0:
		pytest.fail('Text not found!')


# FILE MANIPUPATION FUNCTIONS
def create_temp_file_and_write_data(data):
	file = open("temp_data.txt", "w+")
	file.write(str(data))
	file.close()

def read_data_from_temp_file():
	file = open("temp_data.txt", "r")
	return file.read()

def clear_data_from_temp_file():
	file = open("temp_data.txt", "w+")
	file.close()