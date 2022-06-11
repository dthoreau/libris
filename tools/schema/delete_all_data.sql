begin;

-- trashes all data. mostly used to test import script. beware
\set ON_ERROR_STOP

delete from book_awards;
delete from book_dewey;
delete from book_genre;
delete from book_series;
delete from book_subjects;
delete from authorship;
delete from author_roles;
delete from authors;
delete from awards;
delete from books;
delete from dewey_keywords;
delete from genres;
delete from identifier_types;
delete from identifier;
delete from series;
delete from subjects;


commit;
