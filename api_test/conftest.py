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
    # api_root_url = os.environ[config['env']]['api_root_url']
    # username = os.environ[config['env']]['username']
    # password = os.environ[config['env']]['password']
    # localLanguage = os.environ[config['env']]['localLanguage']
    print(config)
    api_root_url = config['dev_env']['api_root_url']
    username = config['dev_env']['username']
    password = config['dev_env']['password']
    localLanguage = config['dev_env']['localLanguage']
    payload = {
        'username': username,
        'password': password,
        'localLanguage': localLanguage,
    }
    # r = ibotpro.authmgr.login(data=payload)
    # jsessionid = r.raw.headers['Set-Cookie'].split(' ')
    # ck = []
    # for item in jsessionid:
    #     if "JSESSIONID" in item:
    #         if ';' in item:
    #             dex = item.index(';')
    #         ck.append(item[:dex])
    # ck_n = ';'.join(ck)
    yield Env(api_root_url, payload)