import sys
from Bio import Entrez
from openpyxl import load_workbook
from pandas import DataFrame
from database.functions_db import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


Entrez.email = "claire.ceresa@hotmail.fr"

# filename  = "C:\\Users\claire\Desktop\Coraliotech\IUCN Status.xlsx"
# workbook = load_workbook(filename=filename)
# worksheet = workbook["Connus"]
# datas_total = DataFrame(worksheet.values)
# datas_needed = datas_total[[0, 1]]
#
# for row, row_data in datas_needed.iterrows():
#     statut = "\"" + row_data[1] + "\""
#     espece = "\"" + row_data[0] + "\""
#     query = 'UPDATE Organisme SET statutIUCN = ' + statut + ' WHERE espece = ' + espece
#     commit = commit_query(query)

# status = get_all("IUCN_Categories", "acronyme")
# status.append("Inconnu")
#
# app = QApplication(sys.argv)
# widget = QWidget()
# text, ok = QInputDialog.getItem(widget, 'Nouvelle espece', 'Selectionner le statut: ', status, len(status)-1, False)
# print(text)
# sys.exit(app.exec_())

species = "Zostera marina"
statut = "LC"
query = 'UPDATE Organisme SET statutIUCN = \"' + statut + '\" WHERE espece = \"' + species + '\"'
commit = commit_query(query)
print(commit)