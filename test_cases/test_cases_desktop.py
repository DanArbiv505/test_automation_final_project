import time

import allure
import pytest

from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures('init_desktop_driver')
class TestCasesDesktop:

    @allure.title('Test01: Create calculation')
    @allure.description('make calculation with a given string')
    def test_create_task(self):
        DesktopFlows.get_calculate('7+1+2', '10')
        DesktopFlows.get_calculate('5*2+20/6', '5')
        time.sleep(3)