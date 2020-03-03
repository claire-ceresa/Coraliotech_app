from database.functions_db import *
from objects.DB_Product import DB_Product


class DB_Search:

    def __init__(self, terms):
        """
        Search object, on the local database
        :param terms: a dictionnary
                {'organism': {'checked':bool, 'variable':'string, 'value':string},
                 'name':{'checked':bool, 'variable':'nom', 'value':string}}
        """
        self.terms = terms
        self.query = self.create_query()
        self.results = self.get_results()

    def create_query(self):
        """
        Create the MySQL query with the terms
        :return: MySQL query
        """
        query_select = "SELECT P.id"

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

    def get_results(self):
        """
        Get the result of the MySQL query
        :return list of the results
        """
        id_results = execute_query(self.query)
        results = []
        for id in id_results:
            product = DB_Product(id=id[0])
            results.append(product)
        return results