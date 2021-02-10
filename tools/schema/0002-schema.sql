begin;

\set ON_ERROR_STOP

create sequence schema_seq start 1;

CREATE TABLE local_schema (
	id integer primary key not null default nextval('schema_seq'),
	tag text not null,
	schema text not null);

commit;
