import pytest

from variables import (BOOK_NAME_1,
                       GENRE_FANTASTIC,
                       BOOKS_NAME_LESS_THEN_41_SIMBOLS,
                       BOOK_NAMES_AND_GENRES)


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', BOOKS_NAME_LESS_THEN_41_SIMBOLS)
    def test_add_new_book_add_len_name_less_41_book_added(self, book_name, collector):
        collector.add_new_book(book_name)
        assert collector.books_genre[book_name] == ''
    
    @pytest.mark.parametrize('book_name, genre', BOOK_NAMES_AND_GENRES)
    def test_set_book_genre_add_genre_from_list_genre_added(self, book_name, genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_book_name_in_list_get_genre(self, collector):
        collector.add_new_book(BOOK_NAME_1)
        collector.set_book_genre(BOOK_NAME_1, GENRE_FANTASTIC)
        assert collector.get_book_genre(BOOK_NAME_1) == GENRE_FANTASTIC

    def test_get_books_with_specific_genre_genre_from_list_list_books_shown(self, collector_with_book_name_and_genre):
        assert collector_with_book_name_and_genre.get_books_with_specific_genre(GENRE_FANTASTIC) == [BOOK_NAME_1]

    def test_get_books_genre_list_books_shown(self, collector_with_book_name_and_genre):
        assert collector_with_book_name_and_genre.get_books_genre() == {BOOK_NAME_1:GENRE_FANTASTIC}

    def test_get_books_for_children_permitted_books_list_shown(self, collector_with_book_name_and_genre):
        assert collector_with_book_name_and_genre.get_books_for_children() == [BOOK_NAME_1]

    def test_add_book_in_favorites_book_name_in_book_genre_book_added_in_favorites(self, collector_with_book_name_and_genre):
        collector_with_book_name_and_genre.add_book_in_favorites(BOOK_NAME_1)
        assert collector_with_book_name_and_genre.favorites[-1] == BOOK_NAME_1

    def test_get_list_of_favorites_books_list_favorites_books_shown(self, collector_with_book_name_and_genre):
        collector_with_book_name_and_genre.add_book_in_favorites(BOOK_NAME_1)
        assert collector_with_book_name_and_genre.get_list_of_favorites_books() == [BOOK_NAME_1]

    def test_delete_book_from_favorites_book_name_from_favorites_list_of_favorites_empty(self, collector_with_book_name_and_genre):
        collector_with_book_name_and_genre.add_book_in_favorites(BOOK_NAME_1)
        collector_with_book_name_and_genre.delete_book_from_favorites(BOOK_NAME_1)
        assert collector_with_book_name_and_genre.get_list_of_favorites_books() == []
      