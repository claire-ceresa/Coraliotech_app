from Bio import Entrez
from PyQt5.QtWidgets import *
import sys
from graphic.Product_Window import Product_Window
from example import *

Entrez.email = "claire.ceresa@hotmail.fr"


app = QApplication(sys.argv)
window = QMainWindow()
test = WisdomCompositeWidget()
window.setCentralWidget(test)
window.show()
app.exec()