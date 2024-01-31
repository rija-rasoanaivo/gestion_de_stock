import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def disconnect(self):
        self.connection.close()

    def executeQuery(self, query, parametre = None):
        self.connect()
        self.cursor.execute(query, parametre or())
        self.connection.commit()
        self.disconnect()

    def fetch(self, query, parametre = None):
        self.connect()
        self.cursor.execute(query, parametre or())
        result = self.cursor.fetchall()
        return result