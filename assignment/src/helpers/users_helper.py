from assignment.src.Utilities.genericUtilities import *
from assignment.src.Utilities.requestUtility import RequestsUtility
import json
import jsonpickle


class UserHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_users_with_array(self, lst_users):
        lst_user = jsonpickle.encode(lst_users, unpicklable=False)
        print(lst_user)
        create_user_json = self.request_utility.post('user/createWithArray', payload=lst_user, expected_status_code=200)
        return create_user_json

    def update_username_and_details(self, user, updated_username):

        path = 'user' + '/' + user.username
        user.username = updated_username
        lst_user = jsonpickle.encode(user, unpicklable=False)
        create_user_json = self.request_utility.put(endpoint=path, payload=lst_user, expected_status_code=200)
        print(user.username)
        return create_user_json

    def get_user_detais(self, username):

        path =  'user' + '/' + username
        get_all_users_json = self.request_utility.get(path)
        print(username)
        return get_all_users_json

    def create_pets(self, pet):
        pet_json = jsonpickle.encode(pet, unpicklable=False)
        create_user_json = self.request_utility.post('pet', payload=pet_json, expected_status_code=200)
        return create_user_json

    def update_pet_status_and_details(self, pet, status):
        pet.status = status
        pet_json = jsonpickle.encode(pet, unpicklable=False)
        create_user_json = self.request_utility.put(endpoint='pet', payload=pet_json, expected_status_code=200)
        return create_user_json

    def get_pet_status_verify(self, status_option):
        path = "pet/findByStatus?status" + "=" + status_option
        get_all_users_json = self.request_utility.get(path)
        return get_all_users_json
