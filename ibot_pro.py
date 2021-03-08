from api.authmgr.authmgr import Authmgr


class IbotPro:
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.authmgr = Authmgr(self.api_root_url, **kwargs)


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
    print(r.content)
    print(r.raw.headers)
    # jsessionid = r.raw.headers['Set-Cookie']['JSESSIONID']
    # print(jsessionid)

