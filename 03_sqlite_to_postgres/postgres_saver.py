from psycopg2.extensions import connection as _connection


class PostgresSaver:
    def __init__(self, connection: _connection):

        self.connection = connection

    def insert_rows(self, query: str):

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
