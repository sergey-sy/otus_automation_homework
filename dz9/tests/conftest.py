from os import *
import time


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FX_Options
from selenium.webdriver.chrome.options import Options as CH_Options


def pytest_addoption(parser):
    """
    Method adds custom keys for run pytest
    --browser: chrome/firefox/ie - browser for testing
    :param parser: keys parser pytest
    """
    parser.addoption('--browser', action='store', default='chrome', help='This key to choose required browser')
    parser.addoption('--url', action='store', default='http://localhost:80/', help='This is request url')


@pytest.fixture(scope='module')
def get_driver(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    results_dir = path.join(getcwd(), 'tests/results')

    if not path.exists(results_dir):
        makedirs(results_dir)

    log_path = path.join(results_dir, 'driver.log')
    drivers_dir = path.join(getcwd(), 'tests/drivers')

    driver = None
    driver_name = dict(
        firefox='geckodriver',
        chrome='chromedriver'
    )[browser]
    driver_path = path.join(drivers_dir, driver_name)

    if browser == 'firefox':
        options = FX_Options()
        options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(executable_path=driver_path,
                                   service_log_path=log_path,
                                   options=options,
                                   firefox_profile=profile)
    elif browser == 'chrome':
        options = CH_Options()
        options.add_argument('headless')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(executable_path=driver_path,
                                  service_log_path=log_path,
                                  options=options)
    elif browser == 'ie':
        capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
        capabilities['acceptSslCerts'] = True
        driver = webdriver.Ie(executable_path=driver_path,
                              service_log_path=log_path,
                              capabilities=capabilities)

    driver.maximize_window()
    driver.get(url)
    driver.delete_all_cookies()

    def driver_finalizer():
        driver.quit()

    request.addfinalizer(driver_finalizer)
    return driver
