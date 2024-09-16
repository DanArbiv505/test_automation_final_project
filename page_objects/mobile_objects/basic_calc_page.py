from selenium.webdriver.common.by import By

number_0 = (By.ID, "bu0")
number_1 = (By.ID, "bu1")
number_2 = (By.ID, "bu2")
number_3 = (By.ID, "bu3")
number_4 = (By.ID, "bu4")
number_5 = (By.ID, "bu5")
number_6 = (By.ID, "bu6")
number_7 = (By.ID, "bu7")
number_8 = (By.ID, "bu8")
number_9 = (By.ID, "bu9")
reset = (By.ID, "buac")
parentheses = (By.ID, "busign")
multiplication = (By.ID, "bumul")
plus = (By.ID, "buplus")
minus = (By.ID, "buminus")
divided = (By.ID, "budiv")
percentage = (By.ID, "bumod")
equal = (By.ID, "buequal")
dot = (By.ID, "budot")
text_calc = (By.ID, "input")
text_result = (By.ID, "output")
back_button = (By.ID, "backBtn")
color_button = (By.ID, "btnThemeChange")


class BasicCalcPage:

    def __init__(self, driver):
        self.driver = driver

    def get_number_0(self):
        return self.driver.find_element(number_0[0], number_0[1])

    def get_number_1(self):
        return self.driver.find_element(number_1[0], number_1[1])

    def get_number_2(self):
        return self.driver.find_element(number_2[0], number_2[1])

    def get_number_3(self):
        return self.driver.find_element(number_3[0], number_3[1])

    def get_number_4(self):
        return self.driver.find_element(number_4[0], number_4[1])

    def get_number_5(self):
        return self.driver.find_element(number_5[0], number_5[1])

    def get_number_6(self):
        return self.driver.find_element(number_6[0], number_6[1])

    def get_number_7(self):
        return self.driver.find_element(number_7[0], number_7[1])

    def get_number_8(self):
        return self.driver.find_element(number_8[0], number_8[1])

    def get_number_9(self):
        return self.driver.find_element(number_9[0], number_9[1])

    def get_parentheses(self):
        return self.driver.find_element(parentheses[0], parentheses[1])

    def get_multiplication(self):
        return self.driver.find_element(multiplication[0], multiplication[1])

    def get_plus(self):
        return self.driver.find_element(plus[0], plus[1])

    def get_minus(self):
        return self.driver.find_element(minus[0], minus[1])

    def get_divided(self):
        return self.driver.find_element(divided[0], divided[1])

    def get_percentage(self):
        return self.driver.find_element(percentage[0], percentage[1])

    def get_equal(self):
        return self.driver.find_element(equal[0], equal[1])

    def get_dot(self):
        return self.driver.find_element(dot[0], dot[1])

    def get_text_calc(self):
        return self.driver.find_element(text_calc[0], text_calc[1])

    def get_text_result(self):
        return self.driver.find_element(text_result[0], text_result[1])

    def get_back_button(self):
        return self.driver.find_element(back_button[0], back_button[1])

    def get_color_button(self):
        return self.driver.find_element(color_button[0], color_button[1])


