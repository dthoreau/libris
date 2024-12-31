from .engine import make_postgres_connection, get_all, get_one, insert

from .books import get_book_by_id, get_all_books

from .awards import (get_all_awards, get_award_books, get_award_by_id)
from .authors import (get_all_authors, get_author_books,
                      get_author_by_id, add_author)
from .genres import get_all_genres, get_genre_books, get_genre_by_id
from .series import get_all_series, get_series_books, get_series_by_id
from .subjects import (get_all_subjects, get_subject_books,
                       get_subject_by_id)

from .tables import (book_authors, book_awards, books, authors, awards,
                     series, subjects, genres)

__all__ = ['make_postgres_connection', 'init',

           'get_all_authors',
           'get_author_books',
           'get_author_by_id',
           'add_author',

           'get_all_awards',
           'get_award_books',
           'get_award_by_id',

           'get_all_genres',
           'get_genre_books',
           'get_genre_by_id',

           'get_all_series',
           'get_series_books',
           'get_series_by_id',

           'get_all_subjects',
           'get_subject_books',
           'get_subject_by_id',

           'get_book_by_id',
           'get_all_books',

           # ----- database routines
           'get_one', 'get_all',

           # ----- table names
           'book_authors', 'book_awards', 'books', 'authors', 'awards',
           'series', 'subjects', 'genres',

           ]
