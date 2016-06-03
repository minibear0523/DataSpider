# encoding=UTF-8
import psycopg2
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"
USER_ID_LIMIT_PER_CLIENT = 200
USER_ID_TOTAL_COUNT = 11406044
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
        # Maintain a list for spider client.
        self.user_id_list = []
        self.user_id_count = 0

    def _commit(self):
        self.conn.commit()

    def get_user_id(self, start):
        """
        Get user_id index from user_profile with ```start``` and USER_ID_LIMIT
        And fetch more user_id from database.
        """
        # return first 200 user_id from self.user_id_list
        result = self.user_id_list[:200]
        self.user_id_list += len(result)

        # then fetch more user_id from database
        offset = USER_ID_TOTAL_COUNT - self.user_id_count
        self.cursor.execute(GET_USER_ID_FOR_SPIDER, (USER_ID_LIMIT_PER_CLIENT, offset))
        self._commit()
        return result

    def insert_data(self, data):
        """
        Insert data into database
        """
        self.cursor.execute()
        self._commit()
