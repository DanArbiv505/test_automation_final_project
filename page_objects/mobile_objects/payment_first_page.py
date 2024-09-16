from selenium.webdriver.common.by import By

close_page = (By.XPATH, "//*[@id='btnCross']")
title_text = (By.XPATH, "//*[@text='Premium Plan']")


class PaymentFirstPage:

    def __init__(self, driver):
        self.driver = driver

    def get_close_page(self):
        return self.driver.find_element(close_page[0], close_page[1])

    def get_title_text(self):
        return self.driver.find_element(title_text[0], title_text[1])

