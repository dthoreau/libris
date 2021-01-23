begin;

\set ON_ERROR_STOP

drop table authorship, authors, books, book_identifier, identifier_types;

drop sequence books_seq, authors_seq, identifier_seq, identifier_type_seq;

commit;
