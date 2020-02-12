from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from graphic.principal_view import *
from graphic.NCBI_Window import NCBI_Window
from graphic.Product_Window import Product_Window
from graphic.graphics_functions import *


class Principal_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for principal_view
    """
    def __init__(self, parent=None):
        super(Principal_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Coraliotech")
        self.set_image()
        self.window_download = None
        self.window_product = None

    def set_image(self):
        """set the logo on the window"""
        picture = QPixmap("logo.png")
        self.label_image.setPixmap(picture)

    def button_download_clicked(self):
        """when button download is clicked, open the NCBI window"""
        self.window_download = NCBI_Window()
        self.window_download.show()

    def button_complete_file_clicked(self):
        # TODO : a voir si utile. Si oui, voir pour gérer un template Excel ou systeme de creation
        return

    def button_complete_product_clicked(self):
        """when button Go is clicked : open a product or propose to download it"""
        id = self.edit_complete_product.text()
        if len(id) == 0:
            create_messageBox(title="Attention !", text="Remplir le produit")
        else:
            self.window_product = Product_Window(id=id)
            if self.window_product.existed:
                self.window_product.show()
            else:
                message = QMessageBox.question(self, "Attention" ,"Le produit n'est pas enregistre ! \nVoulez vous l'enregistrer ?", QMessageBox.Yes, QMessageBox.Cancel)
                if message == QMessageBox.Yes:
                    self.window_download.edit_id.setText(id)
                    self.window_download.show()

    def button_search_clicked(self):
        # TODO : ouvre la liste des resultats (seulement id et nom) et quand clique, ouvre la fiche produit
        return

