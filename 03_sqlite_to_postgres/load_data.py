import sqlite3
import psycopg2

#from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
#from contextlib import contextmanager

from sqlite_loader import SQLiteLoader
from postgres_saver import PostgresSaver
from config.config import tables, db_path, DATABASES




def load_from_sqlite(connection: sqlite3.Connection):  #, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    
    # postgres_saver = PostgresSaver(pg_conn)

    loader = SQLiteLoader(connection)
    
    for table in tables:
        sqlite_load_generator = loader.load_data(f'SELECT * FROM {table};', table)
        while True:
            try:
                data = next(sqlite_load_generator)
                print(table, data[0])
                #TODO: save to postrges
            except StopIteration:
                break

    # data = sqlite_loader.load_movies()
    # postgres_saver.save_all_data(data)
    



if __name__ == '__main__':

    dsl = {'dbname': DATABASES['postrges']['NAME'],
           'user': 'app', 
           'password': '123qwe', 
           'host': '127.0.0.1', 
           'port': 5432
          }
    with sqlite3.connect(db_path) as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:

        load_from_sqlite(sqlite_conn)

