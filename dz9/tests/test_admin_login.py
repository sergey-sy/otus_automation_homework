# get_driver scope='module'
PAGE_ADRESS = 'http://localhost/admin'


def test_login_panel(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.panel-default')


def test_input_username(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('[name="username"]')


def test_input_password(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('#input-password')


def test_submit_button(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('button[type="submit"]')


def test_help_block(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.help-block')
