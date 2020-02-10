from database.functions_db import *

class DB_Product:

    def __init__(self, id):
        self.id = id
        self.name = None
        self.predicted = None
        self.source = None
        self.note = None
        self.species = None
        self.id_cds = None
        self.fonction = None

        self.set_properties()

    def set_properties(self):
        datas = get_product_by(id=self.id)
        print(datas)
        ## TODO : a debugger a partir de la
        if datas["delete"] == 0:
            self.name = self.datas["name"]
            self.predicted = True if self.datas["predicted"] == 1 else False
            self.source = self.datas["source"]
            self.note = self.datas["note"]
            self.species = self.datas["species"]
            self.id_cds = self.datas["id_cds"]
            self.fonction = self.datas["fonction"]