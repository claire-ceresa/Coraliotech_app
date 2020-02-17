import sys
from Bio import Entrez
from graphic.Excel_Window import *
from objects.DB_Organism import *

Entrez.email = "claire.ceresa@hotmail.fr"

app = QApplication(sys.argv)
form = Excel_Window()
form.show()
app.exec()

