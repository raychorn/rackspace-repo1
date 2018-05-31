from selenium import webdriv
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://dev.example.rackspace.com")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("rackker")
password.send_keys("rackspace")

driver.find_elements_by_class_name("submit.button").click()

'''Unable to test the code at this point because the URL provided did not respond however we can assume the following'''

# close the browser window
driver.quit()
