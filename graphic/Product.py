from graphic.product_view import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from object.Protein import Protein
import sqlite3 as s

class Product(QMainWindow, Ui_MainWindow):

        def __init__(self, parent=None, id=None):
            super(Product, self).__init__(parent)
            self.setupUi(self)
            self.id = id
            self.setWindowTitle(self.id)
            self.set_fiche()

        def set_fiche(self):
            protein = Protein(self.id)
            protein.save_genbank_file()
            text = open('fiche.txt').read()
            self.edit_fiche.setPlainText(text)
