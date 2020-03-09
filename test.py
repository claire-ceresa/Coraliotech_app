import sys
from PyQt5.QtWidgets import *
from graphic.Product_Window import *
from Bio import Entrez
from objects.DB_Product import *
from objects.DB_Application import *

Entrez.email = "claire.ceresa@hotmail.fr"

# KJ766310.1 datas
# KJ780789.1 vide

app = QApplication(sys.argv)
window = Product_Window(id="XM_015916425.1")
window.show()
sys.exit(app.exec_())

