from ibot_pro import IbotPro


class Env:
    def __init__(self, api_root_url, payload):
        self.ibotpro = IbotPro(api_root_url, payload)
