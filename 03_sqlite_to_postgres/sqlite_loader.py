import sqlite3
from dclasses import *

tables = {'film_work'       : Filmwork, 
          'genre'           : Genre,
          'genre_film_work' : GenreFilmwork,
          'person'          : Person,
          'person_film_work': PersonFilmwork}


class SQLiteLoader:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection


    def load_data(self, query: str, table_name: str, count_records: int = 100):
        cursor = self.connection.cursor()
        cursor.execute(query)
        while True:
            data = cursor.fetchmany(count_records)
            if data:
                answer = [tables[table_name](*row) for row in data]
                yield answer
            else:
                break
