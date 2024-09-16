from selenium.webdriver.common.by import By

title = (By.ID, "textView7")
date_time = (By.ID, "tvDateAndTime")
principal_interest = (By.ID, "tvPrincipalAndInterest")
loan_amount = (By.ID, "tvLoanAmount")
total_amount = (By.ID, "tvTotalAmountToPay")
total_interest = (By.ID, "tvTotalInterest")
button_delete = (By.ID, "btnDelete")
button_share = (By.ID, "btnShare")
back_button = (By.ID, "btn_back")




class MortageHistory:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_elements(title[0], title[1])

    def get_date_time(self):
        return self.driver.find_elements(date_time[0], date_time[1])

    def get_principal_interest(self):
        return self.driver.find_elements(principal_interest[0], principal_interest[1])

    def get_loan_amount(self):
        return self.driver.find_elements(loan_amount[0], loan_amount[1])

    def get_total_amount(self):
        return self.driver.find_elements(total_amount[0], total_amount[1])

    def get_total_interest(self):
        return self.driver.find_elements(total_interest[0], total_interest[1])

    def get_button_delete(self):
        return self.driver.find_elements(button_delete[0], button_delete[1])

    def get_button_share(self):
        return self.driver.find_elements(button_share[0], button_share[1])

    def get_back_button(self):
        return self.driver.find_element(back_button[0], back_button[1])

