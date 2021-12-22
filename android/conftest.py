import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage
from ui_page_objects.inbox_page_object import InboxPage
from appium import webdriver
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


# caps for Browserstack
# desired_cap = {
#   "device" : "Samsung Galaxy S21",
#   "os_version" : "11.0",
#   "project" : "First Python project2", 
#   "build" : "browserstack-build-13",
#   "name" : "first_test222",
#   "appPackage": "com.socialsuperstore",
#   "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",  
#   "app_url":"bs://c8bea125ce17fdddd57df2f6ff778e85a97ac175",
#   "browser" : "Chrome",
#   "browserstack.idleTimeout":10,
#   "implicit":8000,
#   "autoGrantPermissions": True,
#   "unicodeKeyboard": True,
#   "noReset:": True,
#   "resetKeyboard": True }


# #Customizing appium driver for Browserstack
# @pytest.fixture(autouse=True)
# def selenium(request):
#     webdriver
#     selenium = webdriver.Remote(
#       command_executor='https://mike_M1rIkt:x2YybDe3qVzH1M6tUpM4@hub-cloud.browserstack.com/wd/hub',
#       desired_capabilities=desired_cap)

#     yield selenium
#     selenium.quit() # marking test is finished for Browserstack
#     #selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
#     clear_data_from_temp_file() # clearing data in temp_data.txt

#Customizing appium driver (implicitly waits + app close/kill)
@pytest.fixture
def selenium(selenium):
    #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
    selenium.implicitly_wait(7)
    yield selenium
    #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
    #selenium.terminate_app('com.socialsuperstore') # put app in background
    selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt


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

@pytest.fixture()
def inbox_model(request):
  fixture = InboxPage()
  return fixture

