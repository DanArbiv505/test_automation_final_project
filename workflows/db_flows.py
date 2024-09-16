import allure

from extensions.db_actions import DBActions
from extensions.ui_actions import UiActions
import utilities.manage_pages as page


class DBFlows:

    @staticmethod
    @allure.step('Get in grafana from DB')
    def log_in_grafana_db():
        columns = ['name', 'password']
        results = DBActions.get_query_result(columns, 'Employee', 'comments', 'correct')
        UiActions.change_text(page.grafana_db_page.get_email(), results[0][0])
        UiActions.change_text(page.grafana_db_page.get_password(), results[0][1])
        UiActions.click(page.grafana_db_page.get_login_button())
        UiActions.click(page.grafana_db_page.get_skip())
