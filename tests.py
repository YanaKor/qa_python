import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    case_1 = ['Граф Монте-Кристо', 1]
    case_2 = ['Три мушкетера', 2]
    case_3 = ['Война и мир', 5]
    case_4 = ['Евгений Онегин', 9]
    case_5 = ['Вишневый сад', 10]

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_two_items_with_similar_name_added_only_one(self):
        """Добавление двух книг с одинаковым названием. ОР: Добавлена только одна книга"""

        collector = BooksCollector()

        collector.add_new_book('Горе от ума')
        collector.add_new_book('Горе от ума')

        assert len(collector.get_books_rating()) == 1

    @pytest.mark.parametrize('name, rating', (case_1, case_2, case_3, case_4, case_5))
    def test_set_book_rating_set_rating_for_book_rating_is_equal_to_the_established(self, name, rating):
        """Параметризация тестов на проверку установки рейтинга. ОР: Рейтинг равен установленному"""

        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) == rating

    def test_set_book_rating_set_rating_0_book_rating_is_equal_to_1(self):
        """Проверка установки рейтинга = 0. ОР: Рейтинг равен 1"""

        collector = BooksCollector()

        collector.add_new_book('Тихий дон')
        collector.set_book_rating('Тихий дон', 1)

        assert collector.get_book_rating('Тихий дон') == 1

    def test_set_book_rating_set_rating_11_book_rating_is_equal_to_1(self):
        """Проверка установки рейтинга =  11. ОР: Рейтинг равен 1"""

        collector = BooksCollector()

        collector.add_new_book('Отцы и дети')
        collector.set_book_rating('Отцы и дети', 11)

        assert collector.get_book_rating('Отцы и дети') == 1

    def test_get_books_with_specific_rating_for_dont_exist_rating(self):
        """Проверка книг с несущестивующим рейтингом. ОР: Выведется пустой список"""
        collector = BooksCollector()

        collector.add_new_book('Анна Каренина')

        assert len(collector.get_books_with_specific_rating(3)) == 0

    def test_get_books_with_specific_rating(self):
        """Проверка книг с одинаковым рейтингом. ОР: Выведутся книги с одинаковым рейтингом"""

        collector = BooksCollector()

        collector.add_new_book('Идиот')
        collector.set_book_rating('Идиот', 5)
        collector.add_new_book('Му-му')
        collector.set_book_rating('Му-му', 5)
        assert len(collector.get_books_with_specific_rating(5)) == 2

    def test_add_book_in_favorites_empty_list_of_favourite_books(self):
        """Проверка списка favorites, если не добавлены книги. ОР: Выведется пустой список"""

        collector = BooksCollector()
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_book_to_favourite_list(self):
        """Проверка списка favorites с добавленной избранной книгой. ОР: Выводится добавленная книга"""

        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']

    def test_delete_book_from_favorites_delete_nonexist_book_from_list_empty_favourite_list(self):
        """Удаление несуществующей книги из избранного. ОР: Выведется пустой список"""

        collector = BooksCollector()

        collector.delete_book_from_favorites('Ревизор')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_add_and_delete_books_from_favourite_empty_favourite_list(self):
        """Добавление и удаление книги из избранного. ОР: Выведется пустой список"""

        collector = BooksCollector()

        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')
        collector.delete_book_from_favorites('Преступление и наказание')
        assert len(collector.get_list_of_favorites_books()) == 0