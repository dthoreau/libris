#! /usr/bin/perl

#use warnings;
use strict;

use SQL::Parser;
use Data::Dumper;
use List::Util qw(max);
$Data::Dumper::Sortkeys = 1;

#my $file = shift @ARGV;
#
#open FILE, '<', $file || die "kaboom: $!";
#
#my @contents = <FILE>;
#
#close FILE || die 'Howwibily';
#
my ( $begin, $commit, $rollback ) = ();

my @statements;

my $parser = SQL::Parser->new();
$parser->feature( 'valid_data_types', 'TEXT',    1 );

my @text = <STDIN>;
my $text = join '', @text;

my $sql = render($parser, $text );

print "$sql\n\n";


sub render ($) {
    my ( $parser, $st ) = @_;

    if ( $st =~ /create sequence (.*);/i ) {
        return render_sequence($1);
    }

    $parser->parse($st);

    my $tree    = $parser->structure;
    my $command = $tree->{command};

    if ( $command eq 'CREATE' ) {

        return render_create($tree);
    }

    return Dumper $tree;
}

sub lpad ($$) {
    my ( $string, $count ) = @_;

    return sprintf( "%-$count" . 's', $string );

}

sub render_create ($) {
    my ($st) = @_;

    my $table_name = shift @{ $st->{table_names} };

    my $sql = "CREATE TABLE $table_name (\n";

    my $columns = [ sort keys %{ $st->{table_defs}{columns} } ];

    my $max = max map { $_ = length $_ } @{ [@$columns] };

    my $first = 1;
    foreach my $name (sort {length $a <=> length $b} @$columns) {
        my $line = ($first) ? '' : ",\n";
        if ($first) { $first = 0; }
        my $def = $st->{table_defs}{columns}{$name};
        $name = lpad( $name, $max );

        my $type        = $def->{data_type};
        my $constraints = $def->{constraints};

        $line .= "$name $type";
        if ($constraints) {
            $line .= ' ';
            $line .= join ' ', @$constraints;
        }

        $sql .= $line;

    }
    $sql .= ");";

    return $sql;

}

sub render_sequence ($) {
    my ($text) = @_;

    return "CREATE SEQUENCE $text;";
}
