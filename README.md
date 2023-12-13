# qa_python_sprint_4

### **В проекте реализованы тесты:**

#### **позитивные**

#### 1 `test_add_new_book_no_books_added_one_books`
*     Проверяет добавление новой книги.
#### 2 `test_add_new_book_no_books_valid_len_name_added`
*     Проверяет добавление книг с допустимыми граничными по длине названиями.
#### 3 `test_set_book_genre_one_book_set_genres`
*     Проверяет установление жанра для книги.
#### 4 `test_get_book_genre_one_book_with_genre_got_genre`
*     Проверяет получение жанра книги по ее названию.
#### 5 `test_get_books_with_specific_genre_seven_books_with_genres_got_books`
*     Проверяет вывод списка книг по жанру.
#### 6 `test_get_books_genre_one_book_with_genres_got_books_genr`
*     Проверяет вывод словаря с названиями и жанрами книг.
#### 7 `test_get_books_for_children_seven_books_with_genres_got_books_genre`
*     Проверяет вывод списка книг без возрастного рейтинга.
#### 8 `test_get_books_for_children_seven_books_with_genres_not_got_books_with_genre_age_rating`
*     Проверяет отсутствие в списке книг для детей книг с возрастным рейтингом.
#### 9 `test_add_book_in_favorites_one_book_added_book`
*     Проверяет добавление новой книги в избранное.
#### 10 `test_delete_book_from_favorites_one_book_deleted_book`
*     Проверяет удаление книги из избранного.
#### 11 `test_get_list_of_favorites_books_seven_books_got_favorites`
*     Проверяет вывод списка книг из избранного.

#### **негативные**

#### 1 `test_add_new_book_one_books_exist_book_no_added`
*     Проверяет добавление уже добавленной книги.
#### 2 `test_add_new_book_no_books_not_valid_len_name_no_added`
*     Проверяет добавление книг с недопустимыми по длине названиями.
#### 3 `test_set_book_genre_one_book_exist_book_not_set`
*     Проверяет установление жанра для отсутствующей в словаре books_genre книги.
#### 4 `test_set_book_genre_one_book_not_exist_genre_not_set`
*     Проверяет установление отсутствующего жанра.
#### 5 `test_add_book_in_favorites_one_book_already_added_book_not_added`
*     Проверяет повторное добавление книги в избранное.
