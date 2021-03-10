from core.restclient import RestClient
from api.mktmgr.welcomemsg import WelcomeMsg

class Mktmgr(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Mktmgr, self).__init__(api_root_url, **kwargs)
        self.welcome_msg = WelcomeMsg(api_root_url, **kwargs)