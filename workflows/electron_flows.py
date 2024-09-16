import time

import allure
import pytest
from selenium.webdriver.common.keys import Keys

import utilities.common_ops
import utilities.manage_pages as page

from extensions.ui_actions import UiActions
from extensions.verifications import Verifications


class ElectronFlows:

    @staticmethod
    @allure.step('insert task')
    def create_task(task_description, important):
          if important in task_description:
              ElectronFlows.add_color()
          UiActions.change_text(page.electron_page.get_create_task(), task_description)
          UiActions.press_enter()
          if important in task_description:
              ElectronFlows.back_to_no_color()
          ElectronFlows.verify_task_in_list(task_description)


    @staticmethod
    @allure.step('verify task in list of tasks')
    def verify_task_in_list(given_task):
        list_of_task = page.electron_page.get_title_of_task_list()
        list_text = []
        for task in list_of_task:
            list_text.append(task.text)
        Verifications.is_in(given_task, list_text)

    @staticmethod
    @allure.step('delete task by index')
    def delete_task(index):
        try:
            wanted_deleted_task_elem = page.electron_page.get_delete_buttons()[index]
        except:
            pytest.fail('List is empty')

        UiActions.move_to_electron(wanted_deleted_task_elem)

    @staticmethod
    @allure.step('delete all tasks')
    def delete_all_task():
        size_of_list = ElectronFlows.get_size_of_task_list()
        for i in range(size_of_list):
            UiActions.click(page.electron_page.get_delete_buttons()[0])


    @staticmethod
    @allure.step('get size of list')
    def get_size_of_task_list():
        return len(page.electron_page.get_task_list())

    @staticmethod
    @allure.step('add color to task')
    def add_color():
        UiActions.click(page.electron_page.get_color_dropdown())
        UiActions.click(page.electron_page.get_red_color())

    @staticmethod
    @allure.step('back to no color')
    def back_to_no_color():
        UiActions.click(page.electron_page.get_no_color())
        UiActions.click(page.electron_page.get_color_dropdown())

    @staticmethod
    @allure.step('click the last task as complete')
    def complete_last_task():
        complete_button_elem_list = page.electron_page.get_complete_task_button()
        UiActions.click(complete_button_elem_list[len(complete_button_elem_list)-1])

    # @staticmethod
    # @allure.step('go to previous page and verify disable create task')
    # def check_previous_page():
    #     if page.electron_page.get_no_task().is_displayed():
    #         UiActions.long_click_and_drag(utilities.common_ops.Direction.RIGHT, page.electron_page.get_no_task())
    #     else:
    #         UiActions.long_click_and_drag(utilities.common_ops.Direction.RIGHT, page.electron_page.get_title_of_task_list()[0])
    #     time.sleep(5)
    #     Verifications.is_not_displayed(page.electron_page.get_create_task())


    # @staticmethod
    # @allure.step('drag the first task to be last')
    # def drag_task():
    #     drag_elements = page.electron_page.get_drag_buttons()
    #     first_task = drag_elements[0]
    #     last_task = drag_elements[len(drag_elements)-1]
    #     UiActions.drag_and_drop(first_task, last_task)
    #     complete_button_elem_list = page.electron_page.get_complete_task_button()
    #     UiActions.click(complete_button_elem_list[len(complete_button_elem_list)-1])





