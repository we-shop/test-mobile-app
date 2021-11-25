import pytest
import os
from appium import webdriver
#from selenium import webdriver
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage

# Read from file function
def get_data(data):
	return data.split("#")[0]

# Open settings file
f = open("credentials.txt", "r")
lines = f.readlines()
LOGIN = get_data(lines[0])
PASSWORD = get_data(lines[1])
LOGIN_URL = get_data(lines[2])
f.close()


prefs = {"download.default_directory": os.getcwd() + "/"}

# Customizing appium driver (implicitly waits + app close/kill)
@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    yield selenium
    #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
    #selenium.terminate_app('com.socialsuperstore') # put app in background
    selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch

# just for note purpose
desired_caps = {
  "appium:deviceName": "21f050e03a027ece",
  "appium:platformName": "Android",
  "appium:platformVersion": "10",
  "appium:appPackage": "com.socialsuperstore",
  #"appium:app": "C:\\Selen\\universal.apk",
  "appium:appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",
  "appium:unicodeKeyboard": True,
  "appium:resetKeyboard": True
}


#FIXTURES PAGE OBJECT
@pytest.fixture()
def login_model(request):
	fixture = LoginPage(LOGIN_URL, LOGIN, PASSWORD)
	return fixture

@pytest.fixture()
def debug_model(request):
	fixture = DebugPage()
	return fixture

@pytest.fixture()
def search_model(request):
  fixture = SearchPage()
  return fixture
