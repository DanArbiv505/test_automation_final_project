from selenium.webdriver.common.by import By

default = (By.ID, "button11")
red = (By.ID, "button22")
orange = (By.ID, "button33")
purple = (By.ID, "button44")
light_blue = (By.ID, "button45")
pink = (By.ID, "button47")
back_button = (By.ID, "btnBack")




class ColorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_default(self):
        return self.driver.find_element(default[0], default[1])

    def get_red(self):
        return self.driver.find_element(red[0], red[1])

    def get_orange(self):
        return self.driver.find_element(orange[0], orange[1])

    def get_purple(self):
        return self.driver.find_element(purple[0], purple[1])

    def get_light_blue(self):
        return self.driver.find_element(light_blue[0], light_blue[1])

    def get_pink(self):
        return self.driver.find_element(pink[0], pink[1])


    def get_back_button(self):
        return self.driver.find_element(back_button[0], back_button[1])

