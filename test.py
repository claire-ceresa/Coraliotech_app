import sys
from Bio import Entrez
from graphic.Search_Window import *
from objects.DB_Search import *

Entrez.email = "claire.ceresa@hotmail.fr"

# TODO : VIDER LA BASE DE DONNEES !!
# TODO : FINIR D'IMPLEMENTER LA FENETRE SEARCH

terms = {'organism': {'checked': False, 'variable': '', 'value': ''},
         'name': {'checked': True, 'variable': 'nom', 'value': 'collagen'}}
search = DB_Search(terms)

app = QApplication(sys.argv)
form = Search_Window(search=search)
form.show()
app.exec()