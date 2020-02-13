from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from graphic.principal_view import *
from graphic.NCBI_Window import NCBI_Window
from graphic.Product_Window import Product_Window
from graphic.graphics_functions import *
from database.functions_db import *
from objects.DB_Search import *


class Principal_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for principal_view
    """
    def __init__(self, parent=None):
        super(Principal_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Coraliotech")
        self.window_product = None
        self._set_image()
        self._set_combobox_org()

    # CLASS METHOD #

    def button_download_clicked(self):
        """when button download is clicked, open the NCBI window"""
        self.window_download = NCBI_Window()
        self.window_download.show()

    def button_visualise_product_clicked(self):
        """when button Go is clicked : open a product or propose to download it"""
        id = self.edit_visualise_product.text()
        if len(id) == 0:
            create_messageBox(title="Attention !", text="Remplir le produit")
        else:
            self.window_product = Product_Window(id=id)
            if self.window_product.existed:
                self.window_product.show()
            else:
                message = QMessageBox.question(self, "Attention" ,"Le produit n'est pas enregistre ! \nVoulez vous l'enregistrer ?", QMessageBox.Yes, QMessageBox.Cancel)
                if message == QMessageBox.Yes:
                    try:
                        self.window_download = NCBI_Window()
                        self.window_download.edit_id.setText(id)
                        self.window_download.show()
                    except Exception as e:
                        print(e)

    def button_search_clicked(self):
        product_name = str(self.edit_search_name.text())
        organism_type = str(self.combobox_search_org.currentText())
        organism_value = str(self.edit_search_org.text())
        terms = {'organism': {'checked':False, 'variable':'', 'value':''},
                 'name':{'checked':False, 'variable':'nom', 'value':''}
                 }

        if self.checkbox_search_org.isChecked() and not self.checkbox_search_name.isChecked():
            if len(organism_value) > 0:
                terms["organism"]["checked"] = True
                terms["organism"]["variable"] = organism_type
                terms["organism"]["value"] = organism_value
            else:
                create_messageBox("Attention !", "Remplir le champs !")

        elif not self.checkbox_search_org.isChecked() and self.checkbox_search_name.isChecked():
            terms["name"]["checked"] = True
            terms["name"]["value"] = product_name

        elif self.checkbox_search_org.isChecked() and self.checkbox_search_name.isChecked():
            if len(organism_value) > 0:
                terms["organism"]["checked"] = True
                terms["organism"]["variable"] = organism_type
                terms["organism"]["value"] = organism_value
                terms["name"]["checked"] = True
                terms["name"]["value"] = product_name
            else:
                create_messageBox("Attention !", "Remplir le champs !")

        else:
            create_messageBox("Attention !", "Choisir un champs !")

        search = DB_Search(terms)
        print(search.query)


    def button_treate_file_clicked(self):
        # TODO : a voir si utile. Si oui, voir pour gérer un template Excel ou systeme de creation
        return

    # GRAPHIC METHODS #

    def _set_image(self):
        """set the logo on the window"""
        picture = QPixmap("logo.png")
        self.label_image.setPixmap(picture)

    def _set_combobox_org(self):
        columns = get_column_names("Organisme")
        for column in columns:
            self.combobox_search_org.addItem(column)
        self.combobox_search_org.setEnabled(False)
