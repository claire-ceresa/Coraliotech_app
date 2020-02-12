from graphic.product_view import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from objects.NCBI_Product import NCBI_Product
from objects.DB_Product import DB_Product

class Product_Window(QMainWindow, Ui_MainWindow):

        def __init__(self, parent=None, id=None):
            super(Product_Window, self).__init__(parent)
            self.setupUi(self)
            self.id = id
            self.setWindowTitle(self.id)
            self.product = DB_Product(id=self.id)
            self.set_window()

        def set_window(self):
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
