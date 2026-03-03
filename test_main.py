import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book_name',
                             ['A',
                              'AB',
                              'Война и мир',
                              'Война и мир, Война и мир, Война и мир, ',
                              'Война и мир, Война и мир, Война и мир, В'])
    def test_add_new_book_add_len_name_less_41_book_added(self, book_name, collector):
        collector.add_new_book(book_name)
        assert collector.books_genre[book_name] == ''
    
    @pytest.mark.parametrize('book_name, genre',
                             [['Война и мир','Фантастика'],
                              ['Пуаро','Детективы'],
                              ['Шерлок Холмс','Детективы']])
    def test_set_book_genre_add_genre_from_list_genre_added(self, book_name, genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_book_name_in_list_get_genre(self, collector):
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_books_with_specific_genre_genre_from_list_list_books_shown(self, collector):
        assert collector.get_books_with_specific_genre('Детективы') == ['Пуаро', 'Шерлок Холмс']

    def test_get_books_genre_list_books_shown(self, collector_with_book_name):
        assert collector_with_book_name.get_books_genre() == {'Война и мир':''}

    def test_get_books_for_children_permitted_books_list_shown(self, collector):
        assert collector.get_books_for_children() == ['Война и мир']

    def test_add_book_in_favorites_book_name_in_book_genre_book_added_in_favorites(self, collector):
        collector.add_book_in_favorites('Война и мир')
        assert collector.favorites[-1] == 'Война и мир'

    def test_get_list_of_favorites_books_list_favorites_books_shown(self, collector):
        assert collector.get_list_of_favorites_books() == collector.favorites

    def test_delete_book_from_favorites_book_name_from_favorites_list_of_favorites_empty(self, collector):
        collector.delete_book_from_favorites('Война и мир')
        assert collector.favorites == []
      