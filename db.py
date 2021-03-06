# encoding=UTF-8
import psycopg2
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"
USER_ID_LIMIT_PER_CLIENT = 200
GET_USER_ID_FOR_SPIDER = """SELECT user_id FROM user_profile ORDER BY user_id ASC LIMIT %s OFFSET %s"""


def _format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime(DATE_FORMAT)


class FitTimeClass:
    """
    FitTime Database Class
    * GET index for spider.
    * INSERT data for new data.
    * FORMAT timestamp.
    * COMMIT operation.
    """
    def __init__(self):
        """
        Create a connection to database and get cursor for operation.
        """
        self.conn = psycopg2.connect("dbname=fittime user=MiniBear")
        self.cursor = self.conn.cursor()

    def get_user_id(self, index):
        self.cursor.execute(GET_USER_ID_FOR_SPIDER, (USER_ID_LIMIT_PER_CLIENT, index))
        data = self.cursor.fetchall()
        return map(lambda x: x[0], data)

    def _commit(self):
        self.conn.commit()

    def insert_data(self, query, data):
        """
        Insert data into database
        """
        self.cursor.execute(query, data)
        self._commit()
