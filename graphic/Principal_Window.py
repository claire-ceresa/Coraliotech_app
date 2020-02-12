from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from graphic.principal_view import *
from graphic.NCBI_Window import NCBI_Window
from graphic.Product_Window import Product_Window
from objects.DB_Product import DB_Product

class Principal_Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Principal_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Coraliotech")
        self.set_image()
        self.window_download = NCBI_Window()

    def set_image(self):
        """set the logo on the window"""
        picture = QPixmap("logo.png")
        self.label_image.setPixmap(picture)

    def button_download_clicked(self):
        self.window_download.show()

    def button_complete_file_clicked(self):
        # TODO : a voir si utile. Si oui, voir pour gérer un template Excel ou systeme de creation
        return

    def button_complete_product_clicked(self):
        id = self.edit_complete_product.text()
        if len(id) == 0:
            message = QMessageBox()
            message.setText("Remplir le produit !")
            message.setWindowTitle("Attention !")
            message.exec()
        else:
            self.window_product = Product_Window(id=id)
            self.window_product.show()

    def button_search_clicked(self):
        # TODO : ouvre la liste des resultats (seulement id et nom) et quand clique, ouvre la fiche produit
        return

