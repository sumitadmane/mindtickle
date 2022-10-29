import requests
import os
import json
from assignment.src.configs.hosts_config import swagger_api_hosts
import logging as logger


class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get("ENV", 'test')
        self.baseurl = swagger_api_hosts[self.env]

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status Code." \
                                                              f"Expected: {self.expected_status_code}, " \
                                                              f"and Actual status code {self.status_code}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json",
                        "accept": "application/json"}

        url = self.baseurl + endpoint
        rs_api = requests.post(url=url, data=payload, headers=headers)
        import pdb; pdb.set_trace()
        self.status_code = rs_api.status_code

        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code},but got ' \
                                                              f'this {self.status_code} '
        logger.debug(f"API response:{rs_api.json()}")
        return rs_api

    def get(self, endpoint, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json"}

        self.url = self.baseurl + endpoint
        rs_api = requests.get(url=self.url, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rsjson = rs_api.json()
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code},but got ' \
                                                              f'this {self.status_code}'

        logger.debug(f"API response:{rs_api.json()}")
        return rs_api


    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json",
                        "accept": "application/json"}

        self.url = self.baseurl + endpoint
        rs_api = requests.put(url=self.url, data=payload, headers=headers)
        import pdb;
        pdb.set_trace()
        self.status_code = rs_api.status_code

        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code},but got ' \
                                                              f'this {self.status_code} '
        logger.debug(f"API response:{rs_api.json()}")
        return rs_api

    def postt(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json",
                        "accept": "application/json"}

        url = self.baseurl + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers)

        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code},but got ' \
                                                              f'this {self.status_code} '
        logger.debug(f"API response:{rs_api.json()}")
        return rs_api.json()

    def putt(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json",
                        "accept": "application/json"}

        url = self.baseurl + endpoint
        rs_api = requests.put(url=url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code

        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code},but got ' \
                                                              f'this {self.status_code} '
        logger.debug(f"API response:{rs_api.json()}")
        return rs_api.json()