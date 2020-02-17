import sys
import inspect
from Bio import Entrez
from graphic.Excel_Window import *
from objects.DB_Organism import *
from objects.DB_Product import *

Entrez.email = "claire.ceresa@hotmail.fr"

# app = QApplication(sys.argv)
# form = Excel_Window()
# form.show()
# app.exec()

prod = DB_Product("EU159467.1")
print(prod.get_attributes())

