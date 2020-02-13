from database.functions_db import *


class DB_Search:

    def __init__(self, terms):
        self.terms = terms
        self.query = self.create_query()

    def create_query(self):
        variables_selected = ["P.id", "P.nom", "P.espece", "P.source", "P.predicted"]
        query_select = "SELECT " + " , ".join(variables_selected)

        if self.terms["organism"]["checked"] and self.terms["name"]["checked"]:
            query_from = " FROM Produit P JOIN Organisme O ON P.espece = O.espece "
            query_where = " WHERE O." + self.terms["organism"]["variable"] + " = \"" + self.terms["organism"]["value"] + "\"" \
                                + " AND " + self.terms["name"]["variable"] + " LIKE \"%" + self.terms["name"]["value"] + "%\""

        elif self.terms["organism"]["checked"] and not self.terms["name"]["checked"]:
            query_from = " FROM Produit P JOIN Organisme O ON P.espece = O.espece "
            query_where = " WHERE O." + self.terms["organism"]["variable"] + " = \"" + self.terms["organism"]["value"] + "\""

        elif self.terms["name"]["checked"] and not self.terms["organism"]["checked"]:
            query_from = " FROM Produit P"
            query_where = " WHERE " + self.terms["name"]["variable"] + " LIKE \"%" + self.terms["name"]["value"] + "%\""

        query = query_select + query_from + query_where + " AND P.is_delete = 0"
        return query