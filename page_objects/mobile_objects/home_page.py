from selenium.webdriver.common.by import By

basic_calc_page = (By.ID, "imageView161")
loan_calc_page = (By.ID, "ivNumberLookup1")
mortgage_page = (By.ID, "btnRecoverFiles1")
history_page = (By.ID, "iv_History")
right_menu_page = (By.ID, "iv_Drawer")
payment_first_page = (By.ID, "iv_Premium")
crown_image = (By.ID, "imageView9")


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_crown_image(self):
        return self.driver.find_element(crown_image[0], crown_image[1])

    def get_basic_calc_page(self):
        return self.driver.find_element(basic_calc_page[0], basic_calc_page[1])

    def get_loan_calc_page(self):
        return self.driver.find_element(loan_calc_page[0], loan_calc_page[1])

    def get_mortgage_page(self):
        return self.driver.find_element(mortgage_page[0], mortgage_page[1])

    def get_history_page(self):
        return self.driver.find_element(history_page[0], history_page[1])

    def get_right_menu_page(self):
        return self.driver.find_element(right_menu_page[0], right_menu_page[1])

    def get_payment_first_page(self):
        return self.driver.find_element(payment_first_page[0], payment_first_page[1])
