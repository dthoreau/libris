#! /usr/bin/perl

use warnings;
use strict;

use lib q{../lib/perl};

use JSON;

###### A stub script that show how the base DB works. Also a test of some of the
# tooling

use DB;
use Util qw{get_hashval get_hashvals};
use Authors qw{maybe_add_author get_authors_hash};
use Subjects qw(maybe_add_subject get_subjects_hash);

use List::Util qw(uniq);
use Data::Dumper;

sub main {
    my $db = DB->new();

    my $rows = $db->match_many(['book_subjects.subject', 'subject.name'],
	    ['book = %id',], {id=>11});

    print Dumper $rows;
}

main();
