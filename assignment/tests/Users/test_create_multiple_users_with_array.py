import pytest
import logging as logger
from assignment.src.Utilities.genericUtilities import *
from assignment.src.helpers.users_helper import UserHelper
from assignment.src.Core.User import User




@pytest.mark.tcid01
@pytest.mark.parametrize("no_of_users",
                         [
                            (1),
                            (2)
                         ])
def test_create_multiple_users_with_array(no_of_users):
    logger.info("TEST: Create multiple users with array.")
    user_objects = []
    user_helper = UserHelper()

    for i in range(0, no_of_users):
        user_class = User()
        user_class.id = random.randint(1,10000)
        user_objects.append(user_class)

    users_response = user_helper.create_users_with_array(user_objects)
    assert users_response.status_code == 200, f"response code is not expected"
    users = users_response.json()
    assert users["message"] == "ok"


@pytest.mark.parametrize("no_of_users",
                         [
                            (1),
                            #(2)
                         ])
@pytest.mark.tcid02
def test_update_user_with_username(no_of_users):
    logger.info("TEST: Update a user's username and other details.")
    user_objects = []
    user_helper = UserHelper()

    for i in range(0, no_of_users):
        user_class = User()
        user_class.id = random.randint(1,10000)
        user_objects.append(user_class)

    users_response = user_helper.create_users_with_array(user_objects)
    assert users_response.status_code == 200, f"response code is not expected"
    users = users_response.json()
    assert users["message"] == "ok"

    for user in user_objects:
        updated_username = user.lasttname + '_' + user.firstname
        user_update_info = user_helper.update_username_and_details(user, updated_username)
        assert user_update_info.status_code == 200, f"response code is not expected"
        user_response = user_update_info.json()
        user.username = updated_username


@pytest.mark.parametrize("no_of_users",
                         [
                            (1),
                            #(2)
                         ])
@pytest.mark.tcid03
def test_get_user_info_with_username(no_of_users):
    logger.info("TEST: GET Updated user's username and other details.")
    user_objects = []
    user_helper = UserHelper()

    for i in range(0, no_of_users):
        user_class = User()
        user_class.id = random.randint(1, 10000)
        user_objects.append(user_class)

    users_response = user_helper.create_users_with_array(user_objects)
    assert users_response.status_code == 200, f"response code is not expected"
    users = users_response.json()
    assert users["message"] == "ok"

    #Updated
    for user in user_objects:
        updated_username = user.lasttname + '_' + user.firstname
        user_update_info = user_helper.update_username_and_details(user, updated_username)
        assert user_update_info.status_code == 200, f"response code is not expected"
        user_response = user_update_info.json()
        user.username = updated_username
        #GET
        user_get_info = user_helper.get_user_detais(user.username)
        assert user_get_info.status_code == 200
        user_info = user_get_info.json()
        import pdb;pdb.set_trace()
        # assert user_info['firstname'] == user.firstname
        assert user_info['username'] == user.username






