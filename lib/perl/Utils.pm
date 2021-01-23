package Utils;

use warnings;
use strict;

use Exporter;

our @ISA       = qw(Exporter);
our @EXPORT_OK = qw(true false);

sub true  { return 1; }
sub false { return 0; }

1;
