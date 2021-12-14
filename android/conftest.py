import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage
from selenium import webdriver
from ui_page_objects.functions import *


from dotenv import load_dotenv

load_dotenv()

# Read from file function
def get_data(data):
	return data.split("#")[0]

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL")


prefs = {"download.default_directory": os.getcwd() + "/"}

# desired_caps = {
#   "browserstack.user" : "mike_M1rIkt",
#   "browserstack.key" : "x2YybDe3qVzH1M6tUpM4",
#   "device" : "Xiaomi Redmi Note 9",
#   "os_version" : "10.0",
#   "project" : "First Python project", 
#   "build" : "browserstack-build-11",
#   "name" : "first_test11",
#   "app_url":"bs://0a9a501bfa181e9e455fd0aca15f534fa71f2c9a",
#   "autoGrantPermissions": True,
#   "unicodeKeyboard": True,
#   "noReset:": True,
#   "resetKeyboard": True
# }


#Customizing appium driver (implicitly waits + app close/kill)
@pytest.fixture
def selenium(selenium):
    #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
    selenium.implicitly_wait(12)
    yield selenium
    #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
    #selenium.terminate_app('com.socialsuperstore') # put app in background
    selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt




# { "capabilities": {
#   "browserstack.user" : "mike_M1rIkt",
#   "browserstack.key" : "x2YybDe3qVzH1M6tUpM4",
#   "device" : "Xiaomi Redmi Note 9",
#   "os_version" : "10.0",
#   "project" : "First Python project", 
#   "build" : "browserstack-build-11",
#   "name" : "first_test11",
#   "app_url":"bs://0a9a501bfa181e9e455fd0aca15f534fa71f2c9a",
#   "autoGrantPermissions": true,
#   "unicodeKeyboard": true,
#   "noReset:": false,
#   "resetKeyboard": true }
# }  

# # just for note purpose
# desired_caps2 = {
#   "appium:deviceName": "21f050e03a027ece",
#   "appium:platformName": "Android",
#   "appium:platformVersion": "10",
#   "appium:appPackage": "com.socialsuperstore",
#   #"appium:app": "C:\\Selen\\universal.apk",
#   #{"app_url":"bs://0a9a501bfa181e9e455fd0aca15f534fa71f2c9a"}
#   "appium:appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",
#   "appium:unicodeKeyboard": True,
#   "appium:resetKeyboard": True
# }

# mike_M1rIkt
# x2YybDe3qVzH1M6tUpM4


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

@pytest.fixture()
def product_page_model(request):
  fixture = ProductDetailPage()
  return fixture

@pytest.fixture()
def profile_model(request):
  fixture = ProfilePage(LOGIN_URL, LOGIN, PASSWORD)
  return fixture

@pytest.fixture()
def post_model(request):
  fixture = PostPage()
  return fixture

