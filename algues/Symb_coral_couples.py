import xlsxwriter as x
from Bio import Entrez
from objects.DB_Search import DB_Search
from objects.NCBI_Product import NCBI_Product

Entrez.email = "claire.ceresa@hotmail.fr"

needed = {'organism': {'checked':True, 'variable':'famille', 'value':'Symbiodiniaceae'},
            'name':{'checked':False, 'variable':'nom', 'value':None}}

search = DB_Search(terms=needed)
list_products = search.results
list_ids = []

for product in list_products:
    id = product.id
    list_ids.append(id)

# search = NCBI_Search(request = "Symbiodiniaceae AND mRNA [Title] AND complete [Title] AND cds [Title] ")
# list_ids = search.get_list_ids()

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
    row = [id, species, host]
    worksheet.write_row(line, 0, row)

workbook.close()