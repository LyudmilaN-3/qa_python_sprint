from itertools import cycle

import pytest

import data
from main import BooksCollector


@pytest.fixture()
def collector():
    """Возвращает экземпляр класса BooksCollector."""
    return BooksCollector()


@pytest.fixture
def collector_add_one_book(collector):
    """Создает словарь с одной книгой."""
    collector.books_genre[data.one_book_name] = ''


@pytest.fixture
def collector_add_seven_books(collector):
    """Создает словарь с названиями книг из списка data.book_names."""
    collector.books_genre = dict.fromkeys(data.book_names, '')


@pytest.fixture
def collector_add_one_book_and_set_genre(collector):
    """Создает словарь с одной книгой и присваивает ей жанр."""
    collector.books_genre[data.one_book_name] = collector.genre[0]


@pytest.fixture
def collector_add_seven_books_and_set_genres(collector):
    """
    Создает словарь с названиями книг из списка data.book_names и жанрами.
    """
    collector.books_genre = dict(zip(data.book_names, cycle(collector.genre)))


@pytest.fixture
def collector_add_one_book_in_favorites(collector, collector_add_one_book):
    """Добавляет книги из списка data.book_names в избранное."""
    collector.favorites.append(data.one_book_name)
