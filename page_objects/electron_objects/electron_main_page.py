from selenium.webdriver.common.by import By

create_task = (By.XPATH, "//input[@placeholder='Create a task']")
task_list = (By.CSS_SELECTOR, "div[class='view_2Ow90']")
delete_buttons = (By.CSS_SELECTOR, "div[class='view_2Ow90']>svg")
drag_buttons = (By.CSS_SELECTOR, "div[class='taskWrapper_2u8dN']>svg")
title_of_task_list = (By.CSS_SELECTOR, "div[class='view_2Ow90']>div>label")
complete_task_button = (By.CSS_SELECTOR, "div[class='view_2Ow90']>label>svg")
no_task = (By.CSS_SELECTOR, "h2[class='emptyState_3FwtK']")
color_dropdown = (By.CSS_SELECTOR, "svg[viewBox='0 0 30 14']")
red_color = (By.XPATH, "//div[@class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']/span[2]")
no_color = (By.XPATH, "//div[@class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']/span[1]")



class ElectronMainPage():

    def __init__(self, driver):
        self.driver = driver

    def get_create_task(self):
        return self.driver.find_element(create_task[0], create_task[1])

    def get_task_list(self):
        return self.driver.find_elements(task_list[0], task_list[1])

    def get_delete_buttons(self):
        return self.driver.find_elements(delete_buttons[0], delete_buttons[1])

    def get_drag_buttons(self):
        return self.driver.find_elements(drag_buttons[0], drag_buttons[1])

    def get_title_of_task_list(self):
        return self.driver.find_elements(title_of_task_list[0], title_of_task_list[1])

    def get_complete_task_button(self):
        return self.driver.find_elements(complete_task_button[0], complete_task_button[1])

    def get_no_task(self):
        return self.driver.find_element(no_task[0], no_task[1])

    def get_color_dropdown(self):
        return self.driver.find_element(color_dropdown[0], color_dropdown[1])

    def get_red_color(self):
        return self.driver.find_element(red_color[0], red_color[1])

    def get_no_color(self):
        return self.driver.find_element(no_color[0], no_color[1])

