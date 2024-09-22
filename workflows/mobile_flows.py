import allure
import pytest


from extensions.mobile_actions import MobileActions
import page_objects.mobile_objects.payment_first_page
import page_objects.mobile_objects.principal_and_interest_page
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import get_data, wait, For
import page_objects.mobile_objects.mortgage_history_page


class MobileFlows:

    @staticmethod
    @allure.step('Close the payment page')
    def close_payment_page():
        wait(For.ELEMENT_EXIST, page_objects.mobile_objects.payment_first_page.title_text)
        MobileActions.tap(page.payment_first_page.get_close_page(),1)

    @staticmethod
    @allure.step('Swipe the payment logo in home page')
    def swipe_logo_home(elem, direction):
        x_start = None
        x_end = None
        y_start = None
        y_end = None

        if direction == 'right':
            x_start = elem.rect['x'] + elem.rect['width'] * 0.1
            x_end = elem.rect['x'] + elem.rect['width'] * 0.9
            y_start = elem.rect['y'] + elem.rect['height'] / 2
            y_end = y_start
        elif direction == 'left':
            x_start = elem.rect['x'] + elem.rect['width'] * 0.9
            x_end = elem.rect['x'] + elem.rect['width'] * 0.1
            y_start = elem.rect['y'] + elem.rect['height'] / 2
            y_end = y_start
        MobileActions.swipe(x_start, y_start, x_end, y_end, int(get_data('DurationSwipe')))

    @staticmethod
    @allure.step('Go to basic calculator, switch color and perform calculation')
    def perform_basic_calc(operator1, operand, operator2, expected):
        MobileActions.tap(page.home_page.get_basic_calc_page(),1)
        MobileActions.click(page.basic_calc_page.get_color_button())
        MobileActions.click(page.color_page.get_purple())
        if operator1 == '0':
            MobileActions.click(page.basic_calc_page.get_number_0())
        elif operator1 == '1':
            MobileActions.click(page.basic_calc_page.get_number_1())
        elif operator1 == '2':
            MobileActions.click(page.basic_calc_page.get_number_2())
        elif operator1 == '3':
            MobileActions.click(page.basic_calc_page.get_number_3())
        elif operator1 == '4':
            MobileActions.click(page.basic_calc_page.get_number_4())
        elif operator1 == '5':
            MobileActions.click(page.basic_calc_page.get_number_5())
        elif operator1 == '6':
            MobileActions.click(page.basic_calc_page.get_number_6())
        elif operator1 == '7':
            MobileActions.click(page.basic_calc_page.get_number_7())
        elif operator1 == '8':
            MobileActions.click(page.basic_calc_page.get_number_8())
        elif operator1 == '9':
            MobileActions.click(page.basic_calc_page.get_number_9())

        if operand == '+':
            MobileActions.click(page.basic_calc_page.get_plus())
        elif operand == '-':
            MobileActions.click(page.basic_calc_page.get_minus())
        elif operand == '*':
            MobileActions.click(page.basic_calc_page.get_multiplication())
        elif operand == '/':
            MobileActions.click(page.basic_calc_page.get_divided())

        if operator2 == '0':
            MobileActions.click(page.basic_calc_page.get_number_0())
        elif operator2 == '1':
            MobileActions.click(page.basic_calc_page.get_number_1())
        elif operator2 == '2':
            MobileActions.click(page.basic_calc_page.get_number_2())
        elif operator2 == '3':
            MobileActions.click(page.basic_calc_page.get_number_3())
        elif operator2 == '4':
            MobileActions.click(page.basic_calc_page.get_number_4())
        elif operator2 == '5':
            MobileActions.click(page.basic_calc_page.get_number_5())
        elif operator2 == '6':
            MobileActions.click(page.basic_calc_page.get_number_6())
        elif operator2 == '7':
            MobileActions.click(page.basic_calc_page.get_number_7())
        elif operator2 == '8':
            MobileActions.click(page.basic_calc_page.get_number_8())
        elif operator2 == '9':
            MobileActions.click(page.basic_calc_page.get_number_9())

        MobileActions.click(page.basic_calc_page.get_equal())

        Verifications.verify_equals(page.basic_calc_page.get_text_result().text, expected)
        MobileActions.tap(page.basic_calc_page.get_back_button(),1)


    @staticmethod
    @allure.step('Delete item if exist by index')
    def delete_item_by_index(index):
        try:
          MobileActions.click(page.mortgage_history_page.get_button_delete()[int(index)])
        except:
            pytest.fail("Index do not exist")

    @staticmethod
    @allure.step('Calc in Mortgage calculation')
    def mortgage_calc(price, payment, years, rate):
        MobileActions.tap(page.home_page.get_mortgage_page(), 1)
        MobileActions.change_text(page.mortgage_calc_page.get_home_price(), price)
        MobileActions.clear(page.mortgage_calc_page.get_down_payment())
        MobileActions.change_text(page.mortgage_calc_page.get_down_payment(), payment)
        if years == '10':
             MobileActions.tap(page.mortgage_calc_page.get_years_of_loan_10(), 1)
        elif years == '15':
             MobileActions.tap(page.mortgage_calc_page.get_years_of_loan_15(), 1)
        elif years == '20':
             MobileActions.tap(page.mortgage_calc_page.get_years_of_loan_20(), 1)
        elif years == '30':
             MobileActions.tap(page.mortgage_calc_page.get_years_of_loan_30(), 1)

        MobileActions.change_text(page.mortgage_calc_page.get_interest_rate(), rate)
        MobileActions.tap(page.mortgage_calc_page.get_calc_button(), 1)

        wait(For.ELEMENT_EXIST, page_objects.mobile_objects.principal_and_interest_page.principle_interest)
        expected = page.principal_and_interest_page.get_total_interest().text
        MobileActions.click(page.principal_and_interest_page.get_save_button())
        wait(For.ELEMENT_EXIST, page_objects.mobile_objects.mortgage_history_page.title)
        #items_size = len(page.mortgage_history_page.get_total_interest())
        Verifications.verify_equals(page.mortgage_history_page.get_total_interest()[0].text.split(" ")[2], expected)






