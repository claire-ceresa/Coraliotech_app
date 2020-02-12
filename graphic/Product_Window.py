from graphic.product_view import Ui_MainWindow
from database.functions_db import *
from PyQt5.QtWidgets import *
from objects.NCBI_Product import NCBI_Product
from objects.DB_Product import DB_Product

class Product_Window(QMainWindow, Ui_MainWindow):

        def __init__(self, parent=None, id=None):
            super(Product_Window, self).__init__(parent)
            self.setupUi(self)
            self.setWindowTitle(id)
            self.id = id
            self.app_checkboxes = []
            self.create_frame_app()
            self.product = DB_Product(id=self.id)
            self.existed = self.product.existed
            if self.existed:
                self.set_window()


        def create_frame_app(self):
            applications = get_all_applications_possibles()
            layout = QVBoxLayout()
            self.app_groupbox_checkboxes.setLayout(layout)
            for application in applications:
                checkbox = QCheckBox()
                checkbox.setText(application[0])
                layout.addWidget(checkbox)
                self.app_checkboxes.append(checkbox)

        def set_window(self):
            self.set_labels()
            self.set_fiche()
            self.set_applications()

        def set_labels(self):
            self.prod_label_name.setText(self.product.name)
            self.prod_label_source.setText(self.product.source)
            self.prod_label_id.setText(self.product.id)
            text_cds = str(self.product.cds.start) + "-" + str(self.product.cds.stop)
            self.prod_label_cds_value.setText(text_cds)
            self.prod_label_length_value.setText(str(self.product.cds.length) + " pb")
            self.prod_label_weight_value.setText(str(self.product.cds.mw) + " kD")
            if self.product.cds.complete == 0:
                self.prod_label_complete_value.setText("non")
                self.prod_label_complete_value.setStyleSheet('color:red')
            else:
                self.prod_label_complete_value.setText("oui")
            if self.product.predicted == 0:
                self.prod_label_pred_value.setText("non")
            else:
                self.prod_label_pred_value.setText("oui")
                self.prod_label_pred_value.setStyleSheet('color:red')
            self.prod_edit_note.setPlainText(self.product.note)
            self.esp_label_name.setText(self.product.species)


        def set_applications(self):
            for application in self.product.applications:
                for checkbox in self.app_checkboxes:
                    if application["nom_app"] == checkbox.text():
                        checkbox.setChecked(True)
                        checkbox.setStyleSheet('font:bold')

        def set_fiche(self):
            protein = NCBI_Product(self.id)
            protein.save_genbank_file()
            text = open('fiche.txt').read()
            self.edit_fiche.setPlainText(text)

        def app_button_modif_clicked(self):
            # TODO : creer modification des applications
            return

        def esp_button_open_clicked(self):
            # TODO : creer fenetre espece
            return
