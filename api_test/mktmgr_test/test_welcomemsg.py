import pytest

class TestWelcomeMsg:
    def test_list_welcome_msg(self, env):
        r = env.ibotpro.mktmgr