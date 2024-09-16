import time

import allure
import pytest

from utilities.common_ops import get_data
from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_electron_driver')
class TestCasesElectron:

    @allure.title('Test01: Create task')
    @allure.description('Create task and verify that created successfully')
    def test_create_task(self):
        ElectronFlows.create_task('My 1 task test', 'important')
        ElectronFlows.create_task('My 2 task test','important')
        ElectronFlows.create_task('My 3 task test','important')
        ElectronFlows.create_task('My 4 task test','important')
        ElectronFlows.complete_last_task()
        time.sleep(2)



    @allure.title('Test02: Create task with color')
    @allure.description('Create task and verify that created successfully with color')
    def test_create_task_color(self):
        ElectronFlows.create_task('My 5 task test - important', 'important')
        ElectronFlows.create_task('My 6 task test', 'important')
        ElectronFlows.complete_last_task()
        time.sleep(2)

    @allure.title('Test03: Delete task')
    @allure.description('delete task per index')
    @pytest.mark.skipif(True, reason="List always be empty because using delete all in teardown method")
    def test_delete_task(self):
        ElectronFlows.delete_task(int(get_data('Index_to_delete')))
        time.sleep(2)


    def teardown_method(self):
        ElectronFlows.delete_all_task()
        time.sleep(2)

    # @allure.title('Test03: Swipe to previous date')
    # @allure.description('Swipe to previous date')
    # def test_swipe_prev_date(self):
    #     ElectronFlows.check_previous_page()

    # @allure.title('Test04: Drag task')
    # @allure.description('Drag first task to be last task')
    # def test_drag_task(self):
    #     ElectronFlows.drag_task()
    #     time.sleep(3)