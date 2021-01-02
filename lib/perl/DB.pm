package DB;

use warnings;
use strict;

use MongoDB;

sub new {
    my $db = MongoDB->connect('mongodb://localhost');
    my $collection = $db->ns('test.libris');

    my $self = { namespace => $collection, dbh => $db};

    bless $self;

    return $self;
}

sub fetch_single {
    my ($self, $id) = @_;

    return $self->{namespace}->find_one({id=>$id});
}

sub insert_single {
    my ($self, $data) = @_;

    return $self->{namespace}->insert_one($data);
}

sub update_single {
    my ($self, $id, $data) = @_;

    return $self->{namespace}->update_one({id=>$id}, $data);
}



1;
