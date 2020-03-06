import sys
from PyQt5.QtWidgets import *
from graphic.Product_Window import *
from Bio import Entrez
from objects.DB_Product import *
from objects.DB_Application import *

Entrez.email = "claire.ceresa@hotmail.fr"

# KJ766310.1 datas
# KJ780789.1 vide

app = QApplication(sys.argv)
window = Product_Window(id="KJ780789.1")
window.show()
sys.exit(app.exec_())

product = DB_Product(id='KJ780789.1')
#application = DB_Application(id='KJ766310.1', nom_application='Biotechnologie')
for app in product.applications:
    print(app.id)
    print(app.name_app)
    print(app.validity)
    print(app.remark)