from selenium.webdriver.common.by import By

loan_amount = (By.ID, "editTextPrincipalLoanAmount")
interest_rate = (By.ID, "editTextInterestRate")
number_of_years = (By.ID, "editNoOfYearsInTerm")
calc_button = (By.ID, "btnCalculate")
back_button = (By.ID, "btn_back")



class LoanCalcPage:

    def __init__(self, driver):
        self.driver = driver

    def get_loan_amount(self):
        return self.driver.find_element(loan_amount[0], loan_amount[1])

    def get_interest_rate(self):
        return self.driver.find_element(interest_rate[0], interest_rate[1])

    def get_number_of_years(self):
        return self.driver.find_element(number_of_years[0], number_of_years[1])

    def get_calc_button(self):
        return self.driver.find_element(calc_button[0], calc_button[1])

    def get_back_button(self):
        return self.driver.find_element(back_button[0], back_button[1])