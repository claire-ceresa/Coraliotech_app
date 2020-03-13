import sys
from PyQt5.QtWidgets import *
from graphic.Product_Window import *
from Bio import Entrez
from objects.DB_Product import *
from objects.DB_Application import *
from objects.NCBI_Search import NCBI_Search

Entrez.email = "claire.ceresa@hotmail.fr"

query = "Anthozoa AND interleukin [Title] AND mRNA [Title] NOT partial [Title] "
search = NCBI_Search(request=query)
result = search.get_list_ids()
print(result)
