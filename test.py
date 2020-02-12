from Bio import Entrez
from objects.NCBI_Product import *

Entrez.email = "claire.ceresa@hotmail.fr"

id = "EU159467.1"
product = NCBI_Product(id)
start = product.cds.start
stop = product.cds.stop
sequence = product.fiche.seq
print(sequence[start-1:stop])
