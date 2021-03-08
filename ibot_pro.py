from api.authmgr.authmgr import Authmgr
from api.unimgr.unimgr import Unimgr


class IbotPro:
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.authmgr = Authmgr(self.api_root_url, **kwargs)
        self.unimgr = Unimgr(self.api_root_url, **kwargs)


if __name__ == '__main__':
    ibotpro = IbotPro('http://hftest.demo.xiaoi.net')
    ibotpro.authmgr.session.headers['X-Requested-With'] = 'XMLHttpRequest'
    payload = {
        'username': 'admin',
        'password': '6a6b62c50f7d74bb7e1ce50959ff0b5c12bb7379',
        'localLanguage': 'en_US',
    }
    r = ibotpro.authmgr.login(data=payload)
    assert r.status_code == 200
    assert r.content["message"] == "Login Succeed"
    print(r.content)
    print(r.raw.headers)
    jsessionid = r.raw.headers['Set-Cookie'].split(' ')
    ck = []
    for item in jsessionid:
        if "manager" in item:
            ck.append(item)
    ck_n = ' '.join(ck)
    ibotpro = IbotPro("http://hftest.demo.xiaoi.net", Cookie=ck_n)
    payload = {
        "_dc": '1615216654523'
    }
    r = ibotpro.unimgr.get_sys_notfication(data=payload)
    assert r.status_code == 200
    assert r.content['success'] is True
