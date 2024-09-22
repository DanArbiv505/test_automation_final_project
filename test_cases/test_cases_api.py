import allure

from extensions.api_actions import APIActions
from extensions.verifications import Verifications
from workflows.api_flows import APIFlows




class TestApi:

    @allure.title('Test01: Add new team team')
    @allure.description('Add new team in grafana table using post method in rest api ')
    def test_create_team(self):
        response_status = APIFlows.add_team('dan', 'danino@gmail.com')
        Verifications.verify_equals(response_status, 200)

    @allure.title('Test02: Extract data from Json')
    @allure.description('Extract data from users table - get the name from first field')
    def test_extract_data(self):
        extract_val = APIFlows.find_user_detail([1,'name'])
        Verifications.verify_equals(extract_val, 'dan')

    @allure.title('Test03: Update user')
    @allure.description('Update user using name and extract the relevant id')
    def test_update_by_user(self):
        response_status = APIFlows.update_user('danino', 'blublu@yhoo.co.il', 'blublu' , 'balulu')
        Verifications.verify_equals(response_status, 200)

    @allure.title('Test04: delete team')
    @allure.description('Delete team using name and extract the relevant id')
    def test_delete_team_using_name(self):
        response_status = APIFlows.delete_team('dan')
        Verifications.verify_equals(response_status, 200)

    # Reset the user name back to default, grafana api don't allow to create new user
    def teardown_class(self):
        APIFlows.update_user('balulu', 'danino@gmail.co.il', 'dan', 'danino')

