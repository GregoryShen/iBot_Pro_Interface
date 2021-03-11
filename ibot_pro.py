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
        'username': 'admin',
        'password': 'd033e22ae348aeb5660fc2140aec35850c4da997',
        'localLanguage': 'zh_CN',
    }
    ibotpro = IbotPro("http://172.16.9.254:84/pro", payload)
    dt = {
        "type": "1",
        "title": "test",
        "welcome": "test",
        "platform": "web",
        "semantic": "M1D2"
    }
    dt = json_parser.dumps(dt)
    payload = {"data": dt}
    r = ibotpro.mktmgr.welcome_msg.save_welcome_msg(data=payload)
    print(r.content)
