from Bio import Entrez
from objects.DB_Search import *
from database.functions_db import *

Entrez.email = "claire.ceresa@hotmail.fr"

terms = {'organism': {'checked': True, 'variable': 'espece', 'value': 'Stylophora pistillata'},
         'name': {'checked': False, 'variable': 'nom', 'value': ''}
         }

search = DB_Search(terms)
names = []
for product in search.results:
    names.append(product.name)

interesting= get_all("Produits_interessants", "nom")

dict_excel = {"lists":[], "values":[]}

for substring in interesting:
    substring_in = []
    other = []
    for name in names:
        if substring in name:
            substring_in.append(name)
        else:
            other.append(name)
    dict_excel["lists"].append(substring_in)
    dict_excel["values"].append(substring)
    names = other
dict_excel["lists"].append(names)
dict_excel["values"].append("others")

print(dict_excel)