package Util;

use warnings;
use strict;

require Exporter;
our @ISA = q{Exporter};
our @EXPORT_OK = qw{false true table_hash};

sub true { 1}
sub false {0}

sub table_hash {
	my ($table, $style) = @_;
	my $text = "<table $style>";
	foreach my $key (keys %$table) {
		$text .= "<tr><td>$key</td><td>$table->{$key}</td></tr>";
	}
	return $text;
}

1;
