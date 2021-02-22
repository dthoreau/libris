package DB;

use warnings;
use strict;

use DBI;
use Util qw(true false);

use Carp qw(confess);
use Data::Dumper;

sub new {
#TODO switch autocommit off
    my $db =
      DBI->connect( "dbi:Pg:dbname=libris", 'libris', '', { AutoCommit => 1 } );

    my $self = { dbh => $db };

    bless $self;

    return $self;
}

#TODO destroy function that rolls back cursor

#TODO create transaction function (probably involving Try::Tiny

sub insert_entry {
    my ( $self, $table, $values ) = @_;

    my $db = $self->{dbh};

# TODO barf if not in transaction
    my @fnames = sort keys %$values;
    my @qlist;
    my @fields;

    foreach my $field (@fnames) {
        push @qlist,  '?';
        push @fields, $values->{$field};
    }
    my $sql =
        "INSERT INTO $table ("
      . join( ', ', @fnames )
      . " ) values ( "
      . join( ', ', @qlist ) . ' )';

    my $csr = $db->prepare($sql)     || fatal( $db->errstr );
    my $id  = $csr->execute(@fields) || fatal( $db->errstr );

# TODO close the cursor

    return $db->last_insert_id(undef, undef, $table, undef);
}

sub match_many ($$$$) {
    my ( $self, $fields, $clauses, $params ) = @_;

    my $db = $self->{dbh};

    my ( $sql, $param_array ) =
      _build_select_query( $fields, $clauses, $params );

    my $csr = $db->prepare($sql) || fatal( $db->errstr );
    $csr->execute(@$param_array) || fatal( $db->errstr );

    my $rows = [];
    while ( my $row = $csr->fetchrow_hashref ) {
        push @$rows, $row;
    }

#TODO close the cursor
    return $rows;
}

sub delete_entry {
    my ( $self, $table, $id ) = @_;
    my $db = $self->{dbh};

    my $sql = "DELETE from $table WHERE id = ?";

    my $csr = $db->prepare($sql) || fatal( $db->errstr );
    $csr->execute(  $id  ) || fatal( $db->errstr );

}


sub match_optional_single ($$$$) {
    my ( $self, $fields, $clauses, $params, $opt ) = @_;

    return $self->match_single( $fields, $clauses, $params, true );
}

# TODO this one doesn't work properly
sub match_tuple ($$$$) {
    my ( $self, $fields, $clauses, $params, $opt ) = @_;

    if ( !wantarray ) {
        fatal('Not called in array context');
    }

    my $result = $self->match_single( $fields, $clauses, $params ) ;
    my $return = $result->{id};
    return ($return);
}

sub match_single ($$$$;$) {
    my ( $self, $fields, $clauses, $params, $opt ) = @_;

    $opt //= false;

    my $rows = $self->match_many( $fields, $clauses, $params );

    my $row_count = scalar @$rows;
    if ( $row_count == 0 ) {
        confess("1 row expected, zero returned") unless $opt;
    }
    elsif ( $row_count > 1 ) {
        confess("1 row expected, $row_count returned");
    }
    return $rows->[0];
}

sub _build_select_query {
    my ( $fields, $clauses, $params ) = @_;

    $clauses = ( ref $clauses eq 'ARRAY' ) ? $clauses : [$clauses];
    $params  = ( ref $params eq 'HASH' )   ? $params  : { id => $params };

    my ($table) = split /\./, $fields->[0];

    my $param_array = [];
    my $sql         = 'SELECT ' . join( ', ', @$fields ) . " FROM $table ";

    my $cc = 0;
    foreach my $clause (@$clauses) {
        $cc++;
        if ( $clause =~ /^(.*)\s\%(\w*)\s?$/ ) {
            $clause = "$1 ?";
            push @$param_array, $params->{$2};
        }
    }

    if ($cc) { $sql = "$sql WHERE " . join ' AND ', @$clauses; }

    return ( $sql, $param_array );
}

sub fatal ($) {
    my ($message) = @_;

    $message .= "\n";

    confess $message;
}

sub fetch_table_meta($$) {
    my ($self, $table_name) = @_;



}

1;
