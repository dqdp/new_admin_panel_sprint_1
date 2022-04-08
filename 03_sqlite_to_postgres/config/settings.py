import os
from dotenv import load_dotenv

from dclasses import Filmwork, Person, Genre, PersonFilmwork, GenreFilmwork
from queries_maker import QueriesMaker as QM

load_dotenv()

DB_PATH = 'db.sqlite'

ROWS_BATCH_SIZE = 100

DATABASES = {
    'postgres': {
        'dbname': os.environ.get('PG_DB_NAME'),
        'user': os.environ.get('PG_DB_USER'),
        'password': os.environ.get('PG_DB_PASSWORD'),
        'host': os.environ.get('PG_DB_HOST', '127.0.0.1'),
        'port': os.environ.get('PG_DB_PORT', 5432),
    }
}

QUERY_MAKERS = {
    'film_work'       : QM.make_insert_query_filmwork, 
    'genre'           : QM.make_insert_query_genre,
    'genre_film_work' : QM.make_insert_query_genre_filmwork,
    'person'          : QM.make_insert_query_person,
    'person_film_work': QM.make_insert_query_person_filmwork
    }


TABLES = {
    'film_work'       : Filmwork, 
    'genre'           : Genre,
    'genre_film_work' : GenreFilmwork,
    'person'          : Person,
    'person_film_work': PersonFilmwork
    }
