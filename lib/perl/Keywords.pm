package Keywords;

use warnings;
use strict;

require Exporter;
our @ISA = q{Exporter};
our @EXPORT_OK = qw{get_keywords_hash maybe_add_keyword};

use Util qw{get_hashval get_hashvals};

sub get_keywords_hash {
    my ($db) = @_;

    my $return_hash = {};
    my $db_keywords = $db->match_many(['keywords.id', 'name'],[],{});

    foreach my $db_a (@$db_keywords) {
	my ($id, $name) = get_hashvals($db_a,[qw(id name)]);
	$return_hash->{$name}=$id;
    }

    return $return_hash;
}

sub maybe_add_author ($$;$){
    my ($db, $name, $lookup) = @_;

    $lookup //= get_keywords_hash($db);

    if (not exists $lookup->{$name}) {
	my $id = $db->insert_entry('keywords', {name=>$name});

	$lookup->{$name} = $id;
    }

    return $lookup;
}


1;

