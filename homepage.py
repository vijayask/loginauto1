class HomePage():
    def __init__(self,driver):
        self.driver = driver


        self.downarrow_link_id = "logoutCaret"
        self.logout_link_linkText = "Logout"


    def click_downarrow(self):
        self.driver.find_element_by_id(self.downarrow_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()

