import sys
import inspect
from Bio import Entrez
from graphic.Excel_Window import *
from graphic.Search_Window import *
from objects.DB_Search import *
from objects.DB_Product import *

Entrez.email = "claire.ceresa@hotmail.fr"

terms = {'organism': {'checked': True, 'variable': 'genre', 'value': 'Stylophora'},
         'name': {'checked': False, 'variable': 'nom', 'value': ''}
         }
search = DB_Search(terms=terms)

app = QApplication(sys.argv)
form = Search_Window(search=search)
form.show()
app.exec()
