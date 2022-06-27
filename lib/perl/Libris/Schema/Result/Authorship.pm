use utf8;
package Libris::Schema::Result::Authorship;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::Authorship

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<authorship>

=cut

__PACKAGE__->table("authorship");

=head1 ACCESSORS

=head2 book

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=head2 author

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=cut

__PACKAGE__->add_columns(
  "book",
  { data_type => "integer", is_foreign_key => 1, is_nullable => 0 },
  "author",
  { data_type => "integer", is_foreign_key => 1, is_nullable => 0 },
);

=head1 RELATIONS

=head2 author

Type: belongs_to

Related object: L<Libris::Schema::Result::Author>

=cut

__PACKAGE__->belongs_to(
  "author",
  "Libris::Schema::Result::Author",
  { id => "author" },
  { is_deferrable => 0, on_delete => "NO ACTION", on_update => "NO ACTION" },
);

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


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:svHWFQ06d+NcYQewGfqcHg


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
