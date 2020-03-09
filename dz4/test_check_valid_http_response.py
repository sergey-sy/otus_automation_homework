import requests


def test_answer(url_param):
    """Compare status code from request with status code from input"""
    response = requests.get(url_param['--url'])
    if str(response.status_code) == url_param['--status_code']:
        assert True
    else:
        print(
            f"""\n!response.status_code does not satisfy --status_code from input
            *** {response.status_code} != {url_param['--status_code']} ***"""
        )
        assert False
