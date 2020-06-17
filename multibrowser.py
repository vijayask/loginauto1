
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/VIJAYA/Desktop/webdrivers/chromedriver_win32/chromedriver")

driver.implicitly_wait(5)
driver.maximize_window()



driver.get("http://datamd-md-india.qa.i3systems.in/")

driver.find_element_by_id("id_username").send_keys("admin")
driver.find_element_by_id("id_password").send_keys("!3$y$+eMs")

driver.find_element_by_class_name("btn").click()

driver.find_element_by_partial_link_text("Logout").click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")









