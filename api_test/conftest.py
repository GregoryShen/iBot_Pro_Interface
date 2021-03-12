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


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时,将收集到的item的name和nodeid的中文显示在控制台上,所有的测试
    用例收集完毕后调用,可以再次过滤或者对他们重新排序
    items (收集的测试项目列表)
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
