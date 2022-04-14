package Subjects;

use warnings;
use strict;

require Exporter;
our @ISA = q{Exporter};
our @EXPORT_OK = qw{get_subjects_hash maybe_add_subject};

use Util qw(get_hashval get_hashvals);

sub get_subjects_hash ($) {
    my ($db) = @_;

    my $return_hash = {};
    my $db_subjects = $db->match_many( [ 'subjects.id', 'name' ], [], {} );

    foreach my $db_s (@$db_subjects) {
        my ( $id, $name ) = get_hashvals( $db_s, [qw(id name)] );
        $return_hash->{$name} = $id;
    }
    return $return_hash;
}

sub maybe_add_subject ($$;$) {
    my ($db, $subject, $lookup) = @_;

    $lookup //=get_subjects_hash($db);

    if (not exists $lookup->{$subject}) {
	my $id = $db->insert_entry('subjects', {name=>$subject});

	$lookup->{$subject} = $id;
    }
    return $lookup;
}


1;
