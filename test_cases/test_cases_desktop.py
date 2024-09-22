import time

import allure
import pytest
from smart_assertions import verify_expectations

from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures('init_desktop_driver')
class TestCasesDesktop:

    @allure.title('Test01: Create calculation')
    @allure.description('make calculation with a given string')
    def test_create_task(self):
        result = DesktopFlows.get_calculate('7+1+2')
        Verifications.verify_equal_with_soft_assert(result, '10')
        result = DesktopFlows.get_calculate('5*2+20/6')
        Verifications.verify_equal_with_soft_assert(result, '5')
        verify_expectations()