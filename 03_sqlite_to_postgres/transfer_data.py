import sqlite3

import psycopg2
from psycopg2.extras import DictCursor

from config.settings import DATABASES, DB_PATH, QUERY_MAKERS, TABLES
from postgres_saver import PostgresSaver
from sqlite_loader import SQLiteLoader


def transfer_data():

    with sqlite3.connect(DB_PATH) as sqlite_conn,\
         psycopg2.connect(**DATABASES['postgres'], cursor_factory=DictCursor) as pg_conn:

        postgres_saver = PostgresSaver(pg_conn)
        loader = SQLiteLoader(sqlite_conn)

        for table in TABLES:
            load_generator = loader.load_data(f'SELECT * FROM {table};', table)
            while True:
                try:
                    data = next(load_generator)
                    query = QUERY_MAKERS[table](data)
                    postgres_saver.insert_rows(query)

                except StopIteration:
                    print('Data transferred successfully!')
                    break
                except Exception as e:
                    print(f'Error during transferred table {table} : {e}')
                    raise e


if __name__ == '__main__':
    transfer_data()
