import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    @allure.step('Verify if two values are equals')
    def verify_equals(actual, expected):
        assert actual == expected, f'Verify Equals Failed, Actual: {actual} is not equals to Expected: {expected}'

    @staticmethod
    @allure.step('Verify if element is display')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Element: {elem.text} is not displayed'

    @staticmethod
    @allure.step('Verify element is not display')
    def is_not_displayed(elem: WebElement):
        assert not elem.is_displayed(), f'Element: {elem.text} is displayed'

    @staticmethod
    @allure.step('Verify sub value is in value')
    def is_in(sub, full):
        assert sub in full, f'{sub} is not in {full}'

    @staticmethod
    @allure.step('Check all elements in list displayed')
    def check_list_display(elem_list):
        for i in range(len(elem_list)):
            soft_assert(elem_list[i].is_displayed(),f"Element of: {elem_list[i].text} not displayed.")

        verify_expectations()

    @staticmethod
    @allure.step('Check equal of number of checks with soft assertion')
    def verify_equal_with_soft_assert(val1, val2):
        soft_assert(val1 == val2, f"{val1} is not equal to {val2}")
