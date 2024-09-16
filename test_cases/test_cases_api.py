import allure

from extensions.api_actions import APIActions
from extensions.verifications import Verifications
from workflows.api_flows import APIFlows




class TestApi:

    @allure.title('Test01: Create team')
    @allure.description('Create team in table')
    def test_create_team(self):
        APIFlows.add_team('dan', 'danino@gmail.com')

    @allure.title('Test02: Extract data from Json')
    @allure.description('Extract data from users')
    def test_extract_data(self):
        APIFlows.find_user_detail([1,'name'], 'dan')

    @allure.title('Test03: Update user')
    @allure.description('Update user using name and extract the relevant id')
    def test_update_by_user(self):
        APIFlows.update_user('danino', 'blublu@yhoo.co.il', 'blublu' , 'balulu')

    @allure.title('Test04: delete team')
    @allure.description('Delete team using name and extract the relevant id')
    def test_delete_team_using_name(self):
        APIFlows.delete_team('dan')
