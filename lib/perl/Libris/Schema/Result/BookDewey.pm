use utf8;
package Libris::Schema::Result::BookDewey;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::BookDewey

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<book_dewey>

=cut

__PACKAGE__->table("book_dewey");

=head1 ACCESSORS

=head2 book

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=head2 keyword

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=cut

__PACKAGE__->add_columns(
  "book",
  { data_type => "integer", is_foreign_key => 1, is_nullable => 0 },
  "keyword",
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

=head2 keyword

Type: belongs_to

Related object: L<Libris::Schema::Result::DeweyKeyword>

=cut

__PACKAGE__->belongs_to(
  "keyword",
  "Libris::Schema::Result::DeweyKeyword",
  { id => "keyword" },
  { is_deferrable => 0, on_delete => "NO ACTION", on_update => "NO ACTION" },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:JOqS9URrM4iVVbXZy6ddrg


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
