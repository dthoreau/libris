#! /usr/bin/perl

use warnings;
use strict;

use lib q{../lib/perl};

use JSON;

use DB;
use Util qw{get_hashval get_hashvals};
use Authors qw{maybe_add_author get_authors_hash};
use Subjects qw(maybe_add_subject get_subjects_hash);

use List::Util qw(uniq);
use Data::Dumper;

sub main {
    my $db = DB->new();

    my $filename = shift @ARGV;

    if ( !-e $filename ) { die "$filename not found"; }

    my $text = slurp($filename);

    my $data = decode_json($text);

    my ( $books, $authors, $subjects ) = pre_process( $data, $db );

    foreach my $book (@$books) {
        my ( $title, $authors) =
          get_hashvals( $book, [qw(title authors)] ) ;

	my $book_subjects = $book->{subject};
        my $book_id = $db->match_optional_single(
	    ['books.id'],
	    ['title = %title'],
	    { title => $title } );

	if (defined $book_id) { next;}

	$book_id = $db->insert_entry('books', {title=>$title, });

	my $s_list = collapse_ends($book_subjects) ;
	foreach my $subject (@$s_list) {
	    my $s_id = $subjects->{$subject};
	    $db->insert_entry('book_subjects',{book=>$book_id, subject=>$s_id});
	}

    }

}

sub pre_process {
    my ( $data, $db ) = @_;

    my $db_authors = get_authors_hash($db);
    my $db_subjects = get_subjects_hash($db);
    my $books;
    foreach my $key ( keys %$data ) {
        my $book   = get_hashval( $data, $key );
	push @$books, $book;
        my $author = get_hashval( $book, 'authors' );
        foreach my $writer (@$author) {
            if ( ref $writer ne 'HASH' ) { next; }
            my $name = get_hashval( $writer, 'fl' );
            $db_authors = maybe_add_author( $db, $name, $db_authors );

        }
        if ( exists $book->{subject} ) {
            my $subjects = collapse_ends( $book->{subject} );
	    foreach my $subject (@$subjects) {
		$db_subjects=maybe_add_subject($db, $subject, $db_subjects);
	    }
        }
    }

    return ($books, $db_authors, $db_subjects);
}

sub slurp($) {
    my ($fn) = @_;

    open FILE, '<', $fn || die "Error opening $fn: $!";
    my @data = <FILE>;
    close FILE || die "Error closing file: $!";

    return join '', @data;
}

sub collapse_ends ($) {
    my ($st) = @_;

    my $words = [];
    if ( ref $st eq 'ARRAY' ) {
        foreach my $item (@$st) {
            foreach my $sub_item (@$item) {
                push @$words, $sub_item;
            }
        }
    }
    elsif ( ref $st eq 'HASH' ) {
        my $vals = [];
        foreach my $key ( keys %$st ) {
            my $subset = $st->{$key};
            foreach my $blah (@$subset) {
                push @$words, $blah;
            }

        }

    }
    return [ uniq sort @$words ];

}

main();