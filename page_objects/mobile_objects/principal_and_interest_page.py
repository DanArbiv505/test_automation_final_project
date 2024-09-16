from selenium.webdriver.common.by import By

principle_interest = (By.ID, "PrincipalInterest")
loan_amount = (By.ID, "tvLoanAmount")
total_amount = (By.ID, "tvTotalAmountToPayinYears")
total_interest = (By.ID, "tvInterestToPay")
save_button = (By.ID, "btnSave")
back_button = (By.ID, "btn_back")



class PrincipalAndInterestPage:

    def __init__(self, driver):
        self.driver = driver

    def get_principle_interest(self):
        return self.driver.find_element(principle_interest[0], principle_interest[1])

    def get_loan_amount(self):
        return self.driver.find_element(loan_amount[0], loan_amount[1])

    def get_total_amount(self):
        return self.driver.find_element(total_amount[0], total_amount[1])

    def get_total_interest(self):
        return self.driver.find_element(total_interest[0], total_interest[1])

    def get_save_button(self):
        return self.driver.find_element(save_button[0], save_button[1])

    def get_back_button(self):
        return self.driver.find_element(back_button[0], back_button[1])