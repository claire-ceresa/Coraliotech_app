from PyQt5.QtWidgets import *
from graphic.ncbi_view import *
from objects.NCBI_Search import NCBI_Search
from objects.NCBI_Product import NCBI_Product
from graphic.graphics_functions import *
from other_files.useful_functions import *


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
        """Fill in the edit request"""
        if self._organism_written():
            terms = self._get_request_terms()
            request = self._create_request(terms)
            self.edit_request.setEnabled(True)
            self.edit_id.setEnabled(False)
            self.edit_request.setText(request)

    def button_go_pressed(self):
        """Clean the previous messages"""
        if len(self.edit_request.text()) > 0:
            self.label_messages.setText("Chargement...")

    def button_go_clicked(self):
        """Save the result of the request on NCBI on the local DB """

        url = "https://www.ncbi.nlm.nih.gov/nucleotide/"
        connexion = connected_to_internet(url)

        if connexion["connected"]:

            if self.edit_request.isEnabled() and len(self.edit_request.text()) > 0:
                request = self.edit_request.text()
            elif self.edit_id.isEnabled() and len(self.edit_id.text()) > 0:
                request = self.edit_id.text() + "[Accession]"
            else:
                create_messageBox(title="Attention !", text="Il y a un problème !")
                return

            search = NCBI_Search(request)
            list_id = search.get_list_ids()

            nb_product_saved = 0
            products_not_saved = []

            if len(list_id) > 0:
                for id in list_id:
                    product = NCBI_Product(id)
                    if self._check_exceptions(product):
                        saved = product.save_on_database()

                        if saved["product"]["commited"]:

                            nb_product_saved = nb_product_saved + 1
                            if saved["organism"]["commited"]:
                                all_statut = get_all("IUCN_Categories", "acronyme")
                                all_statut.append("Inconnu")
                                species = product.species.species
                                statut, ok = QInputDialog.getItem(self, 'Nouvelle espece !', 'Selectionner le statut IUCN pour ' + species + ' : ',
                                                                  all_statut,
                                                                  len(all_statut) - 1, False)
                                if statut is not "Inconnu":
                                    modif = modif_IUCN_statut(species, statut)

                        else:
                            products_not_saved.append({'id':product.id, 'error':saved["product"]["error"]})
                    else:
                        products_not_saved.append({'id': product.id, 'error': "Exception non utilisable"})

            message = str(nb_product_saved) + " resultats enregistres dans la base de donnees !"
            if len(products_not_saved) > 0:
                message = message + "\n" + str(len(products_not_saved)) + " non enregistres : \n"
                for product in products_not_saved:
                    message = message + " - " + product["id"] + " : " + product["error"] + "\n"

            self._clean_widgets(message)

        else:
            create_messageBox("Attention", "Vous n'etes pas connecte a Internet !\n" + connexion["error"])
            self.label_messages.setText("")

    # GRAPHIC METHODS #

    def _clean_widgets(self, message):
        """Clean all the QWidgets after a research is done"""
        self.label_messages.setText(message)
        self.edit_request.setEnabled(False)
        self.edit_id.setEnabled(True)
        self.edit_id.setText("")
        self.edit_request.setText("")
        self.edit_org.setText("")

    def _get_request_terms(self):
        """
        Getting the value of all the QEdits
        :return a dictionnary of the values needed to build the request
        """
        terms = dict()
        terms["organism"] = self.edit_org.text()
        keys = self.edit_keys.text()
        in_terms = self.edit_in.text()
        out_terms = self.edit_out.text()

        if len(keys) > 0:
            terms["keys"] = keys.split(",")
        else:
            terms["keys"] = []

        if len(in_terms) > 0:
            terms["in_terms"] = in_terms.split(",")
        else:
            terms["in_terms"] = []

        if len(out_terms) > 0:
            terms["out_terms"] = out_terms.split(",")
        else:
            terms["out_terms"] = []

        return terms

    # OTHER METHODS #

    def _create_request(self, terms):
        """
        Create the good NCBI request
        :param terms : a dictionnary of all the values
        :return the request
        """
        beginning = terms["organism"] + " [Organism]"
        and_terms = ""
        not_terms = ""

        for key in terms["keys"]:
            and_terms = and_terms + " AND " + key.strip()
        for in_term in terms["in_terms"]:
            and_terms = and_terms + " AND " + in_term.strip() + " [Title]"
        for out_term in terms["out_terms"]:
            not_terms = not_terms + " NOT " + out_term.strip() + " [Title]"

        request = beginning + and_terms + not_terms
        return request

    def _organism_written(self):
        """
        Check if the QEdit of the organism is filled
        :return boolean
        """
        if len(self.edit_org.text()) == 0:
            create_messageBox(title="Attention", text="Remplir un organisme !")
            return False
        return True

    def _check_exceptions(self, product):
        """
        Check if the data is valid, based on decided rules
        :param product: a Product object
        :return boolean
        """

        if product.molecular_weight is None:
        # Unknown molecular weight = error in the ADN sequence
            return False

        if product.name is None:
        # Unknown name = unuseful product
            return False

        if product.cds is None:
        # No cds feature = unuseful product
            return False

        return True

