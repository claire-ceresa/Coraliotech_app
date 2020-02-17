from database.functions_db import *
from objects.DB_CDS import DB_CDS
from objects.DB_Organism import DB_Organism

class DB_Product:

    def __init__(self, id):
        """
        Product object, issued from the local database
        :param id: GenBank id of the product
        """
        self.id = id
        self.existed = True
        self.name = None
        self.predicted = None
        self.source = None
        self.note = None
        self.organism = None
        self.fonction = None
        self.cds = None
        self.applications = []

        self._set_properties()

    def get_attributes(self):
        dict = self.__dict__.keys()
        return list(dict)

    def _set_properties(self):
        """set all the variables with the values"""
        datas = get_product_by(id=self.id)
        if len(datas) > 0:
            if datas["is_delete"] == 0:
                self.name = datas["name"]
                self.predicted = True if datas["predicted"] == 1 else False
                self.source = datas["source"]
                self.note = datas["note"]
                self.fonction = datas["fonction"]
                self.organism = DB_Organism(datas["species"])
                self.cds = DB_CDS(id=datas["cds_id"])
                self.applications = get_application_for_id(self.id)
            else:
                self.existed = False
        else:
            self.existed = False
