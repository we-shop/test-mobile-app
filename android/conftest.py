import pytest
import os
from ui_page_objects.login_page_object import LoginPage
from ui_page_objects.search_page_object import SearchPage
from ui_page_objects.debug_page_object import DebugPage
from ui_page_objects.product_detail_page_object import ProductDetailPage
from ui_page_objects.profile_page_object import ProfilePage
from ui_page_objects.post_page_object import PostPage


from dotenv import load_dotenv

load_dotenv()

# Read from file function
def get_data(data):
	return data.split("#")[0]

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL")


prefs = {"download.default_directory": os.getcwd() + "/"}

# Customizing appium driver (implicitly waits + app close/kill)
@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(12)
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

