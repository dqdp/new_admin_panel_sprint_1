import sqlite3

from config.settings import ROWS_BATCH_SIZE, TABLES


class SQLiteLoader:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def load_data(self, query: str, table_name: str, count_records: int = ROWS_BATCH_SIZE):
        cursor = self.connection.cursor()
        cursor.execute(query)
        while True:
            data = cursor.fetchmany(count_records)
            if data:
                answer = [TABLES[table_name](*row) for row in data]
                yield answer
            else:
                break
