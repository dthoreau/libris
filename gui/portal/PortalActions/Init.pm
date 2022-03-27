package PortalActions::Init;

use warnings;
use strict;

require Exporter;
our @ISA = qw(Exporter);
our @EXPORT_OK = qw(init_libris);

use Data::Dumper;

use lib q{/home/dominic/libris/lib/perl};
use lib q{/home/dominic/libris/gui/portal};

use WebPage;
use Util qw{table_hash};

use PortalActions::ISBN qw(init_isbn);

my $A_home = 'home';

sub init_libris {
	my $page = WebPage::init();

	init_isbn($page);

	$page->add_page($A_home, 'Home', \&home);
	$page->add_page('debug', 'Debug', \&show_debug);

	return $page;
}


sub show_debug {
	my ($page) = @_;

	$page->add_section('Debug Information', sub {table_hash(\%ENV)},1);
}

sub home {
    my ($page) = @_;

    $page->add_section( 'Home', sub { return 'Build home page here' }, 0 );
    $page->add_section( 'Actual content',
        sub { return "<A HREF=?action=isbn-test>List Books</A>"; } );

    my $here = q{<pre>Some notes:
- there's one pre-defined action- isbn-test
- there's a brief schema (books, authors, and authorship to connect the two
	- both these primary table have view- and list- prefixed actions
	hard-coded to show lists
	- the list has no pager (yet)
	- I've only input 6 books into the DB

- One of my things to do is (after finishing the DB layer) is to import my ~700
title library that's exported from LibraryThing in order that we have more test
data. </pre>};

$page->add_section('Notes', sub { return $here; });


}

1;
