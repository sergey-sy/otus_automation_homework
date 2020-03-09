import pytest
import requests
import json
import os
from jsonschema import validate


API_LINK = 'https://jsonplaceholder.typicode.com/posts'
TMP_FILE = 'test_jsonplaceholder.json'


@pytest.yield_fixture(scope='session', autouse=True)
def make_tmp_file():
    with open(TMP_FILE, 'w') as f:
        pass
    yield
    os.remove(TMP_FILE)


@pytest.fixture(scope='module')
def get_api_responce():
    responce = requests.get(API_LINK)
    if responce.ok:
        print(responce)
        with open(TMP_FILE, 'w') as write_file:
            json.dump(responce.json(), write_file, indent=4)
        return responce.json()
    else:
        print(f"\nSomething went wrong. Can't get responce from api. Status_code= {responce.status_code}")


def test_check_json_schema(get_api_responce):
    '''Validate json-schema for https://jsonplaceholder.typicode.com/guide.html'''
    schema = {
        'type': 'object',
        'properties': {
            'id': {"type" : "number"},
            'title': {"type" : "string"},
            'body': {"type" : "string"},
            'userId': {"type" : "number"},
        }
    }

    responce = get_api_responce
    validate(responce[0], schema)
    # if haven't validate raise exception
    assert True


def test_get_single_resource():
    """Check that possible to get one resource"""
    responce = requests.get(f'{API_LINK}/1').json()
    with open('test_jsonplaceholder.json') as f:
        assert json.load(f)[0] == responce


@pytest.mark.parametrize("_id", [1, 100])
class TestClassParametrized:

    def test_create_source(self, _id):
        """Check that possible to get source"""
        send_data = {
            "userId": 1,
            "id": _id,
            "title": "test title",
            "body": "test body"
        }
        responce = requests.post(API_LINK, send_data)
        print(responce.status_code)
        assert responce.ok

    def test_update_source(self, _id):
        """Check that impossible update source"""
        send_data = {
            "userId": 1,
            "id": _id,
            "title": "test title",
            "body": "test body"
        }
        responce = requests.put(f'{API_LINK}/{_id}', send_data)
        print(responce.status_code)
        assert responce.ok

    def test_delete_resource(self, _id):
        """Check delete resource"""
        responce = requests.delete(f'{API_LINK}/{_id}')
        print(responce.status_code)
        assert responce.ok
