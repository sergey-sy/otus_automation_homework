import pytest


def pytest_addoption(parser):
    """Get parameters from command line during start testfile"""
    parser.addoption("--url", action="store", default="https://ya.ru", help="This is request url")
    parser.addoption("--status_code", action="store", default="200", help="This is http status code")


@pytest.fixture
def url_param(request):
    """Return dictionary with params"""
    parsed_params = {}
    parsed_params['--url'] = request.config.getoption('--url')
    parsed_params['--status_code'] = request.config.getoption('--status_code')
    return parsed_params
