import pytest

from main import BooksCollector
from variables import BOOK_NAME_1, GENRE_FANTASTIC

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope='function')
def collector_with_book_name_and_genre():
    collector_with_book_name = BooksCollector()
    collector_with_book_name.add_new_book(BOOK_NAME_1)
    collector_with_book_name.set_book_genre(BOOK_NAME_1, GENRE_FANTASTIC)
    return collector_with_book_name
