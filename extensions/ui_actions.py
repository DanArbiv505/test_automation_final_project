import allure
import pygetwindow
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf

import test_cases.conftest


class UiActions:


    @staticmethod
    @allure.step('Click on element')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('Change element text')
    def change_text(elem: WebElement, value: str):
        elem.send_keys(value)


    # @staticmethod
    # def slider(elem: WebElement, x_offset: int, y_offset: int):
    #     conf.action.drag_and_drop_by_offset(elem, x_offset, y_offset).perform()

    @staticmethod
    @allure.step('Move slider')
    def slider(elem: WebElement, x_offset: int, y_offset: int):
        conf.action.click_and_hold(elem).move_by_offset(x_offset, y_offset).release().perform()

    @staticmethod
    @allure.step('Right click on element')
    def right_click(elem: WebElement):
        conf.action.context_click(elem).perform()

    @staticmethod
    @allure.step('Clear element text field')
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step('Mouse over two elements')
    def move_to(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Go to the previous page')
    def go_back():
        conf.driver.back()

    @staticmethod
    @allure.step('Long click and drag - electron')
    def long_click_and_drag(direction, elem):
        window_size = pygetwindow.getWindowsWithTitle('Electron')[0]
        window_width = window_size.width
        window_height = window_size.height
        x_start = None
        x_end = None

        if direction == 'right':
            x_start = int(window_width) * 0.1
            x_end = int(window_width) * 0.9
        elif direction == 'left':
            x_start = int(window_width) * 0.9
            x_end = int(window_width) * 0.1
        y_start = int(window_height) * 0.5
        ActionChains(conf.driver).click_and_hold(elem).move_by_offset(x_end, 0).release().perform()

    @staticmethod
    @allure.step('press enter - electron')
    def press_enter():
        conf.action.send_keys(Keys.RETURN).perform()

    @staticmethod
    @allure.step('drag and drop - electron')
    def drag_and_drop(elem1, elem2):
        conf.action.drag_and_drop(elem1,elem2).perform()

    @staticmethod
    @allure.step('Mouse over one element - electron')
    def move_to_electron(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).click().perform()