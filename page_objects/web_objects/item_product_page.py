from selenium.webdriver.common.by import By

add_to_cart = (By.NAME, "add-to-cart")



class ItemProductPage:

    def __init__(self, driver):
        self.driver = driver

    def get_add_to_cart(self):
        return self.driver.find_element(add_to_cart[0], add_to_cart[1])