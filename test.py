from Bio import Entrez
from database.functions_db import *

Entrez.email = "claire.ceresa@hotmail.fr"

print("connected" if connected_to_ncbi_server() else "no internet!" )
