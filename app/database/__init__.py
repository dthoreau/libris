from .engine import DataBase

from .books import (get_book_by_id, get_all_books, add_author_to_book,
                    remove_author_from_book, add_award_to_book,
                    remove_award_from_book, add_genre_to_book,
                    remove_genre_from_book, add_series_to_book,
                    remove_series_from_book, add_subject_to_book,
                    remove_subject_from_book)

from .awards import (get_all_awards, get_award_books, get_award_by_id,
                     add_award, find_award_by_name)

from .authors import (get_all_authors, get_author_books, delete_author,
                      get_author_by_id, add_author, find_author_by_name,
                      update_author, count_authors)

from .genres import (get_all_genres, get_genre_books, get_genre_by_id,
                     add_genre, find_genre_by_name)

from .series import (get_all_series, get_series_books, get_series_by_id,
                     add_series, find_series_by_name)

from .subjects import (get_all_subjects, get_subject_books,
                       get_subject_by_id, add_subject,
                       find_subject_by_name)

from .tables import (book_authors, book_awards, book_genres,
                     book_series, book_subjects,  books, authors,
                     awards, series, subjects, genres)

__all__ = ['DataBase',

           'get_all_authors',
           'get_author_books',
           'get_author_by_id',
           'add_author',
           'find_author_by_name',
           'delete_author',
           'update_author',
           'count_authors',

           'get_all_awards',
           'get_award_books',
           'get_award_by_id',
           'add_award',
           'find_award_by_name',

           'get_all_genres',
           'get_genre_books',
           'get_genre_by_id',
           'add_genre',
           'find_genre_by_name',

           'get_all_series',
           'get_series_books',
           'get_series_by_id',
           'add_series',
           'find_series_by_name',

           'get_all_subjects',
           'get_subject_books',
           'get_subject_by_id',
           'add_subject',
           'find_subject_by_name',

           'get_book_by_id',
           'get_all_books',
           'add_author_to_book',
           'remove_author_from_book',

           'add_award_to_book',
           'remove_award_from_book',
           'add_genre_to_book',
           'remove_genre_from_book',
           'add_series_to_book',
           'remove_series_from_book',
           'add_subject_to_book',
           'remove_subject_from_book',


           # ----- database routines
           'get_one', 'get_all', 'insert', 'get_fields',

           # ----- table names
           'book_authors', 'book_awards', 'books', 'authors', 'awards',
           'series', 'subjects', 'genres', 'book_genres',
           'book_series', 'book_subjects',

           ]
