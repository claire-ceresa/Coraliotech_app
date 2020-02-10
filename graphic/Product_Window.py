from graphic.product_view import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from objects.NCBI_Product import NCBI_Product
import sqlite3 as s

class Product_Window(QMainWindow, Ui_MainWindow):

        def __init__(self, parent=None, id=None):
            super(Product_Window, self).__init__(parent)
            self.setupUi(self)
            self.id = id
            self.setWindowTitle(self.id)
            self.set_fiche()

        def set_fiche(self):
            protein = NCBI_Product(self.id)
            protein.save_genbank_file()
            text = open('fiche.txt').read()
            self.edit_fiche.setPlainText(text)
