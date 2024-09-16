import allure
import pytest

import page_objects.mobile_objects.payment_first_page
from extensions.mobile_actions import MobileActions
from utilities.common_ops import get_data, wait, For
from workflows.mobile_flows import MobileFlows
import utilities.manage_pages as page


@pytest.mark.usefixtures('init_mobile_driver')
class TestCasesMobile:

    @allure.title('Test01: Check swipe on element')
    @allure.description('Do swipe on logo in home page')
    def test_logo_swipe(self):
       MobileFlows.close_payment_page()
       MobileFlows.swipe_logo_home(page.home_page.get_crown_image(), get_data('DirectionSwipe'))

    @allure.title('Test02: Choose color and perform calculation')
    @allure.description('Choose purple color and perform calculation')
    def test_create_calc(self):
        MobileFlows.perform_basic_calc(get_data('Operator1'), get_data('Operand'), get_data('Operator2'), '20')

    @allure.title('Test03: Add data to mortgage calculation')
    @allure.description('Add data to mortgage calculation and verify total interest')
    def test_mortgage_loan(self):
        MobileFlows.mortgage_calc('200000', '500', '15',  '3.5')

    @allure.title('Test04: Delete item in history')
    @allure.description('Delete an item in history of mortgage loan')
    def test_delete_history_loan(self):
        MobileFlows.delete_item_by_index(get_data('IndexToDelete'))
