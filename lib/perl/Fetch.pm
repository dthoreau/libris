package Fetch;

use warnings;
use strict;

use LWP::Simple;
use Carp;
use JSON;

sub new {

    my $self = {};

    bless $self;

    return $self;
}

sub store_url {
    my ($self, $key, $url) = @_;

    $self->{URLs}{$key} = $url;
}

sub retrieve_json($$$) {
    my ($self, $key, $params) = @_;

    my $json = $self->retrieve($key, $params);

    return decode_json($json);

}

sub retrieve ($$$) {
    my ($self, $key, $params) = @_;

    my $base_url = $self->{URLs}{$key};

    my $formatted_url = sprintf($base_url, @$params);


    my $content = get $formatted_url;


    return $content;




}

1;
