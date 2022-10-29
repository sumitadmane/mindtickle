import logging as logger
import random
import string
import names


def generate_random_email_password(domain=None, email_prefix=None, ):
    logger.debug("Generating random email and password.")

    if not domain:
        domain = "ggmail.com"

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_email = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_email + '@' + domain

    password_length = 10
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password are: {random_info}")

    return random_info


def generate_first_names():

    for i in range(1):
        first_name = names.get_first_name(gender='male')
        return first_name


def generate_last_names():

    for i in range(1):
        last_name = names.get_last_name()
        return last_name


def generate_phone_number():
    n = 8
    mobile_number = "+919" + str(random.randint(0, 9)) + ''.join(
            ["%s" % random.randint(0, 9) for num in range(0, n)])
    return mobile_number


