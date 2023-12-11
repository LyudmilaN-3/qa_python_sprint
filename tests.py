import pytest

import data


class TestBooksCollector:

    def test_add_new_book_no_books_added_one_books(self, collector):
        """Проверяет добавление новой книги."""
        collector.add_new_book('Название книги')
        assert len(collector.books_genre) == 1

    def test_add_new_book_one_books_exist_book_no_added(
            self, collector, collector_add_one_book):
        """Проверяет добавление уже добавленной книги."""
        len_before_add = len(collector.books_genre)
        collector.add_new_book(data.one_book_name)
        len_after_add = len(collector.books_genre)
        assert len_before_add == len_after_add

    @pytest.mark.parametrize(
        'name',
        [
         '',
         'Название книги более 40 символов: 41 симв',
         'Название книги более 40 символов: 42 симво'
        ]
    )
    def test_add_new_book_no_books_not_valid_len_name_no_added(
            self, collector, name):
        """Проверяет добавление книг с недопустимыми по длине названиями."""
        len_before_add = len(collector.books_genre)
        collector.add_new_book(name)
        len_after_add = len(collector.books_genre)
        assert len_before_add == len_after_add

    @pytest.mark.parametrize(
        'name',
        [
            'Н',
            'На',
            'Название книги 39 символов - название--',
            'Название книги 40 символов - название---',
        ]
    )
    def test_add_new_book_no_books_valid_len_name_added(
            self, collector, name):
        """
        Проверяет добавление книг с допустимыми граничными по длине названиями.
        """
        len_before_add = len(collector.books_genre)
        collector.add_new_book(name)
        len_after_add = len(collector.books_genre)
        assert len_before_add + 1 == len_after_add

    def test_set_book_genre_one_book_set_genres(
            self, collector, collector_add_one_book):
        """Проверяет установление жанра для книги."""
        collector.set_book_genre(data.one_book_name, collector.genre[0])
        assert collector.books_genre[data.one_book_name] == collector.genre[0]

    def test_set_book_genre_one_book_exist_book_not_set(
            self, collector, collector_add_one_book):
        """
        Проверяет установление жанра
        для отсутствующей в словаре books_genre книги.
        """
        new_name = f'Инoe {data.one_book_name}'
        len_books_genre_before_set = len(collector.books_genre)
        len_genre_lst_before_set = 0
        for name in collector.books_genre:
            if collector.books_genre[name] != '':
                len_genre_lst_before_set += 1
        collector.set_book_genre(new_name, collector.genre[0])
        len_books_genre_after_set = len(collector.books_genre)
        len_genre_lst_after_set = 0
        for name in collector.books_genre:
            if collector.books_genre[name] != '':
                len_genre_lst_after_set += 1
        assert (len_books_genre_before_set == len_books_genre_after_set
                and
                len_genre_lst_before_set == len_genre_lst_after_set)

    def test_set_book_genre_one_book_not_exist_genre_not_set(
            self, collector, collector_add_one_book):
        """Проверяет установление отсутствующего жанра."""
        name = data.one_book_name
        new_genre = f'Не {collector.genre[0]}'
        len_books_genre_before_set = len(collector.books_genre)
        len_genre_lst_before_set = 0
        for name in collector.books_genre:
            if collector.books_genre[name] != '':
                len_genre_lst_before_set += 1
        collector.set_book_genre(name, new_genre)
        len_books_genre_after_set = len(collector.books_genre)
        len_genre_lst_after_set = 0
        for name in collector.books_genre:
            if collector.books_genre[name] != '':
                len_genre_lst_after_set += 1
        assert (len_books_genre_before_set == len_books_genre_after_set
                and
                len_genre_lst_before_set == len_genre_lst_after_set)

    def test_get_book_genre_one_book_with_genre_got_genre(
            self, collector, collector_add_one_book_and_set_genre):
        """Проверяет получение жанра книги по ее названию."""
        genre_for_name = collector.get_book_genre(data.one_book_name)
        assert genre_for_name == collector.books_genre[data.one_book_name]

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

    def test_get_books_genre_one_book_with_genres_got_books_genre(
            self, collector, collector_add_one_book_and_set_genre):
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

    def test_get_books_for_children_seven_books_with_genres_not_got_books_with_genre_age_rating(
            self, collector, collector_add_seven_books_and_set_genres):
        """
        Проверяет отсутствие в списке книг для детей
        книг с возрастным рейтингом.
        """
        temp_lst = collector.get_books_for_children()
        for name in collector.books_genre:
            if collector.books_genre[name] in collector.genre_age_rating:
                assert collector.books_genre[name] not in temp_lst

    def test_add_book_in_favorites_one_book_added_book(
            self, collector, collector_add_one_book):
        """Проверяет добавление новой книги в избранное."""
        collector.add_book_in_favorites(data.one_book_name)
        assert data.one_book_name in collector.favorites

    def test_add_book_in_favorites_one_book_already_added_book_not_added(
            self, collector, collector_add_one_book_in_favorites):
        """Проверяет повторное добавление книги в избранное."""
        len_favorites_before_add = len(collector.favorites)
        collector.add_book_in_favorites(data.one_book_name)
        len_favorites_after_add = len(collector.favorites)
        assert len_favorites_before_add == len_favorites_after_add

    def test_delete_book_from_favorites_one_book_deleted_book(
            self, collector, collector_add_one_book_in_favorites):
        """Проверяет удаление книги из избранного."""
        collector.delete_book_from_favorites(data.one_book_name)
        assert data.one_book_name not in collector.favorites

    def test_get_list_of_favorites_books_seven_books_got_favorites(
            self, collector, collector_add_seven_books):
        """Проверяет вывод списка книг из избранного."""
        value = collector.books_genre.keys()
        collector.favorites.append(list(value)[0])
        collector.favorites.append(list(value)[1])
        assert collector.get_list_of_favorites_books() == collector.favorites
