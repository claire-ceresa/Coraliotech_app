from PyQt5.QtWidgets import *
from graphic.ncbi_view import *
from database.functions_db import *
from objects.NCBI_Search import NCBI_Search
from objects.NCBI_Product import NCBI_Product


class NCBI_Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(NCBI_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telecharger")

    def button_write_clicked(self):
        if self.organism_written():
            terms = self.get_request_terms()
            request = self.create_request(terms)
            self.edit_request.setEnabled(True)
            self.edit_request.setText(request)
            self.button_go.setEnabled(True)
            self.edit_id.setEnabled(False)

    def button_go_pressed(self):
        self.label_messages.setText("")

    def button_go_clicked(self):
        if self.edit_request.isEnabled():
            request = self.edit_request.text()
        elif self.edit_id.isEnabled():
            request = self.edit_id.text() + "[Accession]"
        else:
            print("probleme")

        search = NCBI_Search(request)

        try:
            list_id = search.get_list_ids()
        except Exception as e:
            print(e)


        nb_product_saved = 0
        product_not_saved = []

        if len(list_id) > 0:
            for id in list_id:
                protein = NCBI_Product(id)
                save = self.save_protein(protein)
                if self.check_exceptions(protein) and save["commited"]:
                    nb_product_saved = nb_product_saved + 1
                else:
                    product_not_saved.append({'id':protein.id, 'error':save["error"]})

        if len(product_not_saved) > 0:
            message = str(len(product_not_saved)) + " non enregistres : \n"
            for product in product_not_saved:
                message = message + " - " + product["id"] + " : " + product["error"] + "\n"
        else:
            message = str(nb_product_saved) + " resultat enregistre dans la base de donnees"
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

    def save_protein(self, protein):
        self.save_cds(protein)
        self.save_organism(protein)
        product = self.save_product(protein)
        return product

    def save_cds(self, protein):
        datas_cds = {}
        datas_cds["id"] = "\"cds_" + protein.id + "\""
        datas_cds["debut"] = str(protein.cds.start)
        datas_cds["fin"] = str(protein.cds.stop)
        datas_cds["poids_moleculaire"] = str(protein.molecular_weight)
        datas_cds["complete"] = "0" if protein.is_partial else "1"
        query = get_query_insert("CDS", datas_cds)
        commit = commit_query(query)
        return commit

    def save_organism(self, protein):
        datas_org = {}
        datas_org["espece"] = "\"" + protein.species.species + "\"" if protein.species.species is not None else "NULL"
        datas_org["genre"] = "\"" + protein.species.genus + "\"" if protein.species.genus is not None else "NULL"
        datas_org["famille"] = "\"" + protein.species.family + "\"" if protein.species.family is not None else "NULL"
        datas_org["ordre"] = "\"" + protein.species.order + "\"" if protein.species.order is not None else "NULL"
        datas_org["sous_classe"] = "\"" + protein.species.subclass + "\"" if protein.species.subclass is not None else "NULL"
        datas_org["classe"] = "\"" + protein.species.classe + "\"" if protein.species.classe is not None else "NULL"
        datas_org["embranchement"] = "\"" + protein.species.phylum + "\"" if protein.species.phylum is not None else "NULL"
        query = get_query_insert("Organisme", datas_org)
        commit = commit_query(query)
        return commit

    def save_product(self, protein):
        datas_prod = {}
        datas_prod["id"] = "\"" + protein.id + "\""
        datas_prod["nom"] = "\"" + protein.name + "\""
        datas_prod["source"] = "\"NCBI\""
        datas_prod["note"] = "\"" + protein.note + "\"" if protein.note is not None else "NULL"
        datas_prod["espece"] = "\"" + protein.species.species + "\""
        datas_prod["id_cds"] = "\"cds_" + protein.id + "\""
        datas_prod["predicted"] = "1" if protein.is_predicted else "0"
        query = get_query_insert("Produit", datas_prod)
        commit = commit_query(query)
        return commit

    def organism_written(self):
        if len(self.edit_org.text()) == 0:
            message = QMessageBox()
            message.setText("Remplir un organisme !")
            message.setWindowTitle("Attention !")
            message.exec()
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



    # TODO : reprendre toute la classe avec nouvelle nomenclature

    # def fill_box_type(self):
    #     """fill the comboBox with the name of the created styles"""
    #     files = listdir('files_type')
    #     for file in files:
    #         list = file.split(".")[0].split("_")
    #         name = " ".join(list)
    #         self.box_type.addItem(name)
    #
    # def button_ok_pressed(self):
    #     """instructions when the button ok is pressed"""
    #     self._clean_labels()
    #
    # def button_ok_clicked(self):
    #     """instructions when button ok is clicked"""
    #
    #     try:
    #         infos = self.get_info()
    #         organism = infos[0]
    #         request = infos[1]
    #         type = infos[2]
    #         search = Search(organism=organism, request=request, type=type)
    #
    #     except Exception as e:
    #         self.label_error.setText("ERROR : " + str(e))
    #
    #     else:
    #         self.label_nb_result.setText(str(search.nb_result) + " results found.")
    #
    #         if len(search.errors) > 0:
    #             text_errors = "ERRORS :\n"
    #             for error in search.errors:
    #                 text_errors = text_errors + " - " + error + "\n"
    #             self.label_error.setText(text_errors)
    #
    #         if search.file_created is True:
    #             self.label_create.setText("File created !")
    #         else:
    #             self.label_create.setText("ERROR : File not created !")
    #
    #     self.button_ok.setEnabled(False)
    #
    # def button_request_clicked(self):
    #     """instruction when button request clicked"""
    #     self.button_ok.setEnabled(True)
    #     self.edit_request.setEnabled(True)
    #     self.set_request()
    #
    # def get_request(self):
    #     """export requests from the json file"""
    #     with open('types.json') as json_data:
    #         requests = json.load(json_data)
    #     return requests
    #
    # def set_request(self):
    #     """fill in the edit request"""
    #     organism = self.edit_organism.text()
    #     type = self.box_type.currentText()
    #
    #     if len(organism) == 0 or len(type) == 0:
    #         self._print_warning_message()
    #     else:
    #         requests = self.get_request()
    #         request_end = requests[type]
    #         request = organism + " AND " + request_end
    #         self.edit_request.setText(request)
    #
    # def get_info(self):
    #     """get the request from the LineEdit"""
    #     organism = self.edit_organism.text()
    #     request = self.edit_request.text()
    #     type = self.box_type.currentText()
    #
    #     if len(organism) == 0 or len(type) == 0 or self.box_type.currentIndex() == 0:
    #         self._print_warning_message()
    #     else:
    #         return [organism, request, type]
    #
    # def _print_warning_message(self):
    #     """open a warning message if the request's not complete"""
    #     message = QMessageBox()
    #     message.setText("Remplir les 3 champs !")
    #     message.setWindowTitle("Attention !")
    #     message.exec()
    #
    # def _clean_labels(self):
    #     """clean all the labels between 2 researches"""
    #     self.label_create.setText("")
    #     self.label_error.setText("")
    #     self.label_nb_result.setText("")