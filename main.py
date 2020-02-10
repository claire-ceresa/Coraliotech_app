import sys
from Bio import Entrez
from PyQt5.QtWidgets import QApplication
from graphic.Principal import Principal

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Principal()
form.show()
app.exec()