from assignment.src.Utilities.genericUtilities import *
from assignment.src.Utilities.requestUtility import RequestsUtility
import json
import jsonpickle


class UserHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()
        usrname = ''
        pet_name = ''
        tag_name = ''
        pet_category = ''

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
        import pdb;
        pdb.set_trace()
        print(username)
        return get_all_users_json


    def create_multiple_pets(self):

        pet_n = generate_first_names()
        tag_n = generate_last_names()
        pets = ['Dog', 'Cat', 'Rodent']

        arr = round(random.randint(0, (len(pets)) - 1), 1)
        pet_c = str(pets[arr])

        global pet_name
        global pet_category
        global tag_name

        pet_name = pet_n
        tag_name = tag_n
        pet_category = pet_c

        payload = {
                  "id": 0,
                  "category": {
                    "id": 0,
                    "name": pet_category
                  },
                  "name": pet_name,
                  "photoUrls": [
                    "linktophoto.down.up"
                  ],
                  "tags": [
                    {
                      "id": 0,
                      "name": tag_name
                    }
                  ],
                  "status": "available"
                }
        import pdb;
        #pdb.set_trace()
        create_pet = self.request_utility.postt(endpoint='pet', payload=payload, expected_status_code=200)
        print(pet_name)
        return create_pet

    def update_pet_details(self):
        statuses = ['Available', 'Pending', 'Sold']
        arr = round(random.randint(0, (len(statuses)) - 1), 1)
        status = str(statuses[arr])

        payload = {
                  "id": 0,
                  "category": {
                    "id": 0,
                    "name": pet_category
                  },
                  "name": pet_name,
                  "photoUrls": [
                    "linktophoto.up.down;"
                  ],
                  "tags": [
                    {
                      "id": 0,
                      "name": tag_name
                    }
                  ],
                  "status": status
                }

        update_pet = self.request_utility.putt(endpoint='pet', payload=payload, expected_status_code=200)
        #import pdb; pdb.set_trace()
        print(pet_name)
        return update_pet

    def get_pet_status_verify(self, status_option):

        path = "pet/findByStatus?status" + "=" + status_option
        get_all_users_json = self.request_utility.get(path)
        import pdb;
        #pdb.set_trace()
        print(pet_name)
        return get_all_users_json

