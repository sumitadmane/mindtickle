import pytest
import logging as logger
from assignment.src.Utilities.genericUtilities import *
from assignment.src.helpers.users_helper import UserHelper
from assignment.src.Core.Pets import Pets




@pytest.mark.tcid01
@pytest.mark.parametrize("no_of_pets",
                         [
                            (1),
                            (2)
                         ])
def test_create_pets(no_of_pets):
    logger.info("TEST: Create multiple pets.")
    user_helper = UserHelper()

    for i in range(0, no_of_pets):
        pet_class = Pets()
        pet_class.id = random.randint(1, 10000)
        users_response = user_helper.create_pets(pet_class)
        assert users_response.status_code == 200, f"response code is not expected"
        users = users_response.json()


@pytest.mark.parametrize("status",
                         [
                            ('Pending'),
                            ('Sold')
                         ])

def test_update_pets(status):
    logger.info("TEST: Update created pet.")
    user_helper = UserHelper()

    pet_class = Pets()
    pet_class.id = random.randint(1, 10000)
    pet_response = user_helper.create_pets(pet_class)
    assert pet_response.status_code == 200, f"response code is not expected"
    pets = pet_response.json()
    assert pets['status'] == 'available', f"pet status is not available when created"
    print(pets['name'])

    update_pet_status = user_helper.update_pet_status_and_details(pet_class, status)
    assert update_pet_status.status_code == 200, f"status code is not expected"
    update_pet_info = update_pet_status.json()
    assert update_pet_info['name'] == pets['name'], f" Status got updated to wrong pet"


@pytest.mark.parametrize("status",
                         [
                            ('Pending'),
                            ('Sold')
                         ])
def test_get_pet_details_by_status(status):
    logger.info("TEST: Get pet details by updated status.")
    user_helper = UserHelper()

    pet_class = Pets()
    pet_class.id = random.randint(1, 10000)
    pet_response = user_helper.create_pets(pet_class)
    assert pet_response.status_code == 200, f"response code is not expected"
    pets = pet_response.json()
    assert pets['status'] == 'available', f"pet is not available when created"

    update_pet_status = user_helper.update_pet_status_and_details(pet_class, status)
    assert update_pet_status.status_code == 200, f"status code is not expected"
    update_pet_info = update_pet_status.json()
    assert update_pet_info['name'] == pets['name']

    get_pet_info = user_helper.get_pet_status_verify(status)
    assert get_pet_info.status_code == 200, f"response code is not expected"
    get_pet_by_status = get_pet_info.json()
    assert (get_pet_by_status[len(get_pet_by_status)-1]['name']) == update_pet_info['name']

