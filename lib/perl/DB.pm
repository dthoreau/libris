package DB;

use warnings;
use strict;

use DBI;

sub new {
    my $db = DBI->connect("dbi:Pg:dbname=libris",'libris','',{AutoCommit => 1});

    my $self = { dbh => $db};

    bless $self;

    return $self;
}

sub insert_entry {
    my ($self, $table, $values) = @_;

    my $db = $self->{dbh};

    my @fnames = sort keys %$values;
    my @qlist;
    my @fields;

    foreach my $field (@fnames) {
	push @qlist, '?';
	push @fields, $values->{$field};
    }
    my $sql = "INSERT INTO $table (" . join(', ', @fnames) . " ) values ( ".  join(', ', @qlist) . ' )';

    my $rv = [$sql, $values];

    my $csr = $db->prepare($sql) ;
    push @$rv,  $csr->execute(@fields);

    return $rv;





}


sub match_many ($$$$) {
    my ($self, $fields, $clauses, $params) = @_;

    my $db = $self->{dbh};

    my ($sql, $param_array) = _build_select_query($fields, $clauses, $params);

#    return [{sql=>$sql, array => @$param_array}];
    my $csr=$db->prepare($sql) || fatal $!;
    $csr->execute(@$param_array);

#    return $csr->errstr;
#    return $csr->rows;
    my $rows = [];
    while (my $row = $csr->fetchrow_hashref) {
	push @$rows, $row;
    }
    return $rows;
}

sub _build_select_query {
    my ( $fields, $clauses, $params ) = @_;

    my ($table) = split /\./, $fields->[0];

    my $param_array = [];
    my $sql = 'SELECT ' . join( ' ,', @$fields ) . " FROM $table ";

    my $cc = 0;
    foreach my $clause (@$clauses) {
	$cc ++;
	if ($clause =~ /^(.*)\s\%(\w*)\s?$/) {
	    $clause = "$1 ?";
	    push @$param_array, $params->{$2};
	}
    }

    if ($cc) { $sql = "$sql WHERE " . join ' AND ', @$clauses; }

    return ($sql, $param_array);
}

1;
