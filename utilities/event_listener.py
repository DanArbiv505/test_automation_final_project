import pytest
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print("Before Navigate to", url)

    def after_navigate_to(self, url, driver):
        print("After Navigate to", url)

    def before_navigate_back(self, driver):
        print("Before Navigate back", driver.current_url)

    def after_navigate_back(self, driver):
        print("After Navigate back", driver.current_url)

    def before_navigate_forward(self, driver):
        print("Before Navigate forward", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After Navigate forward", driver.current_url)

    def before_find(self, by, value, driver):
        print("Before find", value)

    def after_find(self, by, value, driver):
        print("After find", value)

    def before_click(self, element, driver):
        EventListener.button_text = element.get_attribute("value")
        print("Before click", EventListener.button_text)

    def after_click(self, element, driver):
        print("After click", EventListener.button_text)

    def before_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("Before change value of" + element.get_attribute("value"))
        else:
            print("Before change value of" + element.text)

    def after_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("After change value of" + element.get_attribute("value"))
        else:
            print("After change value of" + element.text)

    def before_execute_script(self, script, driver):
        print("Before execute script", script)

    def after_execute_script(self, script, driver):
        print("After execute script", script)

    def before_close(self, driver):
        print("Before close session")

    def after_close(self, driver):
        print("After close session")

    def before_quit(self, driver):
        print("Before quit")

    def after_quit(self, driver):
        print("After quit")

    def on_exception(self, exception, driver):
        print("On Exception:" + str(exception))
        # pytest.fail()