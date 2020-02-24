from PyQt5.QtWidgets import *
from graphic.ncbi_view import *
from objects.NCBI_Search import NCBI_Search
from objects.NCBI_Product import NCBI_Product
from graphic.graphics_functions import *
from useful_functions import *


class NCBI_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for ncbi_view
    """
    def __init__(self, parent=None):
        super(NCBI_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telecharger")

    # METHOD OF THE CLASS #

    def button_write_clicked(self):
        """when button write is clicked, fill in the edit request"""
        if self.organism_written():
            terms = self.get_request_terms()
            request = self.create_request(terms)
            self.edit_request.setEnabled(True)
            self.button_go.setEnabled(True)
            self.edit_id.setEnabled(False)
            self.edit_request.setText(request)

    def button_go_pressed(self):
        """clean the previous messages"""
        self.label_messages.setText("Chargement...")

    def button_go_clicked(self):
        """when button go is clicked, save on the DB the result of the request on NCBI"""

        url = "https://www.ncbi.nlm.nih.gov/nucleotide/"
        if connected_to_internet(url):

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
                    if self.check_exceptions(product):
                        saved = product.save_on_database()
                        if saved["commited"]:
                            nb_product_saved = nb_product_saved + 1
                        else:
                            products_not_saved.append({'id':product.id, 'error':saved["error"]})
                    else:
                        products_not_saved.append({'id': product.id, 'error': "Exception non utilisable"})

            message = str(nb_product_saved) + " resultats enregistres dans la base de donnees !"
            if len(products_not_saved) > 0:
                message = message + "\n" + str(len(products_not_saved)) + " non enregistres : \n"
                for product in products_not_saved:
                    message = message + " - " + product["id"] + " : " + product["error"] + "\n"

            self.clean_widgets(message)

        else:
            create_messageBox("Attention", "Vous n'etes pas connecte a Internet !")
            self.label_messages.setText("")

    # GRAPHIC METHODS #

    def clean_widgets(self, message):
        """clean all the widgets after a research is done"""
        self.label_messages.setText(message)
        self.edit_request.setEnabled(False)
        self.edit_id.setEnabled(True)
        self.edit_id.setText("")
        self.edit_request.setText("")
        self.edit_org.setText("")

    def get_request_terms(self):
        """:return the value of the edits to build the request"""
        terms = dict()
        terms["organism"] = self.edit_org.text()
        keys = self.edit_keys.text()
        in_terms = self.edit_in.text()
        out_terms = self.edit_out.text()

        if len(keys) > 0:
            terms["keys"] = keys.split(" , ")
        else:
            terms["keys"] = []

        if len(in_terms) > 0:
            terms["in_terms"] = in_terms.split(" , ")
        else:
            terms["in_terms"] = []

        if len(out_terms) > 0:
            terms["out_terms"] = out_terms.split(" , ")
        else:
            terms["out_terms"] = []

        return terms

    # GENERAL METHODS#

    def create_request(self, terms):
        """:return the request, created thanks to the terms written"""
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

    def organism_written(self):
        """:return boolean if an organism is written for the research"""
        if len(self.edit_org.text()) == 0:
            create_messageBox(title="Attention", text="Remplir un organisme !")
            return False
        return True

    def check_exceptions(self, protein):
        """:return boolean is the data is valid"""
        if protein.molecular_weight is None:
            return False
        if protein.name is None:
            return False
        return True

