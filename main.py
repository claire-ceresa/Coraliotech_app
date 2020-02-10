import sys
from Bio import Entrez
from PyQt5.QtWidgets import QApplication
from graphic.Principal_Window import Principal_Window

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Principal_Window()
form.show()
app.exec()