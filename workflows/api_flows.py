import json

import allure

from extensions.api_actions import APIActions
from extensions.verifications import Verifications
from utilities.common_ops import get_data

url = get_data('UrlHost')
resource_team = get_data('TeamsRes')
resource_user = get_data('UsersRes')
user_name = get_data('UserNameGrafana')
password = get_data('PasswordGrafana')



class APIFlows:

    @staticmethod
    @allure.step("add team - user can't using api")
    def add_team(new_name, email):
        payload = {'name': new_name, 'email': email}
        response_status = APIActions.add(url+resource_team, payload,  user_name, password)
        return response_status

    @staticmethod
    @allure.step("find a user detail")
    def find_user_detail(node):
        param = None
        response = APIActions.get(url+resource_user, param, user_name, password)
        extract_val = APIActions.extract_data(response, node)
        return extract_val

    @staticmethod
    @allure.step("update user by user login name")
    def update_user(login_name, new_email, new_name,  new_login):
        payload = {'email': new_email, 'name': new_name, "login": new_login}
        search_name = dict(loginOrEmail=login_name)
        response = APIActions.get(url+resource_user+'lookup', search_name, user_name, password)
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        get_id = APIActions.extract_data(response, ['id'])
        print(get_id)
        response_status = APIActions.update(url + resource_user + str(get_id), payload, user_name, password)
        return response_status

    @staticmethod
    @allure.step("delete team")
    def delete_team(name_to_delete):
        param = {'name': name_to_delete}
        response = APIActions.get(url + resource_team + 'search', param, user_name, password)
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        get_id = APIActions.extract_data(response, ['teams', 0, 'id'])
        print(get_id)
        response_status = APIActions.delete(url + resource_team + str(get_id), user_name, password)
        return response_status
