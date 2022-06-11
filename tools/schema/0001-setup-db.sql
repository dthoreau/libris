begin;

\set ON_ERROR_STOP

CREATE SEQUENCE books_seq start 1;

CREATE TABLE books (
id               INTEGER PRIMARY KEY NOT NULL default nextval('books_seq'),
ean              TEXT,
upc              TEXT,
asin             TEXT,
pages            INT,
title            TEXT NOT NULL,
height           TEXT,
length           TEXT,
summary          TEXT,
thickness        TEXT,
page_count       INT,
description      TEXT,
publication      TEXT,
publication_date TEXT);

create sequence author_role_seq start 1;

CREATE TABLE author_roles (
id   TEXT PRIMARY KEY NOT NULL default nextval('author_role_seq'),
name TEXT NOT NULL);

CREATE SEQUENCE authors_seq start 1;

CREATE table authors (
id   INTEGER PRIMARY KEY NOT NULL default nextval('authors_seq'),
name TEXT NOT NULL UNIQUE);

CREATE TABLE authorship (
book   INTEGER NOT NULL references books,
author INTEGER NOT NULL references authors);


CREATE SEQUENCE identifier_type_seq start 1;

CREATE TABLE identifier_types (
id   INTEGER PRIMARY KEY NOT NULL default nextval('identifier_type_seq'),
tag  TEXT NOT NULL,
name TEXT NOT NULL);

insert into identifier_types (name, tag) values ('ISBN-10', 'ISBN_10'),
       ('ISBN 13', 'ISBN_13');

CREATE SEQUENCE identifier_seq start 1;

CREATE TABLE identifier (
id              INTEGER PRIMARY KEY NOT NULL default nextval('identifier_seq'),
book            INTEGER NOT NULL,
identifier      TEXT NOT NULL,
identifier_type INTEGER NOT NULL);

create sequence subject_seq start 1;

CREATE TABLE subjects (
id   INTEGER PRIMARY KEY NOT NULL default nextval('subject_seq'),
name TEXT NOT NULL);

CREATE TABLE book_subjects (
book    INTEGER NOT NULL references books,
subject INTEGER NOT NULL references subjects);



COMMIT;
