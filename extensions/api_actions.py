import json

import allure
import requests
from requests.auth import HTTPBasicAuth

header = {'Content-Type': 'application/json'}


class APIActions:

    @staticmethod
    @allure.step('get users or teams')
    def get(path, param, user_name, password):
       if param == None:
             response = requests.get(path, auth=HTTPBasicAuth(user_name, password))
       else:
             response = requests.get(path, param, auth=HTTPBasicAuth(user_name, password))
       return response


    @staticmethod
    @allure.step('extract data from user or team')
    def extract_data(response, nodes):
        extract_value = None
        response_json = response.json()
        if len(nodes) == 1:
            extract_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extract_value = response_json[nodes[0]][nodes[1]]
        elif len(nodes) == 3:
            extract_value = response_json[nodes[0]][nodes[1]][nodes[2]]
        return extract_value

    @staticmethod
    @allure.step('update user or team')
    def update(path, payload, user_name, password):
        response = requests.put(path, json=payload, headers=header, auth=HTTPBasicAuth(user_name, password))
        return response.status_code

    @staticmethod
    @allure.step("add team - user can't using api")
    def add(path, payload, user_name, password):
        response = requests.post(path, json=payload, headers=header, auth=HTTPBasicAuth(user_name, password))
        return response.status_code

    @staticmethod
    @allure.step("delete team - user can't using api")
    def delete(path, user_name, password):
        response = requests.delete(path, auth=HTTPBasicAuth(user_name, password))
        return response.status_code


