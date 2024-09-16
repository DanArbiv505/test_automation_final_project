import time

import allure
import appium.webdriver
import mysql.connector

import pytest
import selenium
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages

driver = None
action = None
action2 = None
multi_action = None
db_connect = None
eyes = Eyes()

#
@pytest.fixture(scope='class')
def init_driver(request):
    edriver = get_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    if get_data('WorkOnDB') == 'yes':  # use for test grafana login web page with DB connection
        driver.get(get_data('Url_Grafana'))
    else:
        driver.get(get_data('Url')) # use for test atid college app
    globals()['action'] = ActionChains(driver)
    request.cls.driver = driver
    globals()['window_size'] = driver.get_window_size()
    ManagePages.init_web_pages()  # initializes the web pages with the driver
    if get_data('ApplitoolsSkip') == 'no':
        eyes.api_key = get_data('ApplitoolsKey')
    yield
    if get_data('ApplitoolsSkip').lower() == 'no':
        eyes.close()
        eyes.abort()
    time.sleep(3)
    driver.quit()


@pytest.fixture(scope='class')
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    ManagePages.init_mobile_pages()  # initializes the mobile pages with the driver
    globals()['action'] = TouchAction(driver)
    #request.cls.action = action
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['multi_action'] = MultiAction(driver)
    request.cls.multi_action = globals()['multi_action']
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(get_data('WaitTime'))
    request.cls.driver = driver
    ManagePages.init_electron_pages()  # initializes the electron pages with the driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(get_data('WaitTime'))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()  # initializes the desktop pages with the driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_database_connection(request):
    db_connect = mysql.connector.connect(
        host=get_data('DB_Host'),
        database=get_data('DB_Name'),
        user=get_data('DB_User'),
        password=get_data('DB_Password')
    )
    globals()['db_connect'] = db_connect
    request.cls.db_connect = db_connect
    yield
    db_connect.close()

def get_driver():
    web_driver = get_data('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong input, Unrecognized browser')
    return driver


def get_mobile_driver():
    if get_data('Mobile_Device').lower() == 'android':
        mob_driver = get_android(get_data('Udid'))
    elif get_data('Mobile_Device').lower() == 'ios':
        mob_driver = get_ios(get_data('Udid'))
    else:
        mob_driver = None
        raise Exception('Wrong input, Unrecognized mobile device')
    return mob_driver


def get_chrome():

    #chrome_driver = webdriver.Chrome(ChromeDriverManager().install())  #selenium 3.x
    srv = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=srv)
    return chrome_driver


def get_firefox():
    #ff_driver = webdriver.Firefox(GeckoDriverManager().install())  #selenium 3.x
    srv = Service(executable_path=GeckoDriverManager().install())
    ff_driver = selenium.webdriver.Firefox(service=srv)
    return ff_driver


def get_edge():
    #edge_driver = webdriver.Edge(EdgeChromiumDriverManager().install())  #selenium 3.x
    srv = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Edge(service=srv)
    return edge_driver


def get_android(udid):
    dc = {}
    # dc['reportDirectory'] = get_data('Report_Directory')
    # dc['reportFormat'] = get_data('Report_Format')
    #dc['testName'] = get_data('Test_Name')
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('Appium_server'), dc)
    return android_driver


def get_ios(udid):
    dc = {}
    dc['reportDirectory'] = get_data('Report_Directory')
    dc['reportFormat'] = get_data('Report_Format')
    dc['testName'] = get_data('Test_Name')
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('Appium_server'), dc)
    return ios_driver


def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('Electron_app')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('Electron_driver')) #need selenium version 3.x
    return driver


def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('Desktop_App')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowPC'
    desktop_driver = appium.webdriver.Remote("http://127.0.0.1:4723", dc)
    return desktop_driver


# catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if None it's API test
            image = get_data('ScreenshotPath') + 'screen_' + str(get_time_stamp()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
