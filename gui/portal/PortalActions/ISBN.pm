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

    $page->add_page( $A_isbn_test, 'ISBN Test', \&isbn_test );
}

sub isbn_test {
    my ($page) = @_;

    my $db = $page->db;

    my $fetcher = Fetch->new();

    $fetcher->store_url( 'isbn',
        'https://www.googleapis.com/books/v1/volumes?q=isbn:%s' );

    my $data = $fetcher->retrieve_json( 'isbn', [9780857536020 ] );

    $page->add_section( 'Fetched Data', sub { Dumper $data} );

    my $stub = googleapi_to_internal($data);
    $page->add_section( 'book one', sub { Dumper $stub}, 0 );

    my $book_id = add_book( $db, $stub );
    $page->add_section( 'note', sub { Dumper $book_id; } );
    foreach my $auth ( @{ $stub->{authors} } ) {
        my $record = { name => $auth };
    }
    $page->view_multiple_rows(
        [ 'books.id', 'title', 'pages', 'publication_date', 'description' ],
        [], {}, 'Book List' );
    $page->view_multiple_rows( [ 'authors.id', 'name' ], [], {},
        'Author list' );
}

sub add_book ($$) {
    my ( $db, $data ) = @_;

    my $book_id;

    my $existing_book =
      $db->match_optional_single( ['books.id'], ['title = %title'],
        { title => $data->{title} } );

    if ( !$existing_book->{id} ) {

        my $book = {
            title            => $data->{title},
            publication_date => $data->{publishedDate},
            pages            => $data->{pageCount},
            description      => $data->{description}
        };

        $book_id = $db->insert_entry( 'books', $book );
    }
    else {
        $book_id = $existing_book->{id};
        return $book_id;
    }

    foreach my $identifier ( @{ $data->{IndustryIdentifiers} } ) {
        my $isbn  = $identifier->{identifier};
        my $type  = $identifier->{type};
        my $class = ( $type eq 'ISBN_!0' ) ? 1 : 2;

        $db->insert_entry( 'book_identifier',
	    {
                book            => $book_id,
                identifier_type => $class,
                identifier      => $isbn
            }
        );
    }

    foreach my $author ( @{ $data->{authors} } ) {
        my $existing_author =
          $db->match_optional_single( ['authors.id'], ['name = %name'],
            { name => $author } );

        my $ex_auth_id =
          ( exists $existing_author->{id} )
          ? $existing_author->{id}
          : $db->insert_entry( 'authors', { name => $author } );

        $db->insert_entry(
            'authorship',
            {
                book   => $book_id,
                author => $ex_auth_id
            }
        );

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
