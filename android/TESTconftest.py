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


#caps for Browserstack
# "device" : "Samsung Galaxy S21",
# "os_version" : "11.0"

# {"app_url":"bs://576463a96efb0a64e20d5abe7652b5faa671aba4"}

# /* In your test script, use this "app_url" value to specify the application under test using the "app" capability. During test execution, your app will automatically be installed and launched on the device being tested. */

# caps.setCapability("app", "bs://576463a96efb0a64e20d5abe7652b5faa671aba4")


desired_cap = {
  "device" : "Samsung Galaxy A51",
  "os_version" : "10.0",
  "project" : "First Python project2", 
  "build" : "browserstack-build-13",
  "name" : "first_test222",
  "appPackage": "com.socialsuperstore",
  "appActivity": "com.socialsuperstore.ui.activity.LauncherActivity",  
  "app_url":"bs://30685e2517ddd3049429ddb20accdddb77403845",
  "browser" : "Chrome",
  "browserstack.idleTimeout":10,
  "implicit":8000,
  "autoGrantPermissions": True,
  "unicodeKeyboard": True,
  "noReset:": True,
  "resetKeyboard": True }


# Customizing appium driver for Browserstack
@pytest.fixture(autouse=True)
def selenium(request):
    webdriver
    selenium = webdriver.Remote(
      command_executor='https://mika_ajI75Z:3LEmS9BCLDd6zL4uzufk@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)

    yield selenium
    selenium.quit() # marking test is finished for Browserstack
    #selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
    clear_data_from_temp_file() # clearing data in temp_data.txt

# #Customizing appium driver (implicitly waits + app close/kill)
# @pytest.fixture
# def selenium(selenium):
#     #selenium = webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)
#     selenium.implicitly_wait(7)
#     yield selenium
#     #selenium.remove_app(app_id='com.socialsuperstore') # uninstalling app
#     #selenium.terminate_app('com.socialsuperstore') # put app in background
#     selenium.close_app() # making app in background, because of pre-sets app restoring in fresh state o next launch
#     clear_data_from_temp_file() # clearing data in temp_data.txt


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

