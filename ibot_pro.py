from api.authmgr.authmgr import Authmgr
from api.unimgr.unimgr import Unimgr
from api.mktmgr.welcomemsg import WelcomeMsg


class IbotPro:
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.authmgr = Authmgr(self.api_root_url, **kwargs)
        self.unimgr = Unimgr(self.api_root_url, **kwargs)
        self.mktmgr =


if __name__ == '__main__':
    ibotpro = IbotPro('http://172.16.8.117:8888')
    ibotpro.authmgr.session.headers['X-Requested-With'] = 'XMLHttpRequest'
    payload = {
        'username': 'tests',
        'password': '04d13fd0aa6f0197cf2c999019a607c36c81eb9f',
        'localLanguage': 'zh_CN',
    }
    r = ibotpro.authmgr.login(data=payload)
    assert r.status_code == 200
    assert r.content["message"] == "Login Succeed"
    print(r.content)
    print(r.raw.headers)
    jsessionid = r.raw.headers['Set-Cookie'].split(' ')
    ck = []
    for item in jsessionid:
        if "JSESSIONID" in item:
            if ';' in item:
                dex = item.index(';')
            ck.append(item[:dex])
    ck_n = ';'.join(ck)
    print(ck_n)
    ibotpro = IbotPro("http://172.16.8.117:8888", Cookie=ck_n)
    payload = {
        "_dc": '1615271320523s'
    }
    r = ibotpro.unimgr.get_sys_notfication(data=payload)
    assert r.status_code == 200
    assert r.content['success'] is True
