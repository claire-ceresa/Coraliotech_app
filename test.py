from Bio import Entrez
from PyQt5.QtWidgets import *
import sys
from graphic.Product_Window import Product_Window


Entrez.email = "claire.ceresa@hotmail.fr"


app = QApplication(sys.argv)

window = Product_Window(id= "EU159467.1")
sys.exit(app.exec_())