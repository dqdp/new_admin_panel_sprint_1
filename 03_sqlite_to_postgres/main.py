import sqlite3
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import DictCursor

from config.logger_settings import logger
from config.settings import DATABASES, QUERY_MAKERS, SQLITE_PATH, TABLES
from postgres_saver import PostgresSaver
from sqlite_loader import SQLiteLoader


@contextmanager
def open_sqlite():
    conn = sqlite3.connect(SQLITE_PATH)
    try:
        logger.info("Creating connection to sqlite db")
        yield conn
    finally:
        logger.info("Closing connection to sqlite db")
        conn.close()


@contextmanager
def open_postgres():
    conn = psycopg2.connect(**DATABASES['postgres'], cursor_factory=DictCursor)
    try:
        logger.info("Creating connection to postgres db")
        yield conn
    finally:
        logger.info("Closing connection to postgres db")
        conn.close()


def transfer_data():
    with open_sqlite() as sqlite_conn,\
         open_postgres() as pg_conn:

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
                    logger.info(f'Data from table {table} transferred successfully')
                    break
                except Exception as e:
                    logger.error(f'Error during transferred table {table} : {e}')
                    print()
                    raise e


if __name__ == '__main__':
    transfer_data()
