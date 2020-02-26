from Bio import Entrez
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
from other_files.useful_functions import *

Entrez.email = "claire.ceresa@hotmail.fr"

species = "Acropora millepora"
species_low = species.lower()
url_text = 'https://www.iucnredlist.org/search?query={0}&searchType=species'.format(str(species))
print(url_text)
url = QUrl(url_text)
print(url)
encode = url.toEncoded()
print(type(encode))

window = QWebEngineView()


app = QApplication(sys.argv)
# form = QMainWindow()
# form.setCentralWidget(window)
window.setUrl(url)
window.show()
#form.show()
app.exec()



