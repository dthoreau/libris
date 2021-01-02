#! /usr/bin/perl

use warnings;
use strict;

$| = 1;

use lib q{/home/dominic/libris/gui/portal};

use PortalActions::Init qw{init_libris};

sub main {
    my $page = init_libris();

    $page->dispatch();

}

main();
