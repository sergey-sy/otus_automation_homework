# get_driver scope='module'
PAGE_ADRESS = 'http://localhost/index.php?route=product/product&path=20&product_id=42'


def test_good_name(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('#content h1')


def test_tab(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('[data-toggle=tab]')


def test_tab_content(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('.tab-content')


def test_product(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_css_selector('div #product')


def test_related_products_block(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_elements_by_xpath('//*[@id="content"]/div[2]')
