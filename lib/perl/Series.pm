package Seriers;

use warnings;
use strict;

require Exporter;
our @ISA = q{Exporter};
our @EXPORT_OK = qw{get_series_hash maybe_add_series};

use Util qw{get_hashval get_hashvals};

sub get_series_hash {
    my ($db) = @_;

    my $return_hash = {};
    my $db_series = $db->match_many(['series.id', 'name'],[],{});

    foreach my $db_a (@$db_series) {
	my ($id, $name) = get_hashvals($db_a,[qw(id name)]);
	$return_hash->{$name}=$id;
    }

    return $return_hash;
}

sub maybe_add_series ($$;$){
    my ($db, $name, $lookup) = @_;

    $lookup //= get_series_hash($db);

    if (not exists $lookup->{$name}) {
	my $id = $db->insert_entry('series', {name=>$name});

	$lookup->{$name} = $id;
    }

    return $lookup;
}


1;

