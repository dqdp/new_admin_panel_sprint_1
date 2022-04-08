from typing import List

from dclasses import Filmwork, Person, Genre, PersonFilmwork, GenreFilmwork
from config.sql import *

def c(field) -> str:
        if field is None:
            return ''
        return field

class QueriesMaker:

    @staticmethod
    def make_insert_query_filmwork(data: List[Filmwork]) -> str:

        inserts = ''
        for i, row in enumerate(data):
            inserts += f'''('{row.id}',
                            '{c(row.title).replace("'", "''")}',
                            '{c(row.description).replace("'", "''")}',
                            '{c(row.creation_date)}',
                            '{c(row.file_path)}',
                            '{row.rating}',
                            '{c(row.type)}',
                            '{row.created}',
                            '{row.updated}'),'''
        
        return INSERT_QUERY_TEMPLATE.format('film_work', COLUMNS_FILMWORK, inserts[:-1])


    @staticmethod
    def make_insert_query_person(data: List[Person]) -> str:

        inserts = str()
        for i, row in enumerate(data):
            inserts += f'''('{row.id}',
                            '{c(row.full_name).replace("'", "''")}',
                            '{row.created}',
                            '{row.updated}'),'''

        return INSERT_QUERY_TEMPLATE.format('person', COLUMNS_PERSON, inserts[:-1])


    @staticmethod
    def make_insert_query_genre(data: List[Genre]) -> str:

        inserts = str()
        for i, row in enumerate(data):
            inserts += f'''('{row.id}',
                            '{c(row.name).replace("'", "''")}',
                            '{c(row.description).replace("'", "''")}',
                            '{row.created}',
                            '{row.updated}'),'''

        return INSERT_QUERY_TEMPLATE.format('person', COLUMNS_GENRE, inserts[:-1])


    @staticmethod
    def make_insert_query_person_filmwork(data: List[PersonFilmwork]) -> str:

        inserts = str()
        for i, row in enumerate(data):
            inserts += f'''('{row.id}',
                            '{row.filmwork_id}',
                            '{row.person_id}',
                            '{c(row.role)}',
                            '{row.created}'),'''

        return INSERT_QUERY_TEMPLATE.format('person', COLUMNS_PERSON_FILMWORK, inserts[:-1])


    @staticmethod
    def make_insert_query_genre_filmwork(data: List[GenreFilmwork]) -> str:

        inserts = str()
        for i, row in enumerate(data):
            inserts += f'''('{row.id}',
                            '{row.genre_id}',
                            '{row.filmwork_id}',
                            '{row.created}'),'''

        return INSERT_QUERY_TEMPLATE.format('person', COLUMNS_GENRE_FILMWORK, inserts[:-1])