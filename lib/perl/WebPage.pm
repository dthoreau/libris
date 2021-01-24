package WebPage;

use CGI;
use Util qw(true false);

use DB;
use Data::Dumper;

use Try::Tiny;

$| = 1;
sub init {
    my $self = { cgi => CGI->new, disposition => 'text/html', db => DB->new() };

    bless $self;

    return $self;
}

sub db { my ($self) = @_; return $self->{db}; }

sub note { my ( $self, $text ) = @_; $self->{notes} .= "$text\n---\n"; }

sub DESTROY {
    my ($self) = @_;

    print "Content-type: $self->{disposition}\n\n";

    $self->add_footer();

    print $self->{raw_content};
    if ($self->{notes}) {
	print "<hr><em>Notes:</em><br><pre>$self->{notes}</pre>\n";
    }
}

sub build_headers {
    my ($self) = @_;

    my $head = qq{
	<!-- meis libris - personal cloud based library management>
    };
}

sub fatal ($$) {
    my ($self, $text) = @_;

    $self->{raw_content} = '';
    my $message_text = "It appears something has gone wrong. <br>All we know is what we were
	told, and in this case, that is as follows:<br>
	<pre>$text</pre>
	<br><br>Hopefully, this may shed some light on this unfortunate
	situation";

    $self->add_section("Error", $message_text, true);

    die;
}

sub dispatch {
    my ($self) = @_;

    my $action = $self->get_param('action');
    $action //= 'home';

    $self->{action}= $action;

    my $code = $self->{actions}{$action}{code};

    if ($code) {
        try {
            return $code->($self);
        }
        catch {
            fatal($self, $_);
        };
    }
    else {
	fatal($self, "Non existent action '$action'");
    }
}

sub get_param {
    my ( $self, $param_name ) = @_;

    return $self->{cgi}->param($param_name);
}

sub append {
    my ( $self, $html ) = @_;

    $self->{raw_content} .= $html;
}

sub add_footer {
    my ($self) = @_;

    $self->append("<br><hr><em>&copy; 2021 Reclaimed Software</em>\n");
}

sub add_section ($$$;$) {
    my ( $self, $title, $content, $is_html ) = @_;

    my $cr = ref $content;
    if ( $cr eq 'CODE' ) {
        $content = $content->($self);
    }
    if ( not $is_html ) {
        $content = "<pre>$content</pre>";
    }
    my $text =
qq{<table border=0 style="width:100%"><TR><TD bgcolor=#aaffaa>$title</td></tr>
	<tr><td>$content</td></tr></table>};

    $self->append($text);

}

sub view_multiple_rows ($$$$$) {
    my ($self, $fields, $clauses, $params, $title) = @_;

    $self->add_section($title, sub { make_table_from_query($self, $fields,
		$clauses, $params);}, true);

}

sub make_table_from_query ($$$$) {
    my ( $self, $fields, $clauses, $params ) = @_;

    my $db   = $self->db;
    my $rows = $db->match_many( $fields, $clauses, $params );

    my $return = '<table border=1>';
    if ( scalar @$rows ) {

        $return .= '<tr>';
        foreach my $field (@$fields) {
	    $field = _last_dot($field);
	    my $dis = convert_label($field);
            $return .= "<th>$dis</th>";

        }

        $return .= "</tr>\n";
        foreach my $row (@$rows) {
            $return .= '<tr>';
            foreach my $field ( @$fields ) {
		$field = _last_dot($field);
                $return .= "<td>$row->{$field}</td>";
            }
            $return .= '</tr>';
        }
    }
    else {
        $return .= '<tr><TD><em>No rows returned</td></tr>';
    }
    $return .= '</table>';

    return $return;
}

sub convert_label($) {
    my ($s) = @_;

    $s =~ s/_/ /g;
    my $r = [];

    foreach my $w ( split /\s/, $s ) {
        push @$r, ucfirst $w;
    }
    return join(' ', @$r);
}

sub _last_dot ($) {
    my ($string) =@_;

    my $pieces = [split /\./, $string];
    my $count = scalar @$piecees;

    return $pieces->[$count-1];
}

sub add_page {
    my ( $self, $action, $title, $function ) = @_;

    $self->{actions}{$action} = { title => $title, code => $function };
}

sub make_link ($$;$) {
    my ( $self, $action, $title ) = @_;

    my $link = "?action=$action";

    $title //= $self->{actions}{$action}{title};
    $title //= $action;

    my $html = "<A HREF=$link>$title</A>";

    return $html;
}

1;
