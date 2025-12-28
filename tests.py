from main import BooksCollector

import pytest


class TestBooksCollector:

    
    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_add_the_same_book(self, collector):

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 1')

        books = collector.get_books_genre()
        assert len(books) == 1
        assert list(books.keys()) == ['Книга 1']


    def test_set_book_genre(self, collector): 

        collector.add_new_book('Проверочная книга')
        collector.set_book_genre('Проверочная книга', 'Фантастика')

        assert collector.get_book_genre('Проверочная книга') == 'Фантастика'


    def test_set_non_existet_genre(self, collector):

        collector.add_new_book('Проверочная книга')

        collector.set_book_genre('Проверочная книга', 'Несуществующий жанр')

        assert collector.get_book_genre ('Проверочная книга') == ''


    def test_set_genre_for_non_existet_book(self, collector):

        collector.set_book_genre('Несуществующая', 'Ужасы')
        assert collector.get_book_genre ('Несуществующая') is None


    def test_get_book_genre(self, collector):

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')

        assert collector.get_book_genre ('Книга') == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):

        books = ['Книга 1', 'Книга 2', 'Книга 3']

        for book in books:
            collector.add_new_book(book)
        
        collector.set_book_genre('Книга 1', 'Детективы')
        collector.set_book_genre('Книга 2', 'Фантастика')
        collector.set_book_genre('Книга 3', 'Детективы')
        
        detective_books = collector.get_books_with_specific_genre('Детективы')
        assert len(detective_books) == 2
        assert 'Книга 1' in detective_books
        assert 'Книга 3' in detective_books 



    def test_get_books_genre(self, collector):

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')

        books_genre = collector.get_books_genre()

        assert type(books_genre) == dict
        assert 'Книга 1' in books_genre
        assert 'Книга 2' in books_genre
        assert books_genre['Книга 1'] == ''
        assert books_genre['Книга 2'] == ''


    def test_get_books_for_children(self, collector):

        children_books = ['Книга 1', 'Книга 2']
        adult_books = ['Книга 3', 'Книга 4']

        for book in children_books + adult_books:
            collector.add_new_book(book)

    

        collector.set_book_genre('Книга 1', 'Мультфильмы')
        collector.set_book_genre('Книга 2', 'Комедии')
        collector.set_book_genre('Книга 3', 'Ужасы')
        collector.set_book_genre('Книга 4', 'Детективы')

        books_for_children = collector.get_books_for_children()

        assert len(books_for_children) == 2
        assert 'Книга 1' in books_for_children
        assert 'Книга 2' in books_for_children
        assert 'Книга 3' not in books_for_children
        assert 'Книга 4' not in books_for_children


    @pytest.mark.parametrize(
        'book_name', 
        ['Избранная книга 1', 'Избранная книга 2', 'Избранная книга 3']
        )

    def test_add_book_in_favorites(self, book_name, collector):

        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()

        assert book_name in favorites 
        assert len(favorites) == 1


    def test_delete_book_from_favorites(self, collector):

        collector.add_new_book('Удалить книгу')
        collector.add_new_book('Оставить книгу')

        collector.add_book_in_favorites('Удалить книгу')
        collector.add_book_in_favorites('Оставить книгу')

        collector.delete_book_from_favorites('Удалить книгу')

        favorites = collector.get_list_of_favorites_books()

        assert 'Удалить книгу' not in favorites
        assert 'Оставить книгу' in favorites
        assert len(favorites) == 1
