import pytest
import requests
import string
from jsonschema import validate


API_LINK = 'https://api.openbrewerydb.org/breweries'


@pytest.fixture(scope='module')
def get_all_breweries():
    """Get response with breweries"""
    responce = requests.get(API_LINK)
    if responce.ok:
        return responce.json()
    else:
        print(f"\nSomething went wrong. Can't get breweries list. Status_code= {responce.status_code}")


def test_get_list_breweries(get_all_breweries):
    '''
    Validate json-schema for https://api.openbrewerydb.org/breweries
    Returns a list of breweries.
    '''
    schema = {
        'type': 'object',
        'properties': {
            'id': {"type" : "number"},
            'name': {"type" : "string"},
            'brewery_type': {"type" : "string"},
            'street': {"type" : "string"},
            'city': {"type" : "string"},
            'state': {"type" : "string"},
            'postal_code': {"type" : "string"},
            'country': {"type" : "string"},
            'longitude': {"type" : "string"},
            'latitude': {"type" : "string"},
            'phone': {"type" : "string"},
            'website_url': {"type" : "string"},
            'updated_at': {"type" : "string"},
            'tag_list': {"type" : "array"}
        }
    }

    responce = get_all_breweries
    validate(responce[0], schema)
    # if haven't validate raise exception
    assert True


@pytest.fixture(params=['_', '%20'])
def fixture_with_spaces(request):
    """Return different delimeters for spaces in browser address row"""
    return request.param


@pytest.fixture(params=['san diego', 'alameda'])
def fixture_with_cities(request):
    return request.param


def test_filter_by_city(fixture_with_spaces, fixture_with_cities):
    """Filter breweries by cities. Check different space using"""
    responce = requests.get(API_LINK + f'?by_city=' + fixture_with_spaces.join(fixture_with_cities.split())).json()
    for brewery in responce:
        if brewery['city'] == string.capwords(fixture_with_cities):
            continue
        else:
            raise Exception('Filter by_city do not work')
    assert True


@pytest.mark.parametrize('random_brewery_id', ['141', '44', '198', '46', '2'])
def test_get_single_brewery(random_brewery_id):
    """Test that api return single brewery by id"""
    print(random_brewery_id)
    responce = requests.get(API_LINK + f'/{random_brewery_id}')
    assert responce.ok
