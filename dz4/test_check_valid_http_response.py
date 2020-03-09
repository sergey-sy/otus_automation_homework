import requests


def test_answer(url_param):
    response = requests.get(url_param['--url'])
    if str(response.status_code) == url_param['--status_code']:
        assert True
    else:
        print(
            f"""\n!response.status_code does not satisfy inputed --status_code
            *** {response.status_code} != {url_param['--status_code']} ***"""
        )
        assert False
