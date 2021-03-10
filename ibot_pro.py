from api.authmgr.authmgr import Authmgr
from api.unimgr.unimgr import Unimgr
from api.mktmgr.mktmgr import Mktmgr
from core.restclient import RestClient
import json as json_parser

class IbotPro:
    def __init__(self, api_root_url, payload):
        self.api_root_url = api_root_url
        restclient = RestClient(self.api_root_url)
        restclient.session.headers.update({'X-Requested-With':'XMLHttpRequest',
                                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        restclient.login(data=payload)
        restclient.session.headers['X-Requested-With'] = None
        session = restclient.session
        self.authmgr = Authmgr(self.api_root_url, session=session)
        self.unimgr = Unimgr(self.api_root_url, session=session)
        self.mktmgr = Mktmgr(self.api_root_url, session=session)


if __name__ == '__main__':
    payload = {
        'username': 'tests',
        'password': '04d13fd0aa6f0197cf2c999019a607c36c81eb9f',
        'localLanguage': 'zh_CN',
    }
    ibotpro = IbotPro("http://172.16.8.117:8888", payload)
    payload_1 = {
        'page': 1,
        'start': 0,
        'limit': 10
    }

    r = ibotpro.mktmgr.welcome_msg.list_welcome_msg(json=payload)
    assert r.status_code == 200