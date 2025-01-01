import pytest
from app import services, schemas, database

from app.util import deps

ds = database.DataBase()


@pytest.fixture(autouse=True)
def cleanup():
    yield
    retr = services.find_author(ds, 'Harpo J. Snot')
    if retr is not None:
        services.delete_author(ds, retr.id)


def test_authors():
    slice = deps.QuerySlice(0, 1000)

    authors = services.all_authors(ds, slice)

    test_author = 'Harpo J. Snot'
    new_author = schemas.AuthorCreate(name=test_author)
    author = services.add_author(ds, new_author=new_author)
    authors2 = services.all_authors(ds, slice)

    assert len(authors)+1 == len(authors2)
    assert author.name == test_author

    retrieved = services.find_author(ds, test_author)
    assert author.id == retrieved.id
    
    books = services.get_author_books(ds, author.id, slice)
    assert len(books) == 0

    another_author = services.get_author(ds, author.id, slice)
    assert another_author.name == author.name
