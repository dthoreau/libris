begin;

\set ON_ERROR_STOP

create sequence books_seq start 1;

create table books (
	id integer primary key not null default nextval('books_seq'),
	title text not null,
	publication_date text not null,
	pages int ,
	description text);

create sequence authors_seq start 1;
create table authors (
	id integer primary key not null default nextval('authors_seq'),
	name text not null unique);

create table authorship (
	book integer not null references books,
	author integer not null references authors
	);


create sequence identifier_type_seq start 1;

create table identifier_types (
	id integer primary key not null default nextval('identifier_type_seq'),
	name text not null unique,
	tag text not null unique
	);

insert into identifier_types (name, tag) values ('ISBN-10', 'ISBN_10'),
       ('ISBN 13', 'ISBN_13');

create sequence identifier_seq start 1;
create table book_identifier (
	id integer primary key not null default nextval('identifier_seq'),
	book integer references books not null,
	identifier_type integer references identifier_types  not null,
	identifier text not null);




commit;
