package PortalActions::ISBN;

use warnings;
use strict;

use Exporter;

our @ISA       = qw(Exporter);
our @EXPORT_OK = qw(init_isbn);

use JSON;
use Data::Dumper;

use Fetch;

my $A_isbn_test = 'isbn-test';

# TODO should be library, really
my $C_ISBN_10 = 1;
my $C_ISBN_13 = 2;

sub init_isbn {
    my ($page) = @_;

    add_table_books($page);

    $page->add_page( $A_isbn_test, 'ISBN Test', \&isbn_test );
}

sub add_table_books ($) {
    my ($page) = @_;

    $page->register_table(
        'books',
        {
            ListFields => [qw(id publication_date)],
            ViewFields => [qw(title publication_date pages description)],
            EditFields => [qw(title publication_date pages description)],
            PostView   => \&books_post_view,
        }
    );
}

sub books_post_view {
    my ( $page, $id ) = @_;

    $page->add_section( 'Note', sub { return 'Generate author list here'; },
        0 );
}

sub isbn_test {
    my ($page) = @_;

    my $db = $page->db;

    my $fetcher = Fetch->new();

    # TODO Just some sample books from my library.
    my $books = [
        qw(
          9780330323123
          9780857536020
          9781590593899
          9781937785567
          9781521823637
          9781910463871
          )
    ];

    $fetcher->store_url( 'isbn',
        'https://www.googleapis.com/books/v1/volumes?q=isbn:%s' );

    foreach my $b (@$books) {
#        my $data = $fetcher->retrieve_json( 'isbn', [$b] );
#
#        my $stub = googleapi_to_internal($data);
#
#        my $book_id = add_book( $page, $stub );
    }

    $page->view_multiple_rows(
        [ 'books.id', 'title', 'pages', 'publication_date', 'description' ],
        [], {}, 'Book List' );
    $page->view_multiple_rows( [ 'authors.id', 'name' ], [], {},
        'Author list' );
}

sub add_book ($$) {
    my ( $page, $data ) = @_;

    my $db = $page->db;
    if ( !defined $data->{title} ) { return; }

    my $book = {
        title            => $data->{title},
        publication_date => $data->{publishedDate},
        pages            => $data->{pageCount},
        description      => $data->{description}
    };

    my $book_record = $db->match_optional_single( ['books.id'],
        [ 'title = %title', 'pages = %pages' ], $book );

    my $book_id = ( $book_record->{id} )
      ? $book_record->{id}
      : $db->insert_entry( 'books', $book );

    foreach my $identifier ( @{ $data->{industryIdentifiers} } ) {
        my $isbn  = $identifier->{identifier};
        my $type  = $identifier->{type};
        my $class = ( $type eq 'ISBN_10' ) ? 1 : 2;

        my $record = {
            book            => $book_id,
            identifier_type => $class,
            identifier      => $isbn,
        };

        $db->insert_entry( 'book_identifier', $record );
    }

    foreach my $author ( @{ $data->{authors} } ) {

        my $existing_author =
          $db->match_optional_single( ['authors.id'], ['name = %name'],
            { name => $author } );

        my $ex_auth_id =
          ( $existing_author->{id} )
          ? $existing_author->{id}
          : $db->insert_entry( 'authors', { name => $author } );

        my $record = {
            book   => $book_id,
            author => $ex_auth_id
        };

        $db->insert_entry( 'authorship', $record );
    }

    return $book_id;
}

sub add_author ($$) {
    my ( $db, $name ) = @_;

    my $existing_author =
      $db->match_optional_single( ['authors.id'], ['name = %name'],
        { name => $name } );

    return $existing_author->{id} if $existing_author;

    return $db->insert_entry( 'authors', { name => $name } );
}

sub googleapi_to_internal {
    my ($input) = @_;

    my $item   = $input->{items}[0]{volumeInfo};
    my $return = {};

    my $keep_fields = [
        qw{printType publishedDate pageCount maturityRating
          language title categories description industryIdentifiers}
    ];

    foreach my $key (@$keep_fields) {
        $return->{$key} = $item->{$key};
    }

    $return->{authors} = $item->{authors};

    return $return;

}

1
