from selenium.webdriver.common.by import By

home_page = (By.ID, "//*[@text='Home' and ./parent::*[@id='home']]")


class MenuRight:

    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        return self.driver.find_elements(home_page[0], home_page[1])