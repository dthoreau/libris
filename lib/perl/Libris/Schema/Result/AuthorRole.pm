use utf8;
package Libris::Schema::Result::AuthorRole;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::AuthorRole

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<author_roles>

=cut

__PACKAGE__->table("author_roles");

=head1 ACCESSORS

=head2 id

  data_type: 'text'
  is_auto_increment: 1
  is_nullable: 0
  sequence: 'author_role_seq'

=head2 name

  data_type: 'text'
  is_nullable: 0

=cut

__PACKAGE__->add_columns(
  "id",
  {
    data_type         => "text",
    is_auto_increment => 1,
    is_nullable       => 0,
    sequence          => "author_role_seq",
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


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:vNsxQhWUHXWL40Y7HMZFFg


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
