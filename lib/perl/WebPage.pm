package WebPage;

use CGI;

sub init {
    my $self = { cgi => CGI->new };

    bless $self;

    return $self;
}

sub DESTROY {
    my ($self) = @_;

    print "Content-type: text/html\n\n";

    $self->add_footer();

    print $self->{raw_content};
}

sub dispatch {
    my ($self) = @_;

    my $action = $self->get_param('action');
    $action //= 'home';

    my $code = $self->{actions}{$action}{code};
    if ($code) {
        $code->($self);
    }
    else {
        $self->append("Non existent $action");
    }
}

sub get_param {
	my ($self, $param_name) = @_;

	return $self->{cgi}->param($param_name);
}

sub append {
	my ($self, $html) = @_;

	$self->{raw_content} .= $html;
}

sub add_footer {
    my ($self) = @_;

    $self->append .= '<br><hr>Nothing to see here, move along';
}

sub add_section ($$$;$) {
	my ($self, $title, $content, $is_html) = @_;

	my $text = qq{<table><border=0 width=95%'><TR><TD bgcolor=#ffddff>$title</td></tr>
	<tr><td>$content</td></tr></table};

	$self->append($text);
}

sub add_page {
	my ($self, $action, $title, $function) = @_;

	$self->{actions}{$action} = {title => $title, code => $function};
}
1;
