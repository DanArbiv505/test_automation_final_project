from selenium.webdriver.common.by import By

home_price = (By.ID, "etHomePrice")
down_payment = (By.ID, "etDownPayment")
years_of_loan_10 = (By.ID, "tv10Years")
years_of_loan_15 = (By.ID, "tv15Years")
years_of_loan_20 = (By.ID, "tv20Years")
years_of_loan_30 = (By.ID, "tv30Years")
interest_rate = (By.ID, "etInterestRate")
calc_button = (By.ID, "btnCalculateMortgage")
back_button = (By.ID, "btn_back")



class MortgageCalcPage:

    def __init__(self, driver):
        self.driver = driver

    def get_home_price(self):
        return self.driver.find_element(home_price[0], home_price[1])

    def get_down_payment(self):
        return self.driver.find_element(down_payment[0], down_payment[1])

    def get_years_of_loan_10(self):
        return self.driver.find_element(years_of_loan_10[0], years_of_loan_10[1])

    def get_years_of_loan_15(self):
        return self.driver.find_element(years_of_loan_15[0], years_of_loan_15[1])

    def get_years_of_loan_20(self):
        return self.driver.find_element(years_of_loan_20[0], years_of_loan_20[1])

    def get_years_of_loan_30(self):
        return self.driver.find_element(years_of_loan_30[0], years_of_loan_30[1])

    def get_interest_rate(self):
        return self.driver.find_element(interest_rate[0], interest_rate[1])

    def get_calc_button(self):
        return self.driver.find_element(calc_button[0], calc_button[1])

    def get_back_button(self):
        return self.driver.find_element(back_button[0], back_button[1])