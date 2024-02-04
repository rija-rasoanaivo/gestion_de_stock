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
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def executeQuery(self, query, parametre = None):
        self.connect()
        self.cursor.execute(query, parametre or())
        self.connection.commit()
        self.disconnect()
        # print("Query executed successfully")

    def fetch(self, query, parametre = None):
        self.connect()
        self.cursor.execute(query, parametre or())
        result = self.cursor.fetchall()
        # print("Fetch completed")
        return result
    
# if __name__ == "__main__":
#     db = Database(host="localhost", user="root", password="Rija", database="store")

#     # Test de la méthode executeQuery
#     db.executeQuery("INSERT INTO category (name) VALUES (%s)", ('valeur1',))

#     result = db.fetch("SELECT * FROM category")
#     print(result)  # Affichage des données récupérées