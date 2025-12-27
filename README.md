# qa_python_4

Приложение BooksCollector позволяет управлять коллекцией книг: устанавливать жанры, добавлять книги в избранное и фильтровать их по различным критериям.

Запустить проект можно с помощью команды в терминале: pytest tests.py -v

Сценарии покрытые тестами:

1. test_add_new_book_add_two_books: проверка добавления двух книг
2. test_add_new_book_add_the_same_book: проверка добавления книг с одинаковым названием
3. test_set_book_genre: проверка установки жанра книги
4. test_set_non_existet_genre: проверка установки несуществующего жанра книги
5. test_set_genre_for_non_existet_book: проверка установки жанра для несуществующей книги
6. test_get_book_genre: проверка получения жанра книги по имени
7. test_get_books_with_specific_genre: проверка получения книги с определённым жанром
8. test_get_books_genre: проверка получения словаря books_genre
9. test_get_books_for_children: проверка получения книги, подходящие детям
10. test_add_book_in_favorites: проверка добавления книги в избранное
11. test_delete_book_from_favorites: проверка удаления книги из избранного


