import os
from pathlib import Path
from dotenv import load_dotenv

from dclasses import *

load_dotenv()

db_path = 'db.sqlite'

row_batch_size = 100

DATABASES = {
    'postgres': {
        'NAME': os.environ.get('PG_DB_NAME'),
        'USER': os.environ.get('PG_DB_USER'),
        'PASSWORD': os.environ.get('PG_DB_PASSWORD'),
        'HOST': os.environ.get('PG_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('PG_DB_PORT', 5432),
        'OPTIONS': {
            'options': '-c search_path=public,content'
        }
    }
}

#tables = ['film_work', 
#          'genre',
#          'genre_film_work',
#          'person',
#          'person_film_work']



tables = {'film_work'       : Filmwork, 
          'genre'           : Genre,
          'genre_film_work' : GenreFilmwork,
          'person'          : Person,
          'person_film_work': PersonFilmwork}