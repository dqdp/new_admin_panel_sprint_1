import sqlite3
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extensions import connection as _connection

from sqlite_loader import SQLiteLoader
from postgres_saver import PostgresSaver
from config.settings import TABLES, DB_PATH, DATABASES, QUERY_MAKERS 


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PostgresSaver(pg_conn)
    loader = SQLiteLoader(connection)
    
    for table in TABLES:
        counter = 0
        sqlite_load_generator = loader.load_data(f'SELECT * FROM {table};', table)
        while True:
            try:
                data = next(sqlite_load_generator)
                query = QUERY_MAKERS[table](data)
                print(query)
                postgres_saver.insert_rows(query)
                print(table, counter)

            except StopIteration:
                break   


if __name__ == '__main__':

    with sqlite3.connect(DB_PATH) as sqlite_conn,\
         psycopg2.connect(**DATABASES['postgres'], cursor_factory=DictCursor) as pg_conn:

        load_from_sqlite(sqlite_conn, pg_conn)

