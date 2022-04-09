from typing import Any, List

from config.sql import (
    COLUMNS_FILMWORK,
    COLUMNS_GENRE,
    COLUMNS_GENRE_FILMWORK,
    COLUMNS_PERSON,
    COLUMNS_PERSON_FILMWORK,
    INSERT_TEMPLATE,
)
from dclasses import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


def prepare(field: Any) -> str:
    if field is None:
        return 'NULL'
    if type(field) == str:
        field = field.replace("'", "''")
    return f"'{field}'"


class QueriesMaker:

    @staticmethod
    def make_insert_query_filmwork(data: List[Filmwork]) -> str:
        inserts = str()
        for i, row in enumerate(data):
            inserts += f'({prepare(row.id)},'\
                       f'{prepare(row.title)},'\
                       f'{prepare(row.description)},'\
                       f'{prepare(row.creation_date)},'\
                       f'{prepare(row.file_path)},'\
                       f'{prepare(row.rating)},'\
                       f'{prepare(row.type)},'\
                       f'{prepare(row.created)},'\
                       f'{prepare(row.updated)}),'

        return INSERT_TEMPLATE.format('film_work', COLUMNS_FILMWORK, inserts[:-1])

    @staticmethod
    def make_insert_query_person(data: List[Person]) -> str:
        inserts = str()
        for i, row in enumerate(data):
            inserts += f'({prepare(row.id)},'\
                       f'{prepare(row.full_name)},'\
                       f'{prepare(row.created)},'\
                       f'{prepare(row.updated)}),'

        return INSERT_TEMPLATE.format('person', COLUMNS_PERSON, inserts[:-1])

    @staticmethod
    def make_insert_query_genre(data: List[Genre]) -> str:
        inserts = str()
        for i, row in enumerate(data):
            inserts += f'({prepare(row.id)},'\
                       f'{prepare(row.name)},'\
                       f'{prepare(row.description)},'\
                       f'{prepare(row.created)},'\
                       f'{prepare(row.updated)}),'

        return INSERT_TEMPLATE.format('genre', COLUMNS_GENRE, inserts[:-1])

    @staticmethod
    def make_insert_query_person_filmwork(data: List[PersonFilmwork]) -> str:
        inserts = str()
        for i, row in enumerate(data):
            inserts += f'({prepare(row.id)},'\
                       f'{prepare(row.person_id)},'\
                       f'{prepare(row.filmwork_id)},'\
                       f'{prepare(row.role)},'\
                       f'{prepare(row.created)}),'

        return INSERT_TEMPLATE.format('person_film_work', COLUMNS_PERSON_FILMWORK, inserts[:-1])

    @staticmethod
    def make_insert_query_genre_filmwork(data: List[GenreFilmwork]) -> str:
        inserts = str()
        for i, row in enumerate(data):
            inserts += f'({prepare(row.id)},'\
                       f'{prepare(row.genre_id)},'\
                       f'{prepare(row.filmwork_id)},'\
                       f'{prepare(row.created)}),'

        return INSERT_TEMPLATE.format('genre_film_work', COLUMNS_GENRE_FILMWORK, inserts[:-1])
