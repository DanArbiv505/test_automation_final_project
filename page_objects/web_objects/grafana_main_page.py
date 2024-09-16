from selenium.webdriver.common.by import By

title = (By.XPATH, "//h1[contains(text(),'Welcome to Grafana')]")

class GrafanaMain:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(title[0], title[1])