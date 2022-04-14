package Util;

use warnings;
use strict;

require Exporter;
our @ISA       = q{Exporter};
our @EXPORT_OK = qw{false true table_hash get_hashval get_hashvals};

use Data::Dumper;
use Carp;

sub true  { 1 }
sub false { 0 }

sub table_hash {
    my ( $table, $style ) = @_;
    my $text = "<table $style>";
    foreach my $key ( sort keys %$table ) {
        $text .= "<tr><td>$key</td><td>$table->{$key}</td></tr>";
    }
    return $text;
}

sub get_hashvals($$;$$) {
    my ( $hash, $keys, $allow_undef, $undef_value ) = @_;

    if (ref $hash ne 'HASH') { confess "That's not a HASH, that's a ". ref $hash;}
    $undef_value //= undef;
    my @result;
    foreach my $key (@$keys) {
        if ( !exists $hash->{$key} ) {
            confess "key  $key not present in hash " . Dumper $hash;
        }
        my $value = $hash->{$key};
        if ( ( !defined $value ) && ( !$allow_undef ) ) {
            confess "Key $key is undefined in " . Dumper $hash;
        }
        $value //= $undef_value;
        push @result, $value;
    }
    return @result;
}

sub get_hashval ($$;$$) {
    my ( $hash, $key, $allow_undef, $undef_value ) = @_;

    my @result = get_hashvals( $hash, [$key], $allow_undef, $undef_value );
    if ( exists $result[0] ) {
        return $result[0] ;
    }
    elsif ($allow_undef) {
          return $undef_value;
    }
    else {
          confess "Something";
    }
}

1;
