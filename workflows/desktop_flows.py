import allure
import utilities.manage_pages as page

from extensions.ui_actions import UiActions
from extensions.verifications import Verifications


class DesktopFlows():

    @staticmethod
    @allure.step('perform calculate  on a given string')
    def get_calculate(input):
        for val in input:
            DesktopFlows.click_relevant_button(val)
        UiActions.click(page.desktop_calculator_app.get_equals())
        return DesktopFlows.get_result()

    @staticmethod
    @allure.step('choose the operator or operand to click')
    def click_relevant_button(value):
        if value == '0':
            UiActions.click(page.desktop_calculator_app.get_zero())
        if value == '1':
            UiActions.click(page.desktop_calculator_app.get_one())
        if value == '2':
            UiActions.click(page.desktop_calculator_app.get_two())
        if value == '3':
            UiActions.click(page.desktop_calculator_app.get_three())
        if value == '4':
            UiActions.click(page.desktop_calculator_app.get_four())
        if value == '5':
            UiActions.click(page.desktop_calculator_app.get_five())
        if value == '6':
            UiActions.click(page.desktop_calculator_app.get_six())
        if value == '7':
            UiActions.click(page.desktop_calculator_app.get_seven())
        if value == '8':
            UiActions.click(page.desktop_calculator_app.get_eight())
        if value == '9':
            UiActions.click(page.desktop_calculator_app.get_nine())
        if value == '+':
            UiActions.click(page.desktop_calculator_app.get_plus())
        if value == '-':
            UiActions.click(page.desktop_calculator_app.get_minus())
        if value == '*':
            UiActions.click(page.desktop_calculator_app.get_multiply())
        if value == '/':
            UiActions.click(page.desktop_calculator_app.get_divided())

    @staticmethod
    @allure.step('get result')
    def get_result():
        result = page.desktop_calculator_app.get_result().text.split(" ")[2]
        return result

    def teardown_method(self):
        page.desktop_calculator_app.get_clear()