import pytest
import requests
from random import randint, choice


@pytest.fixture(scope='module')
def get_list_all_breeds():
    return requests.get('https://dog.ceo/api/breeds/list/all').json()

def test_get_list_all_breeds(get_list_all_breeds):
    '''
    LIST ALL BREEDS from https://dog.ceo/dog-api/documentation/
    '''
    assert get_list_all_breeds['status'] == 'success'


def test_get_single_random_image():
    '''
    DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION
    from https://dog.ceo/dog-api/documentation/random
    '''
    responce = requests.get('https://dog.ceo/api/breeds/image/random').json()
    single_image_link = responce['message']
    assert requests.get(single_image_link).ok


@pytest.fixture(params=[1, 50])
def fixture_amount_links(request):
    return request.param

def test_get_multiple_imgages_from_breed_collection(fixture_amount_links):
    '''
    DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION
    from https://dog.ceo/dog-api/documentation/random
    '''
    links_amount = fixture_amount_links
    responce = requests.get('https://dog.ceo/api/breed/hound/images/random/' + str(links_amount)).json()
    multiple_images_links = responce['message']
    assert len(multiple_images_links) == links_amount and \
            requests.get(multiple_images_links[randint(0, links_amount-1)]).ok


def test_get_list_all_subbreeds(get_list_all_breeds):
    '''
    LIST ALL SUB-BREEDS
    from https://dog.ceo/dog-api/documentation/sub-breed
    '''
    breeds = get_list_all_breeds['message']
    random_breed = choice(list(breeds))
    responce = requests.get(f'https://dog.ceo/api/breed/{random_breed}/list').json()
    assert breeds[random_breed] == responce['message']
