begin;

\set ON_ERROR_STOP

drop table authorship, authors, books, identifier, identifier_types,
     author_roles;

drop sequence books_seq, authors_seq, identifier_seq, identifier_type_seq,
     author_role_seq;

commit;
