from Database import Database
import csv

class Product:
    def __init__(self):
        self.table =  'product'
        self.database = Database(host='localhost', user='root', password='Rija', database='store')

    def create(self, name, description, price, quantity, id_category):
        query = f"INSERT INTO {self.table} (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        parametre = (name, description, price, quantity, id_category)
        self.database.executeQuery(query, parametre)

    def read(self):
        query = f"SELECT * FROM {self.table}"
        return self.database.fetch(query) 
    
    def update(self, id, name, description, price, quantity, id_category):
        query = f"UPDATE {self.table} SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s"
        parametre = (name, description, price, quantity, id_category, id)
        self.database.executeQuery(query, parametre)

    def delete(self, id):
        query = f"DELETE * FROM {self.table} WHERE id=%s"
        parametre = (id,)
        self.database.executeQuery(query, parametre)

    def find(self, id):
        query = f"SELECT * FROM {self.table} WHERE id=%s"
        paramatre = (id,)
        return self.database.fetch(query, paramatre)
    
    def exportCsvFile(self):
        query = f"SELECT * FROM {self.table} INTO OUTFILE 'tableau.csv'"
        return self.database.executeQuery(query)
    
# run = Product()
# run.exportCsvFile()