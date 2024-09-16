import csv
import time

from selenium.webdriver.support.wait import WebDriverWait
import test_cases.conftest as conf
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
from extensions.ui_actions import UiActions
from utilities import manage_pages


# Function to handle various types of wait for web elements
def wait(type_of_wait, elem):
    if type_of_wait == 'element_exist':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif type_of_wait == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located((elem[0], elem[1])))
    elif type_of_wait == 'element_to_be_selected':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.element_located_to_be_selected((elem[0], elem[1])))


# Enum for selecting the type of wait for element (by tuple in this case)
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_TO_BE_CLICKABLE = 'element_to_be_clickable'
    TITLE_IS = 'title is'
    TITLE_CONTAINS = 'title_contains'
    TEXT_TO_BE_PRESENT_IN_ELEMENT = 'text_to_be_present_in_element'
    ALERT_IS_PRESENT = 'alert_is_present'
    ELEMENT_TO_BE_SELECTED = 'element_to_be_selected'


# Function to fetch data from an XML file
# It reads a specific node (based on node_name) and retrieves the associated value
def get_data(node_name):
    root = ET.parse('C:/Automation/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

# Function to read data from a CSV file and return it as a list of rows
# Each row is appended to the 'rows' list
def read_from_csv(file_name):
    rows = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            rows.append(row)
    return rows

# Function to return the current time stamp (used for generating unique values, logs, etc.)
def get_time_stamp():
    return time.time()

# Enum class to represent different sorting options for products
class Sorted:
    NO_SORTED = 'Relevance'
    SORT_BY_POPULARITY = 'Sort by popularity'
    SORT_BY_AVERAGE_RATING = 'Sort by average rating'
    SORT_BY_LATEST = 'Sort by latest'
    SORT_BY_PRICE_LOW_TO_HIGH = 'Sort by price: low to high'
    SORT_BY_PRICE_HIGH_TO_LOW = 'Sort by price: high to low'

# Enum class to represent different shipping methods
class Shipping:
    FREE_SHIPPING = 'Free shipping'
    LOCAL_PICKUP = 'Local pickup'
    DELIVERY_EXPRESS = 'Delivery express'
    REGISTERED_MAIL = 'Registered mail'


# Function to select a shipping method and calculate the shipping cost based on the selection
def shipping_delivery(shipping):
    if shipping == 'Free shipping':
        ship_pay = 0
    elif shipping == 'Local pickup':
        ship_pay = 0
        UiActions.click(manage_pages.cart_page.get_local_pickup())
    elif shipping == 'Delivery express':
        UiActions.click(manage_pages.cart_page.get_delivery_express())
        ship_pay = float(manage_pages.cart_page.get_delivery_express().text.split(" ")[6])
    elif shipping == 'Registered mail':
        UiActions.click(manage_pages.cart_page.get_registered_mail())
        ship_pay = float(manage_pages.cart_page.get_registered_mail().text.split(" ")[6])
    return ship_pay


# Enum class for different removal strategies (removing items from a cart)
class RemoveBy:
    REMOVE_BY_INDEX = 'index'
    REMOVE_BY_NAME = 'name'
    REMOVE_BY_MAX_PRICE = 'maximum price'

# Enum class to represent different loan/mortgage durations (in years)
class Years:
    TEN_YEARS = '10'
    FIFTEEN_YEARS = '15'
    TWENTY_YEARS = '20'
    THIRTY_YEARS = '30'

# Enum class to represent directions (used for navigate left or right)
class Direction:
    LEFT = 'left'
    RIGHT = 'right'







