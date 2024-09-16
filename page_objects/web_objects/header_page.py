from selenium.webdriver.common.by import By

home = (By.XPATH, "//li[@id='menu-item-381']/a[text()='Home']")
store = (By.XPATH, "//li[@id='menu-item-45']/a")
men = (By.XPATH, "//li[@id='menu-item-266']/a")
women = (By.XPATH, "//li[@id='menu-item-267']/a")
accessories = (By.XPATH, "//li[@id='menu-item-671']/a")
about = (By.XPATH, "//li[@id='menu-item-828']/a")
contact_us = (By.XPATH, "//li[@id='menu-item-829']/a")


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    def get_home(self):
        return self.driver.find_element(home[0],home[1])

    def get_store(self):
        return self.driver.find_element(store[0],store[1])

    def get_men(self):
        return self.driver.find_element(men[0],men[1])


    def get_women(self):
        return self.driver.find_element(women[0],women[1])

    def get_accessories(self):
        return self.driver.find_element(accessories[0], accessories[1])

    def get_about(self):
        return self.driver.find_element(about[0], about[1])

    def get_contact_us(self):
        return self.driver.find_element(contact_us[0], contact_us[1])


