import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import page_objects.web_objects.main_store_page
import extensions
import page_objects.web_objects.cart_page
import utilities
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications

from utilities.common_ops import get_data, read_from_csv , wait, For, Shipping
from utilities.manage_pages import ManagePages
import utilities.manage_pages as page



class WebFlows:

    @staticmethod
    @allure.step('Enter to main store page flow')
    def get_in_to_store_page():
        UiActions.click(page.start_page.get_shop_now())

    @staticmethod
    @allure.step('In store page verify "Filter by price text flow')
    def verify_slider_bar_text(expected):
        Verifications.verify_equals(page.main_store_page.slider_bar_txt().text, expected)

    @staticmethod
    @allure.step('Move left dot to set min price flow')
    def move_left_dot_in_slide_bar(x_offset, y_offset):
        UiActions.slider(page.main_store_page.slider_bar_action_left(), x_offset-30, y_offset)

    @staticmethod
    @allure.step('Move right dot to set max price flow')
    def move_right_dot_in_slide_bar(x_offset, y_offset):
        UiActions.slider(page.main_store_page.slider_bar_action_right(), x_offset-250, y_offset)

    @staticmethod
    @allure.step('Verify min and max price flow')
    def verify_min_max_price(expected_min, expected_max):
        Verifications.verify_equals(page.main_store_page.min_price_txt().text.split(" ")[0], expected_min)
        Verifications.verify_equals(page.main_store_page.max_price_txt().text.split(" ")[0], expected_max)

    @staticmethod
    @allure.step('Verify header menu displayed flow')
    def verify_header_menu():
        menu_list = [page.header_page.get_home(),
                     page.header_page.get_store(),
                     page.header_page.get_men(),
                     page.header_page.get_women(),
                     page.header_page.get_accessories(),
                     page.header_page.get_about(),
                     page.header_page.get_contact_us()
                     ]
        Verifications.check_list_display(menu_list)

    @staticmethod
    @allure.step('Back to start page flow')
    def back_to_start_page(self):
        self.driver.get(get_data('Url'))

    @staticmethod
    @allure.step('Check men items products are sorted by rating')
    def order_product_list():
        check_list = []
        # need to click on men
        UiActions.click(page.main_store_page.get_left_men())
        choose_val = Select(page.main_store_page.get_order_by_dropdown())
        choose_val.select_by_index(2)
        items = page.main_store_page.get_products_list_rating_in_page()
        pages_of_items = page.main_store_page.get_pages_numbers()
        #get rating of each product and put in list of all pages, then verify list is sorted
        for i in range(len(pages_of_items)-1):
             for item in items:
                if item.get_attribute('aria-label') is not None:
                   check_list.append(item.get_attribute('aria-label').split(" ")[1])
                else:
                   check_list.append('0.0')
             #if not last page, will continue to the next page of items
             if i < len(pages_of_items)-2:
                 UiActions.click(pages_of_items[len(pages_of_items)-1])
                 items = page.main_store_page.get_products_list_rating_in_page() # receive the new rating items in new page
        check_list_sorted = check_list
        check_list_sorted.sort()
        Verifications.verify_equals(check_list, check_list_sorted)

    @staticmethod
    @allure.step('Filter items by sending value flow')
    def filter_by_text(value):
        UiActions.change_text(page.main_store_page.get_search_field(), value)
        UiActions.click(page.main_store_page.get_search_button())

    @staticmethod
    @allure.step('Verify number of items as expected flow')
    def verify_size_of_item(expected):
        Verifications.verify_equals(len(page.main_store_page.get_products_list()), int(expected))

    @staticmethod
    @allure.step('Filter by some value and use sort by user decide - this test for applitools visual test')
    def verify_visual_items(filter_val, sorted_val):
        UiActions.change_text(page.main_store_page.get_search_field(), filter_val)
        UiActions.click(page.main_store_page.get_search_button())
        choose_val = Select(page.main_store_page.get_order_by_dropdown())
        choose_val.select_by_visible_text(sorted_val)

    @staticmethod
    @allure.step('Choose item by value')
    def choose_items_by_value(val_name):
        items = page.main_store_page.get_products_list_names()
        #for item in items:
        for i in range(len(items)):
            if val_name in items[i].text:
                UiActions.click(items[i])
                UiActions.click(page.item_product_page.get_add_to_cart())
                UiActions.go_back()
                UiActions.go_back()
                items = page.main_store_page.get_products_list_names()

    @staticmethod
    @allure.step('Verify items price')
    def verify_price_of_choose_items():
        #UiActions.move_to(page.main_store_page.get_view_cart(), page.main_store_page.get_view_cart_button())
         UiActions.click(page.main_store_page.get_view_cart())



    @staticmethod
    @allure.step('Verify total price and with delivery decision')
    def verify_total_in_cart(expected_sub_total, shipping, after_shipping_expected):
        sum = 0
        total_price_list = page.cart_page.get_total_list()
        for price in total_price_list:
            sum += float(price.text.split(' ')[0])
        Verifications.verify_equals(sum, float(expected_sub_total)) # verify sum of list
        Verifications.verify_equals(page.cart_page.get_sub_total_price().text.split(' ')[0], expected_sub_total) # verify sub total price
        # adding the shipping price
        ship_pay = utilities.common_ops.shipping_delivery(shipping)
        sum += ship_pay
        Verifications.verify_equals(sum, float(expected_sub_total) + float(after_shipping_expected))

    @staticmethod
    @allure.step('Update quantity cart')
    def update_quantity_cart_by_index(num_item, quantity_to_update):
        amount_of_item_before = page.cart_page.get_total_list()[int(num_item)].text.split(" ")[0]
        UiActions.clear(page.cart_page.get_quantity_of_item_in_cart()[int(num_item)])
        UiActions.change_text(page.cart_page.get_quantity_of_item_in_cart()[int(num_item)], quantity_to_update)
        UiActions.click(page.cart_page.get_update_carte())
        #time.sleep(5)
        wait(For.ELEMENT_EXIST, page_objects.web_objects.cart_page.alert)
        #wait(For.ELEMENT_EXIST, page.cart_page.alert)
        amount_of_item_after = page.cart_page.get_total_list()[int(num_item)].text.split(" ")[0]
        Verifications.verify_equals(float(amount_of_item_after), float(amount_of_item_before) * int(quantity_to_update))

    @staticmethod
    @allure.step('Remove item')
    def remove_item(way_of_remove):
        if way_of_remove == 'index':
            UiActions.click(page.cart_page.get_remove_item_button()[int(get_data('MoveByIndex'))])
        elif way_of_remove == 'name':
            item_names = page.cart_page.get_names_of_item_in_cart()
            for i in range(len(item_names)):
                if get_data('MoveByName') in item_names[i].text:
                    UiActions.click(page.cart_page.get_remove_item_button()[i])
        elif way_of_remove == 'maximum price':
            single_price_of_all_items = page.cart_page.get_price_of_single_item_in_cart()
            for i in range(len(single_price_of_all_items)):
                if float(single_price_of_all_items[i].text.split(" ")[0]) > float(get_data('MoveByMaxPrice')):
                    UiActions.click(page.cart_page.get_remove_item_button()[i])
        time.sleep(5)




data = read_from_csv(get_data('CSVLocation'))
test_data = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]
