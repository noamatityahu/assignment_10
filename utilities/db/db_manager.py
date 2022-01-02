from settings import DB
import mysql.connector


class DBManager:
    __connection = None
    __cursor = None

    def __init__(self):
        pass

    def commit(self, query, args=()):
        self.__connect()
        self.__execute(query, args)
        self.__connection.commit()
        affected_rows = self.__cursor.rowcount
        self.__close_connection()
        return affected_rows

    def fetch(self, query, args=()):
        query_result = False
        self.__connect()
        if self.__execute(query, args):
            query_result = self.__cursor.fetchall()
        self.__close_connection()
        return query_result

    def execute(self, query, args=()):
        self.__connect()
        query_result = self.__execute(query, args)
        self.__close_connection()
        return query_result

    def __connect(self):
        try:
            if not self.__connection or not self.__connection.is_connected():
                self.__connection = mysql.connector.connect(**DB)
                self.__cursor = self.__connection.cursor(named_tuple=True)
        except mysql.connector.Error as error:
            print("Failed Connection With The Error {}".format(error))

    def __execute(self, query, args=()):
        if query:
            try:
                self.__cursor.execute(query, args)
                return True
            except mysql.connector.Error as error:
                print("Failed Query With The Error {}".format(error))
        return False

    def __close_connection(self):
        try:
            if self.__connection.is_connected():
                self.__connection.close()
                self.__cursor.close()
        except mysql.connector.Error as error:
            print("Failed By Closing The Connection With The Error {}".format(error))


dbManager = DBManager()
