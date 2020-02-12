from database.functions_db import *
from objects.DB_CDS import DB_CDS

class DB_Product:

    def __init__(self, id):
        self.id = id
        self.existed = True
        self.name = None
        self.predicted = None
        self.source = None
        self.note = None
        self.species = None
        self.fonction = None
        self.cds = None
        self.applications = []

        self.set_properties()

    def set_properties(self):
        datas = get_product_by(id=self.id)
        if len(datas) > 0:
            if datas["delete"] == 0:
                self.name = datas["name"]
                self.predicted = True if datas["predicted"] == 1 else False
                self.source = datas["source"]
                self.note = datas["note"]
                self.species = datas["species"]
                self.fonction = datas["fonction"]
                self.cds = DB_CDS(id=datas["cds_id"])
                self.applications = get_application_for_id(self.id)
            else:
                self.existed =False
        else:
            self.existed = False
