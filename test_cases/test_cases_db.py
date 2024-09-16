import allure
import pytest

import utilities.manage_pages
from extensions.verifications import Verifications
from workflows.db_flows import DBFlows


@pytest.mark.usefixtures('init_driver')
@pytest.mark.usefixtures('init_database_connection')
class TestCasesDB:

    @allure.title("Test01: Log in to grafana using DB")
    @allure.description('Log in to grafana using DB')
    def test_login_grafana(self):
        DBFlows.log_in_grafana_db()
        Verifications.verify_equals(utilities.manage_pages.grafana_main_page.get_title().text, 'Welcome to Grafana')

