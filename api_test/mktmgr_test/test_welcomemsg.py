import pytest



def test_list_welcome_msg(env):
    payload = {
        'page': 1,
        'start': 0,
        'limit': 10
    }
    r = env.ibotpro.mktmgr.welcome_msg.list_welcome_msg(json=payload)
    assert r.status_code == 200
    assert r.content['success'] == True
    assert len(r.content['data']) == r.content['total']


if __name__ == '__main__':
    pytest.main()
