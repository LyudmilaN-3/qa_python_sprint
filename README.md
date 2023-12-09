# qa_python_sprint_4

### **В проекте реализованы тесты:**

#### **позитивные**

#### 1 `test_add_new_book_no_books_added_seven_books`
*     Проверяет добавление новых книг.
#### 2 `test_set_book_genre_seven_books_set_genre`
*     Проверяет установление жанров для книг.
#### 3 `test_get_book_genre_seven_books_with_genres_got_book`
*     Проверяет получение жанра книги по ее нозванию.
#### 4 `test_get_books_with_specific_genre_seven_books_with_genres_got_books`
*     Проверяет вывод списка книг по жанру.
#### 5 `test_get_books_genre_seven_books_with_genres_got_books_genre`
*     Проверяет вывод словаря с названиями и жанрами книг.
#### 6 `test_get_books_for_children_seven_books_with_genres_got_books_genre`
*     Проверяет вывод списка книг без возрастного рейтинга
#### 7 `test_add_book_in_favorites_seven_books_added_book`
*     Проверяет добавление новых книг в избранное.
#### 8 `test_delete_book_from_favorites_seven_books_deleted_book`
*     Проверяет удаление книги из избранного.
#### 9 `test_get_list_of_favorites_books_seven_books_got_favorites`
*     Проверяет вывод списка книг из избранного.

#### **негативные**

#### 1 `test_add_new_book_seven_books_not_valid_name_no_added`
*     Проверяет добавление книг с недопустимыми названиями.
#### 2 `test_set_book_genre_seven_books_not_valid_name_genre_not_set`
*     Проверяет установление жанров: недопустимых и для отсутствующих книг.
#### 3 `test_add_book_in_favorites_two_books_already_added_book_not_added`
*     Проверяет повторное добавление книг в избранное.
