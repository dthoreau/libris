use utf8;
package Libris::Schema::Result::BookSeries;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::BookSeries

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<book_series>

=cut

__PACKAGE__->table("book_series");

=head1 ACCESSORS

=head2 book

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=head2 series

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=cut

__PACKAGE__->add_columns(
  "book",
  { data_type => "integer", is_foreign_key => 1, is_nullable => 0 },
  "series",
  { data_type => "integer", is_foreign_key => 1, is_nullable => 0 },
);

=head1 RELATIONS

=head2 book

Type: belongs_to

Related object: L<Libris::Schema::Result::Book>

=cut

__PACKAGE__->belongs_to(
  "book",
  "Libris::Schema::Result::Book",
  { id => "book" },
  { is_deferrable => 0, on_delete => "NO ACTION", on_update => "NO ACTION" },
);

=head2 series

Type: belongs_to

Related object: L<Libris::Schema::Result::Series>

=cut

__PACKAGE__->belongs_to(
  "series",
  "Libris::Schema::Result::Series",
  { id => "series" },
  { is_deferrable => 0, on_delete => "NO ACTION", on_update => "NO ACTION" },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:x+jHuSm4UK/B77N8d0voOA


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
