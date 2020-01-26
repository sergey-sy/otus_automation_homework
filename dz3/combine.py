import csv
import json
from contextlib import contextmanager


@contextmanager
def open_file(path, mode='r'):
    try:
        f_obj = open(path, mode)
        yield f_obj
    except OSError:
        print("Can't open file !")
    finally:
        f_obj.close()



def filter_keys(dct, keys) -> dict:
    """Return filtered dict by given keys"""
    return {key: value for key, value in dct.items() if key in keys}


def make_keys_lowercase(dct) -> dict:
    """Change uppercase keys in dictionary to lowercase, if key is string"""
    return {key.lower() if type(key) == str else key: value for key, value in dct.items()}


if __name__ == '__main__':

    need_user_keys = ['name', 'gender', 'address']
    need_book_keys = ['title', 'author', 'height']

    with open_file('users.json') as f:
        users = [filter_keys(dct, need_user_keys) for dct in json.load(f)]
        for dct in users:
            dct['books'] = []

    with open_file('books.csv') as f:
        reader = csv.DictReader(f)
        loaded_books = list(map(lambda row: dict(row), reader))
        books = [filter_keys(make_keys_lowercase(dct), need_book_keys) for dct in loaded_books]

    with open_file('result.json', 'w') as f:

        # distribute all books to all users one by one and save to json file
        next_user = 0
        for book in books:
            users[next_user]['books'].append(book)
            next_user = (next_user + 1) % len(users)
        json.dump(users, f, indent=4)
