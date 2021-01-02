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

my $A_home = 'home';

sub init_libris {
	my $page = WebPage::init();

	$page->add_page($A_home, 'Home', \&home);
	return $page;
}


sub show_debug {
	my ($page) = @_;

	$page->add_section('Debug Information', sub {return Dumper %ENV;});
}

sub home {
	my ($page) = @_;
	$page->add_section('Home', sub { return 'Build home page here'});
}

1;
