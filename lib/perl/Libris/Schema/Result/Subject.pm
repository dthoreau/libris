use utf8;
package Libris::Schema::Result::Subject;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::Subject

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<subjects>

=cut

__PACKAGE__->table("subjects");

=head1 ACCESSORS

=head2 id

  data_type: 'integer'
  is_auto_increment: 1
  is_nullable: 0
  sequence: 'subject_seq'

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
    sequence          => "subject_seq",
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

=head2 book_subjects

Type: has_many

Related object: L<Libris::Schema::Result::BookSubject>

=cut

__PACKAGE__->has_many(
  "book_subjects",
  "Libris::Schema::Result::BookSubject",
  { "foreign.subject" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:gzZC+ZBiEWjomksubDb4pQ


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
