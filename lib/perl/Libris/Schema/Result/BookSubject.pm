use utf8;
package Libris::Schema::Result::BookSubject;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::BookSubject

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<book_subjects>

=cut

__PACKAGE__->table("book_subjects");

=head1 ACCESSORS

=head2 book

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=head2 subject

  data_type: 'integer'
  is_foreign_key: 1
  is_nullable: 0

=cut

__PACKAGE__->add_columns(
  "book",
  { data_type => "integer", is_foreign_key => 1, is_nullable => 0 },
  "subject",
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

=head2 subject

Type: belongs_to

Related object: L<Libris::Schema::Result::Subject>

=cut

__PACKAGE__->belongs_to(
  "subject",
  "Libris::Schema::Result::Subject",
  { id => "subject" },
  { is_deferrable => 0, on_delete => "NO ACTION", on_update => "NO ACTION" },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:90BGeETYSHLs+vGxrW7TVw


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
