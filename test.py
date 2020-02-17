import sys
from Bio import Entrez
from graphic.Search_Window import *
from objects.DB_Search import *

Entrez.email = "claire.ceresa@hotmail.fr"

# TODO : VIDER LA BASE DE DONNEES !!
# TODO : FINIR D'IMPLEMENTER LA FENETRE SEARCH

terms = {'organism': {'checked': True, 'variable': 'genre', 'value': 'Pocillopora'},
         'name': {'checked': False, 'variable': 'nom', 'value': ''}}
search = DB_Search(terms)

app = QApplication(sys.argv)
form = Search_Window(search=search)
form.show()
app.exec()