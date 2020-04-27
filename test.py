from objects.NCBI_Product import NCBI_Product
from Bio import Entrez

Entrez.email = "claire.ceresa@hotmail.fr"
id = "KX254551.1"
product = NCBI_Product(id=id)
name = product.name
taxo = product.species.taxonomy
length = product.cds.length
mw = product.molecular_weight
species = product.species.species
row = [species, id, name, length, mw]
print(row)
