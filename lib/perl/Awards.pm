package Awards;

use warnings;
use strict;

require Exporter;
our @ISA = q{Exporter};
our @EXPORT_OK = qw{get_awards_hash maybe_add_award};

use Util qw{get_hashval get_hashvals};

sub get_awards_hash {
    my ($db) = @_;

    my $return_hash = {};
    my $db_awards = $db->match_many(['awards.id', 'name'],[],{});

    foreach my $db_a (@$db_awards) {
	my ($id, $name) = get_hashvals($db_a,[qw(id name)]);
	$return_hash->{$name}=$id;
    }

    return $return_hash;
}

sub maybe_add_award ($$;$){
    my ($db, $name, $lookup) = @_;

    $lookup //= get_awards_hash($db);

    if (not exists $lookup->{$name}) {
	my $id = $db->insert_entry('awards', {name=>$name});

	$lookup->{$name} = $id;
    }

    return $lookup;
}


1;
1;

