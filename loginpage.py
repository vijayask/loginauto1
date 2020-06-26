from pomproject.locators.locators import Locators
class LoginPage():

    def __init__(self,driver):
        self.driver = driver


        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = "id_password"
        self.login_button_class_name = "btn"

    def enter_username(self,username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys("admin")

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys("!3$y$+eMs")

    def click_login(self):
        self.driver.find_element_by_class_name(self.login_button_class_name).click()


