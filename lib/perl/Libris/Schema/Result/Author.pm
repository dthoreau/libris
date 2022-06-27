use utf8;
package Libris::Schema::Result::Author;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::Author

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<authors>

=cut

__PACKAGE__->table("authors");

=head1 ACCESSORS

=head2 id

  data_type: 'integer'
  is_auto_increment: 1
  is_nullable: 0
  sequence: 'authors_seq'

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
    sequence          => "authors_seq",
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

=head1 UNIQUE CONSTRAINTS

=head2 C<authors_name_key>

=over 4

=item * L</name>

=back

=cut

__PACKAGE__->add_unique_constraint("authors_name_key", ["name"]);

=head1 RELATIONS

=head2 authorships

Type: has_many

Related object: L<Libris::Schema::Result::Authorship>

=cut

__PACKAGE__->has_many(
  "authorships",
  "Libris::Schema::Result::Authorship",
  { "foreign.author" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:46TYH0eOzUW0c2GTn4dEHQ


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
