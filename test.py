from Bio import Entrez
from objects.DB_Search import DB_Search
import operator

Entrez.email = "claire.ceresa@hotmail.fr"

def split_list_on_index(data_list, index_list):
    all_index = (0,) + tuple(data + 1 for data in index_list) + (len(data_list),)
    all_lists = []
    for start, end in zip(all_index, all_index[1:]):
        all_lists.append(results[start:end])
    return all_lists



terms = {'organism': {'checked': True, 'variable': 'genre', 'value': 'Zostera'},
         'name': {'checked': False, 'variable': 'nom', 'value': ''}
         }
search = DB_Search(terms)
results = search.results

print("RESULTAT BRUTES")

idx_list = []
for index, product in enumerate(results[:-1]):
    print(str(index) + " - " + product.organism.species)
    if results[index].organism.species != results[index+1].organism.species:
        idx_list.append(index)
#idx_list = [index for index, product in enumerate(results[:-1]) if results[index].organism.species != results[index+1].organism.species]
print(idx_list)

#print("RESULTAT TRIE")

sorted_results = sorted(results, key=operator.attrgetter('organism.species'))

idx_sorted_list = []
for index, product in enumerate(sorted_results[:-1]):
    #print(str(index) + " - " + product.organism.species)
    if sorted_results[index].organism.species != sorted_results[index + 1].organism.species:
        idx_sorted_list.append(index)
#idx_sorted_list = [index for index, product in enumerate(sorted_results[:-1]) if sorted_results[index].organism.species != sorted_results[index+1].organism.species ]
#print(idx_sorted_list)

# all_index = (0,) + tuple(data+1 for data in idx_list) + (len(results),)
# print(all_index)
# all_lists = []
# for start, end in zip(all_index, all_index[1:]):
#     all_lists.append(results[start:end])

all_lists = split_list_on_index(results, idx_list)

for index, list in enumerate(all_lists):
    print('liste ' + str(index+1))
    for product in list:
        print(product.organism.species)



