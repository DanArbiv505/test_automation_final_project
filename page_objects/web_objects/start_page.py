from selenium.webdriver.common.by import By

shop_now = (By.XPATH, "//div[@data-id='78ab79a']")
find_more = (By.XPATH, "//div[@data-id='a3546f3']/div/div/a")
atid_college_link = (By.XPATH, "//a[@href='https://atidcollege.co.il/']")

class StartPage:

    def __init__(self, driver):
        self.driver = driver

    # shop now button
    def get_shop_now(self):
        return self.driver.find_element(shop_now[0], shop_now[1])

    # find more button
    def get_find_more(self):
        return self.driver.find_element(find_more[0], find_more[1])

    #atid college link
    def get_atid_college_link(self):
        return self.driver.find_element(atid_college_link[0], atid_college_link[1])



