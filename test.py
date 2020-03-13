import sys
from PyQt5.QtWidgets import *
from graphic.Product_Window import *
from graphic.Phylogeny_Window import *
from Bio import Entrez
from objects.DB_Product import *
from objects.DB_Application import *
from objects.NCBI_Search import NCBI_Search

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Phylogeny_Window(group="Mangroves")
form.show()
app.exec()