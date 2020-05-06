import time


def test_is_opencart_works(get_driver):
    browser = get_driver
    time.sleep(5)
    assert browser.find_elements_by_xpath('//h1/a[text()="Your Store"]')
