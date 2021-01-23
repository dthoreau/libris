package PortalActions::ISBN;

use warnings;
use strict;

use Exporter;

our @ISA = qw(Exporter);
our @EXPORT_OK = qw(init_isbn);

use JSON;
use Data::Dumper;

my $A_isbn_test = 'isbn-test';

sub init_isbn {
    my ($page) = @_;

    $page->add_page( $A_isbn_test, 'ISBN Test', \&isbn_test );
}

sub isbn_test {
    my ($page) = @_;

    my $db   = $page->db;
    my $stub = googleapi_to_internal( fake_data() );
    $page->add_section( 'book one', sub { Dumper $stub}, 0 );

    foreach my $auth ( @{ $stub->{authors} } ) {
        my $record = { name => $auth };

#        $page->add_section( 'insert',
#            sub { Dumper $db->insert_entry( 'authors', $record ) } );
    }
    $page->view_multiple_rows(['authors.id', 'name'],['id > %max'],{max => 10}, 'Author list');
    $page->view_multiple_rows(['authors.id', 'name'],[],{}, 'Author list');


}

sub googleapi_to_internal {
    my ($input) = @_;

    my $item = $input->{items}[0]{volumeInfo};
    my $return = {};

    my $keep_fields = [qw{printType publishedDate pageCount maturityRating
	language title categories}];

    foreach my $key ( @$keep_fields) {
        $return->{$key} = $item->{$key};
    }

    $return->{authors} = $item->{authors} ;

    return $return;

}

sub fake_data {
    my $json = q{{
        "kind"       : "books#volumes",
        "totalItems" : 1,
        "items" : [ {
                "kind" : "books#volume",
                "id"   : "ymiqnAEACAAJ",
                "etag" : "4+kjcXdzwcU",
                "selfLink"
                : "https://www.googleapis.com/books/v1/volumes/ymiqnAEACAAJ",
                "volumeInfo"
                : {
                    "title" : "Agile Web Development with Rails 4",
                    "authors"
                    : [
                        "Sam Ruby", "David Thomas", "David Heinemeier Hansson"
                    ],
                    "publishedDate" : "2013",
                    "description"
                    : "Provides information on creating Web-based applications with Rails 4 and Ruby 2, covering such topics as HTTP authentication, validation and unit testing, cart creation, Ajax, caching, migrations, and plugins.",
                    "industryIdentifiers"
                    : [
                        { "type" : "ISBN_10", "identifier" : "1937785564" },
                        { "type" : "ISBN_13", "identifier" : "9781937785567" }
                    ],
                    "readingModes" : { "text" : false, "image" : false },
                    "pageCount"        : 434,
                    "printType"        : "BOOK",
                    "categories"       : ["Computers"],
                    "averageRating"    : 4,
                    "ratingsCount"     : 8,
                    "maturityRating"   : "NOT_MATURE",
                    "allowAnonLogging" : false,
                    "contentVersion"   : "preview-1.0.0",
                    "imageLinks"
                    : {
                          "smallThumbnail"
                        : "http://books.google.com/books/content?id=ymiqnAEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                        "thumbnail"
                        : "http://books.google.com/books/content?id=ymiqnAEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
                    },
                    "language" : "en",
                    "previewLink"
                    : "http://books.google.co.uk/books?id=ymiqnAEACAAJ&dq=isbn:9781937785567&hl=&cd=1&source=gbs_api",
                    "infoLink"
                    : "http://books.google.co.uk/books?id=ymiqnAEACAAJ&dq=isbn:9781937785567&hl=&source=gbs_api",
                    "canonicalVolumeLink"
                    : "https://books.google.com/books/about/Agile_Web_Development_with_Rails_4.html?hl=&id=ymiqnAEACAAJ"
                },
                "saleInfo"
                : {
                    "country"     : "GB",
                    "saleability" : "NOT_FOR_SALE",
                    "isEbook"     : false
                },
                "accessInfo"
                : {
                    "country"                : "GB",
                    "viewability"            : "NO_PAGES",
                    "embeddable"             : false,
                    "publicDomain"           : false,
                    "textToSpeechPermission" : "ALLOWED",
                    "epub"                   : { "isAvailable" : false },
                    "pdf"                    : { "isAvailable" : false },
                    "webReaderLink"
                    : "http://play.google.com/books/reader?id=ymiqnAEACAAJ&hl=&printsec=frontcover&source=gbs_api",
                    "accessViewStatus" : "NONE",
                    "quoteSharingAllowed" : false
                },
                "searchInfo"
                : {
                      "textSnippet"
                    : "Provides information on creating Web-based applications with Rails 4 and Ruby 2, covering such topics as HTTP authentication, validation and unit testing, cart creation, Ajax, caching, migrations, and plugins."
                }
            }
        ]
    }
    };
    my $data = decode_json($json);

    return $data;
}


1
