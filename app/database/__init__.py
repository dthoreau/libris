from .engine import make_postgres_connection, get_all, get_one

from .books import get_book_by_id, get_all_books

from awards import (get_all_awards, get_award_books, get_award_by_id)
from authors import get_all_authors
from genres import get_all_genres
from series import get_all_series
from subjects import get_all_subjects

from .tables import (book_authors, book_awards, books, authors, awards,
                     series, subjects, genres)

__all__ = ['make_postgres_connection', 'init',

           'get_all_authors',

           'get_all_awards',
           'get_award_books',
           'get_award_by_id',

           'get_all_genres',

           'get_all_series',

           'get_all_subjects',

           'get_book_by_id',
           'get_all_books',

           # ----- database routines
           'get_one', 'get_all',

           # ----- table names
           'book_authors', 'book_awards', 'books', 'authors', 'awards',
           'series', 'subjects', 'genres',

           ]
