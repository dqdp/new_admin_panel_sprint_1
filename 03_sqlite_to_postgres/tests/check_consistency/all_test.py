import sqlite3
from itertools import chain

import psycopg2
from psycopg2.extras import DictCursor

from config.settings import DATABASES, SQLITE_PATH, TABLES
from main import transfer_data


def test_count_rows():
    transfer_data()
    with sqlite3.connect(SQLITE_PATH) as sqlite_conn,\
         psycopg2.connect(**DATABASES['postgres'], cursor_factory=DictCursor) as pg_conn:

        for table in TABLES:

            cursor_sqlite = sqlite_conn.cursor()
            cursor_sqlite.execute(f'SELECT * FROM {table};')
            results_sqlite = cursor_sqlite.fetchall()

            cursor_pg = pg_conn.cursor()
            cursor_pg.execute(f'SELECT * FROM content.{table};')
            results_pg = cursor_pg.fetchall()

            assert len(results_sqlite) == len(results_pg)


def test_name_tables():
    transfer_data()
    with sqlite3.connect(SQLITE_PATH) as sqlite_conn,\
         psycopg2.connect(**DATABASES['postgres'], cursor_factory=DictCursor) as pg_conn:

        cursor_sqlite = sqlite_conn.cursor()
        cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
        results_sqlite = cursor_sqlite.fetchall()
        cursor_pg = pg_conn.cursor()
        cursor_pg.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'content'""")
        results_pg = cursor_pg.fetchall()

        assert sorted(chain(*results_sqlite)) == sorted(chain(*results_pg))


def rearrange(table: str, r: list) -> tuple:
    if table == 'film_work':
        return tuple(chain(r[0:4], [r[-1]], r[4:-1]))
    if table == 'person_film_work' or table == 'genre_film_work':
        return tuple(chain([r[0]], [r[2]], [r[1]], r[3:]))
    return tuple(r)


def test_data():
    transfer_data()
    with sqlite3.connect(SQLITE_PATH) as sqlite_conn,\
         psycopg2.connect(**DATABASES['postgres'], cursor_factory=DictCursor) as pg_conn:

        for table in TABLES:

            cursor_sqlite = sqlite_conn.cursor()
            cursor_sqlite.execute(f'SELECT * FROM {table};')
            results_sqlite = cursor_sqlite.fetchall()

            cursor_pg = pg_conn.cursor()
            cursor_pg.execute(f'SELECT * FROM content.{table};')
            results_pg = cursor_pg.fetchall()

            for row_sqlite, row_pg in zip(results_sqlite, results_pg):

                row_pg = rearrange(table, row_pg)
                assert TABLES[table](*row_sqlite) == TABLES[table](*row_pg)
