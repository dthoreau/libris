#! /usr/bin/perl

use warnings;
use strict;

$| = 1;

use Data::Dumper;
use XML::Simple;

use lib q{/home/dominic/libris/lib/perl};

use DB;

sub main {
    my $db = DB->new();

    my $dbh = $db->{dbh};

# Get table list
    my $sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'";

    my $tables = _rows_to_columns(_fetch_sql($dbh, $sql), 'table_name');

    my $schema = {};

# Get fields in tables
    foreach my $table (@$tables) {
        $sql = "select column_name, data_type from information_schema.columns
	    where table_schema = 'public' and table_name = '$table'";
        my $rows = _fetch_sql( $dbh, $sql );
        foreach my $row (@$rows) {
            $schema->{$table}{ $row->{column_name} } =
              { type => $row->{data_type} };
        }
    }

# TODO Get constraints on tables
    $sql = "select kcu.table_schema,
       kcu.table_name,
       tco.constraint_name,
       tco.constraint_type,
       kcu.ordinal_position as position,
       kcu.column_name as key_column,
ccu.table_schema AS foreign_table_schema,
     ccu.table_name AS foreign_table_name,
     ccu.column_name AS foreign_column_name

from information_schema.table_constraints tco
join information_schema.key_column_usage kcu
     on kcu.constraint_name = tco.constraint_name
     and kcu.constraint_schema = tco.constraint_schema
     and kcu.constraint_name = tco.constraint_name
     join information_schema.constraint_column_usage ccu on ccu.constraint_name
     = tco.constraint_name
--where tco.constraint_type in ('FOREIGN KEY',  'PRIMARY KEY')
order by kcu.table_schema,
         kcu.table_name,
         position";

    my $constraints = _fetch_sql($dbh, $sql);

    foreach my $cons (@$constraints) {
	my ($type, $table, $key_column) = get_hashvals($cons,
		[qw(constraint_type table_name key_column)]);
	if ($type eq 'PRIMARY KEY') {
	    $schema->{$table}{$key_column}{primary_key} = 1;
	} elsif ($type eq 'FOREIGN KEY') {
	    my ($ftable, $fcolumn) = get_hashvals($cons, [qw(foreign_table_name foreign_column_name)]);
	    $schema->{$table}{$key_column}{foreign_key} = {table=>$ftable,
		column=>$fcolumn};
	}
	elsif ($type eq 'UNIQUE') {
	    $schema->{$table}{$key_column}{unique} = 1;
	}
	else {print Dumper $cons;}

    }

# TODO look for not null
    print XMLout($schema);
}

sub _fetch_sql($$) {
    my ($dbh, $sql) = @_;

    my $csr = $dbh->prepare($sql);
    $csr->execute();

    my $rows = [];
    while (my $row = $csr->fetchrow_hashref ) {
	push @$rows, $row;
    }
#TODO close the cursor

    return $rows;
}

sub _rows_to_columns ($$) {
    my ( $rows, $key ) = @_;

    my $return;
    foreach my $row (@$rows) { push @$return, $row->{$key}; }

    return $return;
}

sub get_hashvals($$;$$) {
    my ( $hash, $keys, $allow_undef, $undef_value ) = @_;

    $undef_value //= undef;
    my @result;
    foreach my $key (@$keys) {
        if ( !exists $hash->{$key} ) {
            die "key  $key not present in hash " . Dumper $hash;
        }
        my $value = $hash->{$key};
        if ( ( !defined $value ) && ( !$allow_undef ) ) {
            die "Key $key is undefined in " . Dumper $hash;
        }
        $value //= $undef_value;
        push @result, $value;
    }
    return @result;
}







main();
