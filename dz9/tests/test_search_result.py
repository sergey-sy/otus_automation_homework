# get_driver scope='module'
PAGE_ADRESS = 'http://localhost/index.php?route=product/search'


def test_search_h1(get_driver):
    get_driver.get(PAGE_ADRESS)
    print(get_driver.current_url)
    assert get_driver.find_element_by_xpath('//h1 [text()="Search"]')


def test_input_search(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_element_by_css_selector('#input-search')


def test_select_category_id(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_element_by_css_selector('select[name="category_id"]')


def test_subcategories_checkbox(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_element_by_css_selector('.col-sm-3 .checkbox-inline')


def test_product_description_checkbox(get_driver):
    get_driver.get(PAGE_ADRESS)
    assert get_driver.find_element_by_css_selector('p .checkbox-inline')
