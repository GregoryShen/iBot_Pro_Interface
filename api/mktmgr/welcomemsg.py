from core.restclient import RestClient


class WelcomeMsg(RestClient):

    def list_welcome_msg(self, **kwargs):
        return self.get("/ibotpro/mktmgr/welcome-resource!list.action",
                        **kwargs)

    def save_welcome_msg(self, **kwargs):
        return self.post("/ibotpro/mktmgr/welcome-resource!save.action",
                         **kwargs)

    def delete_welcome_msg(self, **kwargs):
        return self.post("/ibotpro/mktmgr/welcome-resource!delete.action",
                         **kwargs)

    def apply_welcome_msg(self, **kwargs):
        return self.get("/ibotpro/mktmgr/welcome-resource!apply.action",
                        **kwargs)

    def export_welcome_msg(self, **kwargs):
        return self.get("/ibotpro/mktmgr/welcome-resource!export.action",
                        **kwargs)

    def import_welcome_msg(self, **kwargs):
        return self.post("/ibotpro/mktmgr/welcome-resource!_import.action",
                         **kwargs)

    def list_welcome_msg_dim(self, **kwargs):
        return self.get("/ibotpro/mktmgr/welcome-resource!listDimenstion\
                        .action", **kwargs)
