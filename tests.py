import pytest

import data


class TestBooksCollector:

    def test_add_new_book_no_books_added_seven_books(self, collector):
        """Проверяет добавление новых книг."""
        for book_name in data.book_names:
            collector.add_new_book(book_name)
        assert len(collector.books_genre) == len(data.book_names)

    @pytest.mark.parametrize(
        'name',
        [
         'Название книги более 40 символов, а именно 45',
         'Что делать, если ваш кот хочет вас убить'
        ]
    )
    def test_add_new_book_seven_books_not_valid_name_no_added(
            self, collector, collector_add_seven_books, name):
        """Проверяет добавление книг с недопустимыми названиями."""
        len_before_add = len(collector.books_genre)
        collector.add_new_book(name)
        len_after_add = len(collector.books_genre)
        assert len_before_add == len_after_add

    def test_set_book_genre_seven_books_set_genres(
            self, collector, collector_add_seven_books):
        """Проверяет установление жанров для книг."""
        i = 0
        for book_name in data.book_names:
            i = i % len(collector.genre)
            collector.set_book_genre(book_name, collector.genre[i])
            est_book_genre = collector.books_genre[book_name]
            genre_in_lst = collector.genre[i]
            i += 1
            assert est_book_genre == genre_in_lst

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Название книги более 40 символов, а именно 45', 'Комедии'],
            ['Что делать, если ваш кот хочет вас убить', 'Драмы'],
        ]
    )
    def test_set_book_genre_seven_books_not_valid_name_genre_not_set(
            self, collector, collector_add_seven_books, name, genre):
        """
        Проверяет установление жанров: недопустимых и для отсутствующих книг.
        """
        len_books_genre_before_set = len(collector.books_genre)
        len_set_genre_lst_before_set = len(list(filter(
                lambda x: collector.books_genre[x]
                if (name in collector.books_genre
                    and collector.books_genre[name] != '')
                else False, collector.books_genre)))
        collector.set_book_genre(name, genre)
        len_books_genre_after_set = len(collector.books_genre)
        len_set_genre_lst_after_set = len(list(filter(
                lambda x: collector.books_genre[x]
                if (name in collector.books_genre
                    and collector.books_genre[name] != '')
                else False, collector.books_genre)))
        assert (len_books_genre_before_set == len_books_genre_after_set
                and
                len_set_genre_lst_before_set == len_set_genre_lst_after_set)

    def test_get_book_genre_seven_books_with_genres_got_book(
            self, collector, collector_add_seven_books_and_set_genres):
        """Проверяет получение жанра книги по ее нозванию."""
        i = 0
        for book_name in data.book_names:
            i = i % len(collector.genre)
            genre_for_name = collector.get_book_genre(book_name)
            genre_in_lst = collector.genre[i]
            i += 1
            assert genre_for_name == genre_in_lst

    def test_get_books_with_specific_genre_seven_books_with_genres_got_books(
            self, collector, collector_add_seven_books_and_set_genres):
        """Проверяет вывод списка книг по жанру."""
        for i in range(len(collector.genre)):
            lst_books_with_genre = collector.get_books_with_specific_genre(
                collector.genre[i])
            books_lst = list(
                filter(lambda x:
                       collector.books_genre[x] == collector.genre[i],
                       collector.books_genre))
            assert lst_books_with_genre == books_lst

    def test_get_books_genre_seven_books_with_genres_got_books_genre(
            self, collector, collector_add_seven_books_and_set_genres):
        """Проверяет вывод словаря с названиями и жанрами книг."""
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_seven_books_with_genres_got_books_genre(
            self, collector, collector_add_seven_books_and_set_genres):
        """Проверяет вывод списка книг без возрастного рейтинга."""
        books_lst_without_age_rating = []
        for i in range(len(collector.genre)):
            current_lst = list(filter(
                lambda x: collector.books_genre[x] == collector.genre[i]
                if collector.genre[i] not in collector.genre_age_rating
                else False, collector.books_genre)
            )
            books_lst_without_age_rating.extend(current_lst)
        books_lst_without_age_rating.sort()
        temp_lst = collector.get_books_for_children()
        temp_lst.sort()
        assert temp_lst == books_lst_without_age_rating

    def test_add_book_in_favorites_seven_books_added_book(
            self, collector, collector_add_seven_books):
        """Проверяет добавление новых книг в избранное."""
        value = list(collector.books_genre.keys())[0]
        collector.add_book_in_favorites(value)
        assert data.book_names[0] in collector.favorites

    @pytest.mark.parametrize('name',
                             ['Что делать, если ваш кот хочет вас убить'])
    def test_add_book_in_favorites_two_books_already_added_book_not_added(
            self, collector, collector_add_seven_books,
            collector_add_two_books_in_favorites, name):
        """Проверяет повторное добавление книг в избранное."""
        len_favorites_before_add = len(collector.favorites)
        collector.add_book_in_favorites(name)
        len_favorites_after_add = len(collector.favorites)
        assert len_favorites_before_add == len_favorites_after_add

    def test_delete_book_from_favorites_seven_books_deleted_book(
            self, collector, collector_add_seven_books,
            collector_add_two_books_in_favorites):
        """Проверяет удаление книги из избранного."""
        value = collector.favorites[0]
        collector.delete_book_from_favorites(value)
        assert data.book_names[0] not in collector.favorites

    def test_get_list_of_favorites_books_seven_books_got_favorites(
            self, collector, collector_add_seven_books,
            collector_add_two_books_in_favorites):
        """Проверяет вывод списка книг из избранного."""
        value = collector.books_genre.keys()
        collector.favorites.append(list(value)[0])
        collector.favorites.append(list(value)[1])
        assert collector.get_list_of_favorites_books() == collector.favorites
