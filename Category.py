from Database import Database

class Category:
    def __init__(self):
        self.table = 'category'
        self.database = Database(host='localhost', user='root', password='Rija', database='store')

    def create(self, name):
        query = f"INSERT INTO {self.table} (name) VALUES (%s)"
        parametre = (name,)
        self.database.executeQuery(query, parametre)

    def read(self):
        query = f"SELECT * FROM {self.table}"
        return self.database.fetch(query)
    
    def update(self, id, name):
        query = f"UPDATE {self.table} SET name=%s WHERE id=%s"
        parametre = (name, id)
        self.database.executeQuery(query, parametre)

    def delete(self, id):
        query = f"DELETE FROM {self.table} WHERE id=%s"
        parametre = (id,)
        self.database.executeQuery(query, parametre)

    