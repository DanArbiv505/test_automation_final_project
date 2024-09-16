import test_cases.conftest as conf
from page_objects.desktop_objects.desktop_calculator_main import CalculatorApp
from page_objects.electron_objects.electron_main_page import ElectronMainPage
from page_objects.mobile_objects.basic_calc_page import BasicCalcPage
from page_objects.mobile_objects.color_page import ColorPage
from page_objects.mobile_objects.home_page import HomePage
from page_objects.mobile_objects.loan_calc_page import LoanCalcPage
from page_objects.mobile_objects.menu_right_page import MenuRight
from page_objects.mobile_objects.mortgage_calc_page import MortgageCalcPage
from page_objects.mobile_objects.mortgage_history_page import MortageHistory
from page_objects.mobile_objects.payment_first_page import PaymentFirstPage
from page_objects.mobile_objects.principal_and_interest_page import PrincipalAndInterestPage
from page_objects.web_objects.cart_page import CartPage
from page_objects.web_objects.grafana_login_page import GrafanaLoginPage
from page_objects.web_objects.grafana_main_page import GrafanaMain
from page_objects.web_objects.header_page import HeaderPage
from page_objects.web_objects.item_product_page import ItemProductPage
from page_objects.web_objects.main_store_page import MainStorePage
from page_objects.web_objects.start_page import StartPage

# Web page instances (used for initializing and interacting with various web pages)
start_page = None
main_store_page = None
header_page = None
item_product_page = None
cart_page = None

# Grafana page related to database part (used for initializing Grafana related pages)
grafana_db_page = None
grafana_main_page = None

# Mobile page instances (used for initializing and interacting with various mobile pages)
basic_calc_page = None
color_page = None
home_page = None
loan_calc_page = None
menu_right_page = None
mortgage_calc_page = None
mortgage_history_page = None
payment_first_page = None
principal_and_interest_page = None

# Electron page instance (used for initializing and interacting with Electron app pages)
electron_page = None

# Desktop application instance (used for initializing and interacting with desktop applications)
desktop_calculator_app = None


class ManagePages:

    @staticmethod
    def init_web_pages():

        # Initialize all web-related page objects by creating global instances of them.
        # ach page object is associated with a driver (conf.driver) for interacting with the page.


        globals()['start_page'] = StartPage(conf.driver)
        globals()['main_store_page'] = MainStorePage(conf.driver)
        globals()['header_page'] = HeaderPage(conf.driver)
        globals()['item_product_page'] = ItemProductPage(conf.driver)
        globals()['cart_page'] = CartPage(conf.driver)
        globals()['grafana_db_page'] = GrafanaLoginPage(conf.driver)
        globals()['grafana_main_page'] = GrafanaMain(conf.driver)


    @staticmethod
    def init_mobile_pages():

        # Initialize all mobile-related page objects by creating global instances of them.
        # Each page object represents a specific screen or feature in the mobile application.

        globals()['basic_calc_page'] = BasicCalcPage(conf.driver)
        globals()['color_page'] = ColorPage(conf.driver)
        globals()['home_page'] = HomePage(conf.driver)
        globals()['loan_calc_page'] = LoanCalcPage(conf.driver)
        globals()['menu_right_page'] = MenuRight(conf.driver)
        globals()['mortgage_calc_page'] = MortgageCalcPage(conf.driver)
        globals()['mortgage_history_page'] = MortageHistory(conf.driver)
        globals()['payment_first_page'] = PaymentFirstPage(conf.driver)
        globals()['principal_and_interest_page'] = PrincipalAndInterestPage(conf.driver)


    @staticmethod
    def init_electron_pages():

        # Initialize Electron app-related page objects by creating a global instance.
        # This is used to interact with the main Electron application page.

        globals()['electron_page'] = ElectronMainPage(conf.driver)

    @staticmethod
    def init_desktop_pages():

        # Initialize desktop application-related page objects by creating a global instance.
        # This is used for interacting with desktop applications like the Calculator app.

        globals()['desktop_calculator_app'] = CalculatorApp(conf.driver)
