import allure
import test_cases.conftest as conf

class DBActions:

    @staticmethod
    @allure.step('Query builder')
    def query_builder(columns, table, where_name, where_value):
        cols = ','.join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + where_name + "='" + where_value + "'"
        return query

    @staticmethod
    @allure.step('Get Query result')
    def get_query_result(columns, table, where_name, where_value):
        query = DBActions.query_builder(columns, table, where_name, where_value)
        db_cursor = conf.db_connect.cursor()
        db_cursor.execute(query)
        query_result = db_cursor.fetchall()
        return query_result  # Returns list of Tuples