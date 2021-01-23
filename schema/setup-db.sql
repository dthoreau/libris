begin;

\set ON_ERROR_STOP

create sequence books_seq start 1;

create table books (
	id integer primary key not null default nextval('books_seq'),
	title text not null,
	publication_year numeric(4) not null,
	pages int ,
	publisher text);

create sequence authors_seq start 1;
create table authors (
	id integer primary key not null default nextval('authors_seq'),
	name text not null);

create table authorship (
	book integer not null references books,
	author integer not null references authors
	);



commit;
