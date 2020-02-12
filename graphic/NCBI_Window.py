from PyQt5.QtWidgets import *
from graphic.ncbi_view import *
from database.functions_db import *
from objects.NCBI_Search import NCBI_Search
from objects.NCBI_Product import NCBI_Product
from graphic.graphics_functions import *


class NCBI_Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(NCBI_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telecharger")

    def button_write_clicked(self):
        """when button write is clicked, write the good request"""
        if self.organism_written():
            terms = self.get_request_terms()
            request = self.create_request(terms)
            self.edit_request.setEnabled(True)
            self.button_go.setEnabled(True)
            self.edit_id.setEnabled(False)
            self.edit_request.setText(request)

    def button_go_pressed(self):
        """clean the previous messages"""
        self.label_messages.setText("")

    def button_go_clicked(self):
        """when button go is clicked, save on the DB the result of the request on NCBI"""
        if self.edit_request.isEnabled():
            request = self.edit_request.text()
        elif self.edit_id.isEnabled():
            request = self.edit_id.text() + "[Accession]"
        else:
            create_messageBox(title="Attention !", text="Il y a un problème !")

        search = NCBI_Search(request)
        list_id = search.get_list_ids()

        nb_product_saved = 0
        products_not_saved = []

        if len(list_id) > 0:
            for id in list_id:
                product = NCBI_Product(id)
                saved = product.save_on_database()
                if self.check_exceptions(product) and saved["commited"]:
                    nb_product_saved = nb_product_saved + 1
                else:
                    products_not_saved.append({'id':product.id, 'error':saved["error"]})

        message = str(nb_product_saved) + " resultat enregistre dans la base de donnees"
        if len(products_not_saved) > 0:
            message = message + "\n" + str(len(products_not_saved)) + " non enregistres : \n"
            for product in products_not_saved:
                message = message + " - " + product["id"] + " : " + product["error"] + "\n"

        self.label_messages.setText(message)
        self.button_go.setEnabled(False)
        self.edit_request.setEnabled(False)
        self.edit_id.setEnabled(True)

    def check_exceptions(self, protein):
        if protein.molecular_weight is None:
            return False
        if protein.name is None:
            return False
        return True

    def organism_written(self):
        if len(self.edit_org.text()) == 0:
            create_messageBox(title="Attention", text="Remplir un organisme !")
            return False
        return True

    def get_request_terms(self):
        terms = dict()
        terms["organism"] = self.edit_org.text()
        keys = self.edit_keys.text()
        in_terms = self.edit_in.text()
        out_terms = self.edit_out.text()

        if len(keys) > 0:
            terms["keys"] = keys.split(" ")
        else:
            terms["keys"] = []

        if len(in_terms) > 0:
            terms["in_terms"] = in_terms.split(" ")
        else:
            terms["in_terms"] = []

        if len(out_terms) > 0:
            terms["out_terms"] = out_terms.split(" ")
        else:
            terms["out_terms"] = []

        return terms

    def create_request(self, terms):
        beginning = terms["organism"]
        and_terms = ""
        not_terms = ""

        for key in terms["keys"]:
            and_terms = and_terms + " AND " + key
        for in_term in terms["in_terms"]:
            and_terms = and_terms + " AND " + in_term + " [Title]"
        for out_term in terms["out_terms"]:
            not_terms = not_terms + " NOT " + out_term + " [Title]"

        request = beginning + and_terms + not_terms
        return request



    # def save_protein(self, protein):
    #     self.save_cds(protein)
    #     self.save_organism(protein)
    #     product = self.save_product(protein)
    #     return product
    #
    # def save_cds(self, protein):
    #     datas_cds = {}
    #     datas_cds["id"] = "\"cds_" + protein.id + "\""
    #     datas_cds["debut"] = str(protein.cds.start)
    #     datas_cds["fin"] = str(protein.cds.stop)
    #     datas_cds["poids_moleculaire"] = str(protein.molecular_weight)
    #     datas_cds["complete"] = "0" if protein.is_partial else "1"
    #     query = get_query_insert("CDS", datas_cds)
    #     commit = commit_query(query)
    #     return commit
    #
    # def save_organism(self, protein):
    #     datas_org = {}
    #     datas_org["espece"] = "\"" + protein.species.species + "\"" if protein.species.species is not None else "NULL"
    #     datas_org["genre"] = "\"" + protein.species.genus + "\"" if protein.species.genus is not None else "NULL"
    #     datas_org["famille"] = "\"" + protein.species.family + "\"" if protein.species.family is not None else "NULL"
    #     datas_org["ordre"] = "\"" + protein.species.order + "\"" if protein.species.order is not None else "NULL"
    #     datas_org["sous_classe"] = "\"" + protein.species.subclass + "\"" if protein.species.subclass is not None else "NULL"
    #     datas_org["classe"] = "\"" + protein.species.classe + "\"" if protein.species.classe is not None else "NULL"
    #     datas_org["embranchement"] = "\"" + protein.species.phylum + "\"" if protein.species.phylum is not None else "NULL"
    #     query = get_query_insert("Organisme", datas_org)
    #     commit = commit_query(query)
    #     return commit
    #
    # def save_product(self, protein):
    #     datas_prod = {}
    #     datas_prod["id"] = "\"" + protein.id + "\""
    #     datas_prod["nom"] = "\"" + protein.name + "\""
    #     datas_prod["source"] = "\"NCBI\""
    #     datas_prod["note"] = "\"" + protein.note + "\"" if protein.note is not None else "NULL"
    #     datas_prod["espece"] = "\"" + protein.species.species + "\""
    #     datas_prod["id_cds"] = "\"cds_" + protein.id + "\""
    #     datas_prod["predicted"] = "1" if protein.is_predicted else "0"
    #     query = get_query_insert("Produit", datas_prod)
    #     commit = commit_query(query)
    #     return commit