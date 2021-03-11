import pytest
import os
from libraries.environment import Env
from configparser import ConfigParser


@pytest.fixture(scope="module", autouse=True)
def env():
    config = ConfigParser()
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),
                             'config', 'config.ini')
    config.read(file_path)
    api_root_url = config[os.environ['env']]['api_root_url']
    username = config[os.environ['env']]['username']
    password = config[os.environ['env']]['password']
    localLanguage = config[os.environ['env']]['localLanguage']
    payload = {
        'username': username,
        'password': password,
        'localLanguage': localLanguage,
    }
    yield Env(api_root_url, payload)
