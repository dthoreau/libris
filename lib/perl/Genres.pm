package Genres;

use warnings;
use strict;

require Exporter;
our @ISA       = q{Exporter};
our @EXPORT_OK = qw(get_genres_hash maybe_add_genre);

use Util qw(get_hashvals);

sub get_genres_hash {
    my ($db) = @_;

    my $return_hash = {};
    my $db_genres   = $db->match_many( [ 'genres.id', 'name' ], [], {} );

    foreach my $dbg (@$db_genres) {
        my ( $id, $name ) = get_hashvals( $dbg, [ qw(id name) ]);
        $return_hash->{$name} = $id;
    }

    return $return_hash;
}

sub maybe_add_genre($$;$) {
    my ( $db, $name, $lookup ) = @_;

    $lookup //= get_genres_hash($db);

    if ( not exists $lookup->{$name} ) {
        my $id = $db->insert_entry( 'genres', { name => $name } );

        $lookup->{$name} = $id;
    }

    return $lookup;
}

1;
