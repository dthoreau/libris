--
-- PostgreSQL database dump
--

-- Dumped from database version 14.15 (Ubuntu 14.15-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.15 (Ubuntu 14.15-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: libris; Type: DATABASE; Schema: -; Owner: libris
--

CREATE DATABASE libris WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'C.UTF-8';


ALTER DATABASE libris OWNER TO libris;

\connect libris

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: author_role_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.author_role_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.author_role_seq OWNER TO libris;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: author_roles; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.author_roles (
    id text DEFAULT nextval('public.author_role_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.author_roles OWNER TO libris;

--
-- Name: authors_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.authors_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authors_seq OWNER TO libris;

--
-- Name: authors; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.authors (
    id integer DEFAULT nextval('public.authors_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.authors OWNER TO libris;

--
-- Name: authorship; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.authorship (
    book integer NOT NULL,
    author integer NOT NULL
);


ALTER TABLE public.authorship OWNER TO libris;

--
-- Name: awards_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.awards_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.awards_seq OWNER TO libris;

--
-- Name: awards; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.awards (
    id integer DEFAULT nextval('public.awards_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.awards OWNER TO libris;

--
-- Name: book_awards; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.book_awards (
    book integer NOT NULL,
    award integer NOT NULL
);


ALTER TABLE public.book_awards OWNER TO libris;

--
-- Name: book_dewey; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.book_dewey (
    book integer NOT NULL,
    keyword integer NOT NULL
);


ALTER TABLE public.book_dewey OWNER TO libris;

--
-- Name: book_genre; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.book_genre (
    book integer NOT NULL,
    genre integer NOT NULL
);


ALTER TABLE public.book_genre OWNER TO libris;

--
-- Name: book_series; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.book_series (
    book integer NOT NULL,
    series integer NOT NULL
);


ALTER TABLE public.book_series OWNER TO libris;

--
-- Name: book_subjects; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.book_subjects (
    book integer NOT NULL,
    subject integer NOT NULL
);


ALTER TABLE public.book_subjects OWNER TO libris;

--
-- Name: books_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.books_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_seq OWNER TO libris;

--
-- Name: books; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.books (
    id integer DEFAULT nextval('public.books_seq'::regclass) NOT NULL,
    ean text,
    upc text,
    asin text,
    pages integer,
    title text NOT NULL,
    height text,
    length text,
    summary text,
    thickness text,
    page_count integer,
    description text,
    publication text,
    publication_date text
);


ALTER TABLE public.books OWNER TO libris;

--
-- Name: dewey_keyword_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.dewey_keyword_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dewey_keyword_seq OWNER TO libris;

--
-- Name: dewey_keywords; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.dewey_keywords (
    id integer DEFAULT nextval('public.dewey_keyword_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.dewey_keywords OWNER TO libris;

--
-- Name: genres_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.genres_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genres_seq OWNER TO libris;

--
-- Name: genres; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.genres (
    id integer DEFAULT nextval('public.genres_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.genres OWNER TO libris;

--
-- Name: identifier_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.identifier_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.identifier_seq OWNER TO libris;

--
-- Name: identifier; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.identifier (
    id integer DEFAULT nextval('public.identifier_seq'::regclass) NOT NULL,
    book integer NOT NULL,
    identifier text NOT NULL,
    identifier_type integer NOT NULL
);


ALTER TABLE public.identifier OWNER TO libris;

--
-- Name: identifier_type_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.identifier_type_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.identifier_type_seq OWNER TO libris;

--
-- Name: identifier_types; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.identifier_types (
    id integer DEFAULT nextval('public.identifier_type_seq'::regclass) NOT NULL,
    tag text NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.identifier_types OWNER TO libris;

--
-- Name: schema_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.schema_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schema_seq OWNER TO libris;

--
-- Name: local_schema; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.local_schema (
    id integer DEFAULT nextval('public.schema_seq'::regclass) NOT NULL,
    tag text NOT NULL,
    schema text NOT NULL
);


ALTER TABLE public.local_schema OWNER TO libris;

--
-- Name: series_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.series_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.series_seq OWNER TO libris;

--
-- Name: series; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.series (
    id integer DEFAULT nextval('public.series_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.series OWNER TO libris;

--
-- Name: subject_seq; Type: SEQUENCE; Schema: public; Owner: libris
--

CREATE SEQUENCE public.subject_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subject_seq OWNER TO libris;

--
-- Name: subjects; Type: TABLE; Schema: public; Owner: libris
--

CREATE TABLE public.subjects (
    id integer DEFAULT nextval('public.subject_seq'::regclass) NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.subjects OWNER TO libris;

--
-- Name: author_roles author_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.author_roles
    ADD CONSTRAINT author_roles_pkey PRIMARY KEY (id);


--
-- Name: authors authors_name_key; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_name_key UNIQUE (name);


--
-- Name: authors authors_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);


--
-- Name: awards awards_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.awards
    ADD CONSTRAINT awards_pkey PRIMARY KEY (id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: dewey_keywords dewey_keywords_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.dewey_keywords
    ADD CONSTRAINT dewey_keywords_pkey PRIMARY KEY (id);


--
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);


--
-- Name: identifier identifier_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.identifier
    ADD CONSTRAINT identifier_pkey PRIMARY KEY (id);


--
-- Name: identifier_types identifier_types_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.identifier_types
    ADD CONSTRAINT identifier_types_pkey PRIMARY KEY (id);


--
-- Name: local_schema local_schema_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.local_schema
    ADD CONSTRAINT local_schema_pkey PRIMARY KEY (id);


--
-- Name: series series_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_pkey PRIMARY KEY (id);


--
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (id);


--
-- Name: authorship authorship_author_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.authorship
    ADD CONSTRAINT authorship_author_fkey FOREIGN KEY (author) REFERENCES public.authors(id);


--
-- Name: authorship authorship_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.authorship
    ADD CONSTRAINT authorship_book_fkey FOREIGN KEY (book) REFERENCES public.books(id);


--
-- Name: book_awards book_awards_award_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_awards
    ADD CONSTRAINT book_awards_award_fkey FOREIGN KEY (award) REFERENCES public.awards(id);


--
-- Name: book_awards book_awards_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_awards
    ADD CONSTRAINT book_awards_book_fkey FOREIGN KEY (book) REFERENCES public.books(id);


--
-- Name: book_dewey book_dewey_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_dewey
    ADD CONSTRAINT book_dewey_book_fkey FOREIGN KEY (book) REFERENCES public.books(id);


--
-- Name: book_dewey book_dewey_keyword_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_dewey
    ADD CONSTRAINT book_dewey_keyword_fkey FOREIGN KEY (keyword) REFERENCES public.dewey_keywords(id);


--
-- Name: book_genre book_genre_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_genre
    ADD CONSTRAINT book_genre_book_fkey FOREIGN KEY (book) REFERENCES public.books(id);


--
-- Name: book_genre book_genre_genre_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_genre
    ADD CONSTRAINT book_genre_genre_fkey FOREIGN KEY (genre) REFERENCES public.genres(id);


--
-- Name: book_series book_series_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_series
    ADD CONSTRAINT book_series_book_fkey FOREIGN KEY (book) REFERENCES public.books(id);


--
-- Name: book_series book_series_series_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_series
    ADD CONSTRAINT book_series_series_fkey FOREIGN KEY (series) REFERENCES public.series(id);


--
-- Name: book_subjects book_subjects_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_subjects
    ADD CONSTRAINT book_subjects_book_fkey FOREIGN KEY (book) REFERENCES public.books(id);


--
-- Name: book_subjects book_subjects_subject_fkey; Type: FK CONSTRAINT; Schema: public; Owner: libris
--

ALTER TABLE ONLY public.book_subjects
    ADD CONSTRAINT book_subjects_subject_fkey FOREIGN KEY (subject) REFERENCES public.subjects(id);


--
-- PostgreSQL database dump complete
--

