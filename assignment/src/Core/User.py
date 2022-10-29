from assignment.src.helpers.users_helper import UserHelper
from assignment.src.Utilities.genericUtilities import *
import random



class User(object):

    def __init__(self, **kwargs):
        self.id = None
        self.firstname = generate_first_names() if 'firstname' not in kwargs else kwargs['firstname']
        self.lasttname = generate_last_names() if 'lastname' not in kwargs else kwargs['lastname']
        self.username = self.firstname + '_' + self.lasttname
        email_password = generate_random_email_password()
        self.email = email_password['email']
        self.password = email_password['password']
        self.phone_number = generate_phone_number() if 'phone_number' not in kwargs else kwargs['phone_number']
        self.userStatus = random.randint(1, 10000)

