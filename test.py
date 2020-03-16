import sys
from PyQt5.QtWidgets import *
from graphic.Product_Window import *
from graphic.Phylogeny_Window import *
from Bio import Entrez
from objects.DB_Product import *
from objects.DB_Application import *
from objects.NCBI_Search import NCBI_Search
from objects.NCBI_Product import NCBI_Product

Entrez.email = "claire.ceresa@hotmail.fr"

id ="GU722140.1"
product = NCBI_Product(id=id)
print(product.cds)