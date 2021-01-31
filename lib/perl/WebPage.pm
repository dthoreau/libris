package WebPage;

use strict;
use warnings;

use CGI;
use Util qw(true false);

use DB;
use Data::Dumper;

use Try::Tiny;

$| = 1;

sub init {
    my $self = { cgi => CGI->new, disposition => 'text/html', db => DB->new() };

    open( my $TMPL, '<',
        '../..//gui/portal/web/templates/base.tmpl' ) || die $!;
    my @template = <$TMPL>;
    close $TMPL || die $1;

    $self->{template} = join '', @template;

    bless $self;

    return $self;
}

sub db { my ($self) = @_; return $self->{db}; }

sub note { my ( $self, $text ) = @_; $self->{notes} .= "$text\n---\n"; }

sub DESTROY {
    my ($self) = @_;

    print "Content-type: $self->{disposition}\n\n";

    my $template = $self->{template};

    if ( $self->{notes} ) {
        $self->{raw_content} .=
          "<hr><em>Notes:</em><br><pre>$self->{notes}</pre>\n";
    }

    $template =~ s/<!-- CONTENT -->/$self->{raw_content}/e;

    print $template;
}

sub build_headers {
    my ($self) = @_;

    my $head = qq{
	<!-- meis libris - personal cloud based library management>
    };
}

sub fatal ($$) {
    my ( $self, $text ) = @_;

    $self->{raw_content} = '';
    my $message_text =
      "It appears something has gone wrong. <br>All we know is what we were
	told, and in this case, that is as follows:<br>
	<pre>$text</pre>
	<br><br>Hopefully, this may shed some light on this unfortunate
	situation";

    $self->add_section( "Error", $message_text, true );

    die;
}

sub dispatch {
    my ($self) = @_;

    my $action = $self->get_param('action');
    $action //= 'home';

    $self->{action} = $action;

    my $code = $self->{actions}{$action}{code};

    if ($code) {
        try {
            return $code->($self);
        }
        catch {
            fatal( $self, $_ );
        };
    }
    else {
        fatal( $self, "Non existent action '$action'" );
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
    my ( $self, $fields, $clauses, $params, $title ) = @_;

    $self->add_section(
        $title,
        sub {
            make_table_from_query( $self, $fields, $clauses, $params );
        },
        true
    );
}

sub hash_to_table {
    my ( $self, $hash, $fields ) = @_;

    my $return = '<table>';
    foreach my $field (@$fields) {
        $field = _last_dot($field);
        $return .= "<tr><th>$field</th><td>$hash->{$field}</td></tr>";
    }
    $return .= '</table>';

    return $return;
}

sub view_single_row {
    my ( $self, $table, $id ) = @_;

    my $db = $self->db;

    $self->add_section(
        'Single Row',
        sub {
            my $fields        = $self->{Tables}{$table}{ViewFields};
            my $canned_fields = $self->{Tables}{$table}{ViewFields};

            $fields->[0] = "$table.$fields->[0]";
            my $row = $db->match_single( $fields, 'id = %id', $id );
            return $self->hash_to_table( $row, $canned_fields );

        },
        true
    );

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
            foreach my $field (@$fields) {
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
    return join( ' ', @$r );
}

sub _last_dot ($) {
    my ($string) = @_;

    my $pieces = [ split /\./, $string ];
    my $count  = scalar @$pieces;

    return $pieces->[ $count - 1 ];
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

sub register_table ($$$) {
    my ( $self, $table_name, $details ) = @_;

    my $uc_tn = ucfirst $table_name;
    $self->{Tables}{$table_name} = $details;

    $self->add_page( "list-$table_name", "List $uc_tn",
        sub { $self->automatic_list_page($table_name); } );

    $self->add_page( "view-$table_name", "View $uc_tn",
        sub { $self->automatic_view_page($table_name) } );
}

sub automatic_list_page ($$) {
    my ( $self, $table ) = @_;

    my $fields = $self->{Tables}{$table}{ListFields};
    $fields->[0] = "$table.$fields->[0]";

    $self->view_multiple_rows( $fields, [], {}, ucfirst $table );
}

sub automatic_view_page {
    my ( $self, $table ) = @_;

    my $id = $self->{cgi}->param('id');

    $self->view_single_row( $table, $id );
    if ( exists $self->{Tables}{$table}{PostView} ) {
        my $func = $self->{Tables}{$table}{PostView};
        $func->( $self, $id );
    }
}

1;
