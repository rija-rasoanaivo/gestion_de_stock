from Database import Database

class Product:
    def __init__(self):
        self.table =  'product'
        self.database = Database(host='localhost', user='root', password='Rija', database='store')

    