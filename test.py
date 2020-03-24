import sys
import xlsxwriter as x
from PyQt5.QtWidgets import *
from graphic.Product_Window import *
from graphic.Phylogeny_Window import *
from Bio import Entrez
from objects.DB_Product import *
from objects.DB_Application import *
from objects.NCBI_Search import NCBI_Search
from objects.NCBI_Product import NCBI_Product

Entrez.email = "claire.ceresa@hotmail.fr"

search = NCBI_Search(request = "Symbiodiniaceae AND mRNA [Title] AND complete [Title] AND cds [Title] ")
list_ids = search.get_list_ids()

workbook = x.Workbook("host.xlsx")
worksheet = workbook.add_worksheet("Couples")

for line, id in enumerate(list_ids):
    print(str(line))
    product = NCBI_Product(id=id)
    species = product.species.species
    feature_source = product.get_feature_by_type("source")
    if "host" in feature_source.qualifiers:
        host = feature_source.qualifiers["host"][0]
    else:
        host = None
    row = [species, host]
    worksheet.write_row(line, 0, row)

workbook.close()