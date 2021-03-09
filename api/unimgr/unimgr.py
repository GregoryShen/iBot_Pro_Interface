from core.restclient import RestClient


class Unimgr(RestClient):
    def get_unimgr(self, **kwargs):
        return self.get("/managerEN/unimgr/", **kwargs)

    def get_sys_notfication(self, **kwargs):
        return self.get("/ibotpro/unimgr/sys-notification!list.action", **kwargs)
