from app import services, schemas, database

from app.util import deps

ds = database.DataBase()


def test_authors():
    slice = deps.QuerySlice(0, 100)

    test_author = 'Harpo J. Snot'
    new_author = schemas.AuthorCreate(name=test_author)
    author = services.add_author(ds, new_author=new_author)

    assert author.name == test_author
    retrieved = services.find_author(ds, test_author)

    assert author.id == retrieved.id
    books = services.get_author_books(ds, author.id, slice)
    assert len(books) == 0

    another_author = services.get_author(ds, slice, author.id)
    assert another_author.name == author.name
    services.delete_author(ds, author.id)
