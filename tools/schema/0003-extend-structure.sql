begin;

\set ON_ERROR_STOP

CREATE SEQUENCE dewey_keyword_seq start 1;
CREATE SEQUENCE genres_seq start 1;
CREATE SEQUENCE series_seq start 1;
CREATE SEQUENCE awards_seq start 1;

create table dewey_keywords (
	id INTEGER primary key not null default nextval('dewey_keyword_seq'),
	name text not null
	);

create table book_dewey (
	book INTEGER not null references books,
	keyword INTEGER not null references dewey_keywords
	);

create table genres (
	id INTEGER primary key not null default nextval('genres_seq'),
	name text not null
	);

create table book_genre (
	book INTEGER not null references books,
	genre INTEGER not null references genres
	);

create table series (
	id INTEGER primary key not null default nextval('series_seq'),
	name text not null
	);

create table book_series (
	book INTEGER not null references books,
	series INTEGER not null references series
	);

create table awards (
	id INTEGER primary key not null default nextval('awards_seq'),
	name text not null
	);

create table book_awards (
	book INTEGER not null references books,
	subject INTEGER not null references awards);


commit;
