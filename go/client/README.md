# Go API client for swagger

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

## Overview
This API client was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project.  By using the [swagger-spec](https://github.com/swagger-api/swagger-spec) from a remote server, you can easily generate an API client.

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.go.GoClientCodegen

## Installation
Put the package under your project folder and add the following in import:
```golang
import "./swagger"
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorApi* | [**AuthorGet**](docs/AuthorApi.md#authorget) | **Get** /author | Fetch ISBN list of authors works
*AwardApi* | [**AwardGet**](docs/AwardApi.md#awardget) | **Get** /award | list of books that have won this award
*BookApi* | [**BookIsbnGet**](docs/BookApi.md#bookisbnget) | **Get** /book/{isbn} | Retrieve an existing book
*BookApi* | [**BookPost**](docs/BookApi.md#bookpost) | **Post** /book | Add a new book to the library
*BookApi* | [**BookPut**](docs/BookApi.md#bookput) | **Put** /book | Update an existing book
*BookApi* | [**BooksGet**](docs/BookApi.md#booksget) | **Get** /books | Retrieve multiple books
*InformationalApi* | [**StatsGet**](docs/InformationalApi.md#statsget) | **Get** /stats | provide statistics on known books
*SeriesApi* | [**SeriesGet**](docs/SeriesApi.md#seriesget) | **Get** /series | List of books in this series
*SeriesApi* | [**SubjectsGet**](docs/SeriesApi.md#subjectsget) | **Get** /subjects | list of books in subject

## Documentation For Models

 - [Book](docs/Book.md)
 - [Isbn](docs/Isbn.md)

## Documentation For Authorization
 Endpoints do not require authorization.


## Author

