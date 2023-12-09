from itertools import cycle

import pytest

import data
from main import BooksCollector


@pytest.fixture()
def collector():
    """Возвращает экземпляр класса BooksCollector."""
    return BooksCollector()


@pytest.fixture
def collector_add_seven_books(collector):
    """Создает словарь с названиями книг из списка data.book_names."""
    collector.books_genre = dict.fromkeys(data.book_names, '')


@pytest.fixture
def collector_add_seven_books_and_set_genres(collector):
    """Создает словарь с названиями книг из списка data.book_names и жанрами."""
    collector.books_genre = dict(zip(data.book_names, cycle(collector.genre)))


@pytest.fixture
def collector_add_two_books_in_favorites(collector):
    """Добавляет книги из списка data.book_names в избранное."""
    collector.favorites.append(data.book_names[0])
    collector.favorites.append(data.book_names[1])
