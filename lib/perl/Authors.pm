package Authors;

use warnings;
use strict;

require Exporter;
our @ISA = q{Exporter};
our @EXPORT_OK = qw{get_authors_hash maybe_add_author};

use Util qw{get_hashval get_hashvals};

sub get_authors_hash {
    my ($db) = @_;

    my $return_hash = {};
    my $db_authors = $db->match_many(['authors.id', 'name'],[],{});

    foreach my $db_a (@$db_authors) {
	my ($id, $name) = get_hashvals($db_a,[qw(id name)]);
	$return_hash->{$name}=$id;
    }

    return $return_hash;
}

sub maybe_add_author ($$;$){
    my ($db, $name, $lookup) = @_;

    $lookup //= get_authors_hash($db);

    if (not exists $lookup->{$name}) {
	my $id = $db->insert_entry('authors', {name=>$name});

	$lookup->{$name} = $id;
    }

    return $lookup;
}


1;

