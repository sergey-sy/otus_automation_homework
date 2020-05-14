# get_driver scope='module'

def test_header_logo(get_driver):
    assert get_driver.find_elements_by_xpath('//a[text()="Your Store"]')


def test_main_slider(get_driver):
    assert get_driver.find_element_by_css_selector('.swiper-viewport #slideshow0')


def test_navbar(get_driver):
    assert get_driver.find_elements_by_css_selector('div.navbar-ex1-collapse')


def test_cart_in_top_nav(get_driver):
    assert get_driver.find_elements_by_css_selector('a[title="Shopping Cart"]')


def test_cart_button_header(get_driver):
    assert get_driver.find_elements_by_css_selector('header button.dropdown-toggle')
