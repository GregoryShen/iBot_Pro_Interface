from core.restclient import RestClient


class Authmgr(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Authmgr, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post('/ibotpro/authmgr/auth!login.action', **kwargs)
