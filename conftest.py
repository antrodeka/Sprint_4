import pytest

from main import BooksCollector

@pytest.fixture(scope='class')
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_with_book_name():
    collector_with_book_name = BooksCollector()
    collector_with_book_name.add_new_book('Война и мир')
    return collector_with_book_name
