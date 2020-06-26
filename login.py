from selenium import webdriver
import time
import unittest
import HtmlTestRunner
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/VIJAYA/Desktop/webdrivers/chromedriver_win32/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("http://datamd-md-india.qa.i3systems.in/")
        self.driver.find_element_by_id("id_username").send_keys("admin")
        self.driver.find_element_by_id("id_password").send_keys("!3$y$+eMs")
        self.driver.find_element_by_class_name("btn").click()
        time.sleep(2)
    @classmethod
    def test_logout_valid(self):
        self.driver.find_element_by_id("logoutCaret").click()
        self.driver.find_element_by_link_text("Logout").click()    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close(cls)
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/VIJAYA/PycharmProjects/seleniump/pomproject/reports'))




