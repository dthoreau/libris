use utf8;
package Libris::Schema::Result::Award;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::Award

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<awards>

=cut

__PACKAGE__->table("awards");

=head1 ACCESSORS

=head2 id

  data_type: 'integer'
  is_auto_increment: 1
  is_nullable: 0
  sequence: 'awards_seq'

=head2 name

  data_type: 'text'
  is_nullable: 0

=cut

__PACKAGE__->add_columns(
  "id",
  {
    data_type         => "integer",
    is_auto_increment => 1,
    is_nullable       => 0,
    sequence          => "awards_seq",
  },
  "name",
  { data_type => "text", is_nullable => 0 },
);

=head1 PRIMARY KEY

=over 4

=item * L</id>

=back

=cut

__PACKAGE__->set_primary_key("id");

=head1 RELATIONS

=head2 book_awards

Type: has_many

Related object: L<Libris::Schema::Result::BookAward>

=cut

__PACKAGE__->has_many(
  "book_awards",
  "Libris::Schema::Result::BookAward",
  { "foreign.award" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:z2sHAXx/2MlHigxIFWzhwA


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
