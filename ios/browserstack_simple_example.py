from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
desired_cap = {
    # Set your access credentials
    "browserstack.user" : "mike_M1rIkt",
    "browserstack.key" : "x2YybDe3qVzH1M6tUpM4",
  
    # Set URL of the application under test
    "app" : "bs://0a9a501bfa181e9e455fd0aca15f534fa71f2c9a",
  
    # Specify device and os_version for testing
    "device" : "Xiaomi Redmi Note 9",
    "os_version" : "10.0",
      
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

ddd = driver.find_element(By.ID, "com.socialsuperstore:id/debugBtn")
ddd.click()

print("111")
time.sleep(2)
driver.quit()