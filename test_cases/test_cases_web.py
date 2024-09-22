import time

import allure
import pytest

import page_objects.web_objects.main_store_page
from extensions.verifications import Verifications
from test_cases.conftest import eyes
from utilities import common_ops
from workflows import web_flows
from workflows.web_flows import WebFlows
from utilities.common_ops import wait, For, get_data
import test_cases.conftest as conf
import utilities.manage_pages as page



@pytest.mark.usefixtures('init_driver')
class TestCasesWeb:

    @allure.title('Test01: Get in to store page')
    @allure.description('Verify that go in to store successfully')
    def test_verify_get_in_to_store(self):
         WebFlows.get_in_to_store_page()
         Verifications.verify_equals(page.main_store_page.slider_bar_txt().text, 'Filter by Price')

    @allure.title('Test02: Check slider price')
    @allure.description('Verify that slider price range ok')
    def test_range_of_price(self):
         WebFlows.get_in_to_store_page()
         WebFlows.move_left_dot_in_slide_bar(int(get_data('MinPrice')), 0)
         WebFlows.move_right_dot_in_slide_bar(int(get_data('MaxPrice')), 0)
         Verifications.verify_equals(page.main_store_page.min_price_txt().text.split(" ")[0], get_data('MinPrice'))
         Verifications.verify_equals(page.main_store_page.max_price_txt().text.split(" ")[0], get_data('MaxPrice'))

    @allure.title('Test03: Check header menu appeared')
    @allure.description('Verify that header menu appeared')
    def test_header_menu(self):
        WebFlows.get_in_to_store_page()
        menu_list = WebFlows.verify_header_menu()
        Verifications.check_list_display(menu_list)

    @allure.title('Test04: Check mens category')
    @allure.description('Verify that mens category sorting correct by rating')
    def test_check_mens_rating_sorting(self):
        WebFlows.get_in_to_store_page()
        list_before_sort, list_after_sort = WebFlows.order_product_list()
        Verifications.verify_equals(list_before_sort, list_after_sort)

    @allure.title('Test05: Check number of item in store main page')
    @allure.description('Check the number of item after some selected filter or not filtered')
    @pytest.mark.parametrize('description,expected', web_flows.test_data)
    def test_search_number_of_items(self, description, expected):
        WebFlows.get_in_to_store_page()
        WebFlows.filter_by_text(description)
        Verifications.verify_equals(len(page.main_store_page.get_products_list()), int(expected))

    @allure.title('Test06: Visual test')
    @allure.description('This test by visual check filter use and sorted use')
    @pytest.mark.skipif(get_data('ApplitoolsSkip').lower() == 'yes', reason="Using Visual test skipped")
    def test_visual_test(self):
        conf.eyes.open(conf.driver, "Visual Test", "Check filter use and sorted use")
        WebFlows.get_in_to_store_page()
        WebFlows.verify_visual_items(get_data('SendToFilter'), common_ops.Sorted.SORT_BY_PRICE_LOW_TO_HIGH)
        conf.eyes.check_window("Filtered and sorted items")


    @allure.title('Test07: Choose item by value')
    @allure.description('Choose items to cart by value provided')
    def test_add_to_cart_by_value(self):
        WebFlows.get_in_to_store_page()
        WebFlows.filter_by_text(get_data('SendToFilter2').lower())
        WebFlows.choose_items_by_value(get_data('SendToFilter2.1'))
        WebFlows.go_to_cart()
        Verifications.verify_equals(page.cart_page.get_sub_total_price().text.split(" ")[0], "540.00")

    @allure.title('Test08: Test total payment with shipping')
    @allure.description('Test total payment with shipping')
    def test_total_payment_with_shipping(self):
        WebFlows.get_in_to_store_page()
        WebFlows.go_to_cart()
        sum, sum_with_ship_pay = WebFlows.verify_total_in_cart(common_ops.Shipping.DELIVERY_EXPRESS)
        Verifications.verify_equals(sum, float(get_data('ExpectedSubTotalPrice')))  # verify sum of list
        Verifications.verify_equals(page.cart_page.get_sub_total_price().text.split(' ')[0], get_data('ExpectedSubTotalPrice'))  # verify sub total price
        Verifications.verify_equals(sum_with_ship_pay, float(get_data('ExpectedSubTotalPrice')) + float(get_data('ShippingPayment')))
        time.sleep(3)

    @allure.title('Test09: Update quantity of item')
    @allure.description('Check if after change quantity of item to price also updated')
    def test_update_quantity(self):
        WebFlows.get_in_to_store_page()
        WebFlows.go_to_cart()
        after_update, before_update = WebFlows.update_quantity_cart_by_index(get_data('IndexNumberQuantityUpdate'), get_data('QuantityToInsert'))
        Verifications.verify_equals(after_update, before_update * int(get_data('QuantityToInsert')))

    @allure.title('Test10: Remove item from cart')
    @allure.description('Remove item from cart list by Index/Name/max of price per item')
    def test_remove_item(self):
        WebFlows.get_in_to_store_page()
        WebFlows.go_to_cart()
        WebFlows.remove_item(common_ops.RemoveBy.REMOVE_BY_NAME)



    def teardown_method(self):
        WebFlows.back_to_start_page(self)



