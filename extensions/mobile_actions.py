import allure
import test_cases.conftest as conf

from extensions.ui_actions import UiActions


class MobileActions(UiActions):

    @staticmethod
    @allure.step("Tap on element")
    def tap(elem, number_of_tap):
        conf.action.tap(elem, number_of_tap).perform()


    @staticmethod
    @allure.step("swipe")
    def swipe(x_start, y_start, x_end, y_end, duration):
        conf.driver.swipe(x_start, y_start, x_end, y_end, duration)


    @staticmethod
    @allure.step("zoom")
    def zoom(elem, pixels):
        x_loc = elem.rect['x']
        y_loc = elem.rect['y']
        m_action = conf.multi_action
        action1 = conf.action.long_press(x=x_loc,y=y_loc).move_to(x=x_loc, y=y_loc + pixels).wait(500).release()
        action2 = conf.action2.long_press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc - pixels).wait(500).release()
        m_action.add(action1, action2)
        m_action.perform()


    @staticmethod
    @allure.step("pinch")
    def pinch(elem, pixels):
        x_loc = elem.rect['x']
        y_loc = elem.rect['y']
        m_action = conf.multi_action
        action1 = conf.action.long_press(x=x_loc, y=y_loc + pixels).move_to(x=x_loc, y=y_loc).wait(500).release()
        action2 = conf.action2.long_press(x=x_loc, y=y_loc - pixels).move_to(x=x_loc, y=y_loc).wait(500).release()
        m_action.add(action1, action2)
        m_action.perform()

