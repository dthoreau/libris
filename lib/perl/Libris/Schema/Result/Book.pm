use utf8;
package Libris::Schema::Result::Book;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

Libris::Schema::Result::Book

=cut

use strict;
use warnings;

use base 'DBIx::Class::Core';

=head1 TABLE: C<books>

=cut

__PACKAGE__->table("books");

=head1 ACCESSORS

=head2 id

  data_type: 'integer'
  is_auto_increment: 1
  is_nullable: 0
  sequence: 'books_seq'

=head2 ean

  data_type: 'text'
  is_nullable: 1

=head2 upc

  data_type: 'text'
  is_nullable: 1

=head2 asin

  data_type: 'text'
  is_nullable: 1

=head2 pages

  data_type: 'integer'
  is_nullable: 1

=head2 title

  data_type: 'text'
  is_nullable: 0

=head2 height

  data_type: 'text'
  is_nullable: 1

=head2 length

  data_type: 'text'
  is_nullable: 1

=head2 summary

  data_type: 'text'
  is_nullable: 1

=head2 thickness

  data_type: 'text'
  is_nullable: 1

=head2 page_count

  data_type: 'integer'
  is_nullable: 1

=head2 description

  data_type: 'text'
  is_nullable: 1

=head2 publication

  data_type: 'text'
  is_nullable: 1

=head2 publication_date

  data_type: 'text'
  is_nullable: 1

=cut

__PACKAGE__->add_columns(
  "id",
  {
    data_type         => "integer",
    is_auto_increment => 1,
    is_nullable       => 0,
    sequence          => "books_seq",
  },
  "ean",
  { data_type => "text", is_nullable => 1 },
  "upc",
  { data_type => "text", is_nullable => 1 },
  "asin",
  { data_type => "text", is_nullable => 1 },
  "pages",
  { data_type => "integer", is_nullable => 1 },
  "title",
  { data_type => "text", is_nullable => 0 },
  "height",
  { data_type => "text", is_nullable => 1 },
  "length",
  { data_type => "text", is_nullable => 1 },
  "summary",
  { data_type => "text", is_nullable => 1 },
  "thickness",
  { data_type => "text", is_nullable => 1 },
  "page_count",
  { data_type => "integer", is_nullable => 1 },
  "description",
  { data_type => "text", is_nullable => 1 },
  "publication",
  { data_type => "text", is_nullable => 1 },
  "publication_date",
  { data_type => "text", is_nullable => 1 },
);

=head1 PRIMARY KEY

=over 4

=item * L</id>

=back

=cut

__PACKAGE__->set_primary_key("id");

=head1 RELATIONS

=head2 authorships

Type: has_many

Related object: L<Libris::Schema::Result::Authorship>

=cut

__PACKAGE__->has_many(
  "authorships",
  "Libris::Schema::Result::Authorship",
  { "foreign.book" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);

=head2 book_awards

Type: has_many

Related object: L<Libris::Schema::Result::BookAward>

=cut

__PACKAGE__->has_many(
  "book_awards",
  "Libris::Schema::Result::BookAward",
  { "foreign.book" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);

=head2 book_deweys

Type: has_many

Related object: L<Libris::Schema::Result::BookDewey>

=cut

__PACKAGE__->has_many(
  "book_deweys",
  "Libris::Schema::Result::BookDewey",
  { "foreign.book" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);

=head2 book_genres

Type: has_many

Related object: L<Libris::Schema::Result::BookGenre>

=cut

__PACKAGE__->has_many(
  "book_genres",
  "Libris::Schema::Result::BookGenre",
  { "foreign.book" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);

=head2 book_series

Type: has_many

Related object: L<Libris::Schema::Result::BookSeries>

=cut

__PACKAGE__->has_many(
  "book_series",
  "Libris::Schema::Result::BookSeries",
  { "foreign.book" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);

=head2 book_subjects

Type: has_many

Related object: L<Libris::Schema::Result::BookSubject>

=cut

__PACKAGE__->has_many(
  "book_subjects",
  "Libris::Schema::Result::BookSubject",
  { "foreign.book" => "self.id" },
  { cascade_copy => 0, cascade_delete => 0 },
);


# Created by DBIx::Class::Schema::Loader v0.07049 @ 2022-06-27 13:28:22
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:pgtpat0miPR0qrnVwwGPSg


# You can replace this text with custom code or comments, and it will be preserved on regeneration
1;
