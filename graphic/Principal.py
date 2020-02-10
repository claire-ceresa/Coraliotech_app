from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from graphic.principal_view import *
from graphic.NCBI import NCBI
from graphic.Product import Product
from database.functions_db import *

class Principal(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.set_image()
        self.window_download = NCBI()
        self.window_complete = Product(id="EU159467.1")

    def set_image(self):
        """set the logo on the window"""
        picture = QPixmap("logo.png")
        self.label_image.setPixmap(picture)

    def button_complete_file_clicked(self):
        # TODO : a voir si utile. Si oui, voir pour gérer un template Excel ou systeme de creation
        return

    def button_complete_product_clicked(self):
        # TODO : ouvre la fiche produit modifiable, avec fiche GenBank + autre info complementaire
        self.window_complete.show()

    def button_search_clicked(self):
        # TODO : ouvre la liste des resultats (seulement id et nom) et quand clique, ouvre la fiche produit
        return

    def button_download_clicked(self):
        self.window_download.show()