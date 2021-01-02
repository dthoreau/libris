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

my $A_home = 'home';

sub init_libris {
	my $page = WebPage::init();

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

	$page->add_section('Home', sub { return 'Build home page here'}, 1);
}

1;
