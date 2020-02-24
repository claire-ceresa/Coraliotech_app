#from Bio import Entrez
#Entrez.email = "claire.ceresa@hotmail.fr"

# !/usr/bin/python

import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl("https://www.iucnredlist.org/search?query=pocillopora%20damicornis&searchType=species"))
web.show()

sys.exit(app.exec_())