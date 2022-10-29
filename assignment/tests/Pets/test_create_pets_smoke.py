import pytest
import logging as logger
from assignment.src.Utilities.genericUtilities import *
from assignment.src.helpers.users_helper import UserHelper


@pytest.mark.tcid04
def test_create_multiple_pets():
    pet_object = UserHelper()
    pets_info = pet_object.create_multiple_pets()
    import pdb; pdb.set_trace()


@pytest.mark.tcid05
def test_update_pet_status_details():
    pet_object = UserHelper()
    pets_info = pet_object.create_multiple_pets()
    pets_update = pet_object.update_pet_details()
    import pdb;
    pdb.set_trace()


@pytest.mark.tcid06
def test_pet_by_status_verify():
    pet_object = UserHelper()
    pets_info = pet_object.create_multiple_pets()
    pets_update = pet_object.update_pet_details()
    pets_status = pet_object.get_pet_status_verify('sold')
    #assert pets_update['status'] ==