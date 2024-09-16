from selenium.webdriver.common.by import By

email = (By.NAME, "user")
password = (By.NAME, "password")
login_button = (By.XPATH, "//button[@type='submit']")
skip = (By.XPATH, "//button[@type='button']/span")


class GrafanaLoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_email(self):
        return self.driver.find_element(email[0], email[1])

    def get_login_button(self):
        return self.driver.find_element(login_button[0], login_button[1])

    def get_skip(self):
        return self.driver.find_element(skip[0], skip[1])
