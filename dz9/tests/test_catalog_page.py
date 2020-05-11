# get_driver scope='module'
PAGE_ADRESS = 'http://localhost/index.php?route=product/category&path=20'


def test_good_card(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.product-grid:first-of-type')


def test_breadcrumb(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.breadcrumb')


def test_navbar(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.navbar-collapse')


def test_cart_button(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.btn-inverse')


def test_footer(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('footer')
