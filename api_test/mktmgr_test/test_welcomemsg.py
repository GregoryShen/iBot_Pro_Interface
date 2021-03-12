import pytest
import json as json_parser
from libraries.get_data import get_data_path
from libraries.get_data import get_test_data

case, param = get_test_data('test_list_welcome_msg', get_data_path(__file__))


@pytest.mark.parametrize("case, payload, expected", param, ids=case)
def test_list_welcome_msg(env, case, payload, expected):
    r = env.ibotpro.mktmgr.welcome_msg.list_welcome_msg(json=payload)
    assert r.status_code == expected['status_code']
    assert r.content['success'] == expected['success']
    assert len(r.content['data']) == r.content['total']

# def test_save_welcome_msg(env):
#     data = {
#         "type": "1",
#         "title": "中文不编码测试",
#         "welcome": "中文不编码测试",
#         "platform": "web",
#         "semantic": "M1D7"
#     }
#     payload = {"data": json_parser.dumps(data)}
#     r = env.ibotpro.mktmgr.welcome_msg.save_welcome_msg(data=payload)
#     assert r.status_code == 200, "status code should be 200, but actually " \
#                                  "got {}".format(r.status_code)
#     assert r.content['message'] == 'fail'

def test_delete_welcome_msg(env):
    pass

def test_apply_welcome_msg(env):
    pass


if __name__ == '__main__':
    pytest.main(['--verbose', '-s'])
