#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy


#FUCTIONS:
# for mobile
def mob_wait_n_click(driver, locator):
	try: 
		WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator)).click()
	except:
		print(f"Element to click {locator} is not found")


# just wait
def wait(driver, locator):
	try:
		WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
	except:
		print(f"Element to wait {locator} is not found")

def short_wait(driver, locator):
	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
	except:
		print(f"Element to SHORT wait {locator} is not found, not critical, can be ignored")

def long_wait(driver, locator):
	try:
		WebDriverWait(driver, 100).until(EC.element_to_be_clickable(locator))
	except:
		print(f"Element to LONG wait {locator} is not found")


def long_wait_visible(driver, locator):
	try:
		WebDriverWait(driver, 100).until(EC.visibility_of_element_located(locator))
	except:
		print(f"Element to LONG wait visibility {locator} is not found")

def wait_clickable(driver, locator):
	try:
		WebDriverWait(driver, 100).until(EC.element_to_be_clickable(locator))
	except:
		print(f"Element to wait {locator} is not found")

#waits until element will be clickable and click on it
def wait_n_click(driver, locator):
	try: 
		WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator)).click()
	except:
		print(f"Element to click {locator} is not found")

#waits until element will be clickable, sends keywords
def send_keyz(driver, locator, keyz):
	try: 
		WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator)).send_keys(keyz)
	except:
		print(f"Element to enter value {locator} is not found")


def click_few_times(locator, clicks):
	if clicks == 1:
		locator.click()
	else:
		for i in range(clicks):
			locator.click()
			time.sleep(0.3)



# returns found element by xpath using js
def js_by_xpath(selenium, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	selenium.execute_script(js_xpath_func)
	elem = selenium.execute_script("return getElementByXpath(arguments[0])", locator)
	return elem

# check if checkbox is active (returns True or False)
def js_by_xpath_cbox_status(selenium, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	selenium.execute_script(js_xpath_func)
	elem = selenium.execute_script("return getElementByXpath(arguments[0]).checked", locator)
	return elem

# check if button is active (returns True or False)
def js_by_xpath_button_status(selenium, locator):
	js_xpath_func = '''
				window.getElementByXpath = function(path) {
					return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}
	'''
	selenium.execute_script(js_xpath_func)
	elem = selenium.execute_script("return getElementByXpath(arguments[0]).disabled", locator)
	return elem
