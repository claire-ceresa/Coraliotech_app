# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 554)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layout_header = QtWidgets.QHBoxLayout()
        self.layout_header.setObjectName("layout_header")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_header.addItem(spacerItem)
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setMinimumSize(QtCore.QSize(0, 55))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.layout_header.addWidget(self.label_image)
        self.verticalLayout_5.addLayout(self.layout_header)
        self.frame_download = QtWidgets.QFrame(self.centralwidget)
        self.frame_download.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_download.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_download.setObjectName("frame_download")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_download)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_download = QtWidgets.QLabel(self.frame_download)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_download.setFont(font)
        self.label_download.setObjectName("label_download")
        self.verticalLayout_2.addWidget(self.label_download)
        self.layout_database = QtWidgets.QHBoxLayout()
        self.layout_database.setObjectName("layout_database")
        self.label_database = QtWidgets.QLabel(self.frame_download)
        self.label_database.setObjectName("label_database")
        self.layout_database.addWidget(self.label_database)
        self.combobox_database = QtWidgets.QComboBox(self.frame_download)
        self.combobox_database.setObjectName("combobox_database")
        self.combobox_database.addItem("")
        self.layout_database.addWidget(self.combobox_database)
        self.verticalLayout_2.addLayout(self.layout_database)
        self.button_download = QtWidgets.QPushButton(self.frame_download)
        self.button_download.setObjectName("button_download")
        self.verticalLayout_2.addWidget(self.button_download)
        self.verticalLayout_5.addWidget(self.frame_download)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.frame_search = QtWidgets.QFrame(self.centralwidget)
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_search.setObjectName("frame_search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_search)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_search = QtWidgets.QLabel(self.frame_search)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_search.setFont(font)
        self.label_search.setObjectName("label_search")
        self.verticalLayout_3.addWidget(self.label_search)
        self.layout_search_org = QtWidgets.QHBoxLayout()
        self.layout_search_org.setObjectName("layout_search_org")
        self.checkbox_search_org = QtWidgets.QCheckBox(self.frame_search)
        self.checkbox_search_org.setObjectName("checkbox_search_org")
        self.layout_search_org.addWidget(self.checkbox_search_org)
        self.combobox_search_org = QtWidgets.QComboBox(self.frame_search)
        self.combobox_search_org.setObjectName("combobox_search_org")
        self.layout_search_org.addWidget(self.combobox_search_org)
        self.edit_search_org = QtWidgets.QLineEdit(self.frame_search)
        self.edit_search_org.setEnabled(False)
        self.edit_search_org.setObjectName("edit_search_org")
        self.layout_search_org.addWidget(self.edit_search_org)
        self.verticalLayout_3.addLayout(self.layout_search_org)
        self.layout_search_name = QtWidgets.QHBoxLayout()
        self.layout_search_name.setObjectName("layout_search_name")
        self.checkbox_search_name = QtWidgets.QCheckBox(self.frame_search)
        self.checkbox_search_name.setObjectName("checkbox_search_name")
        self.layout_search_name.addWidget(self.checkbox_search_name)
        self.edit_search_name = QtWidgets.QLineEdit(self.frame_search)
        self.edit_search_name.setEnabled(False)
        self.edit_search_name.setObjectName("edit_search_name")
        self.layout_search_name.addWidget(self.edit_search_name)
        self.verticalLayout_3.addLayout(self.layout_search_name)
        self.button_search = QtWidgets.QPushButton(self.frame_search)
        self.button_search.setObjectName("button_search")
        self.verticalLayout_3.addWidget(self.button_search)
        self.verticalLayout_5.addWidget(self.frame_search)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.frame_visualise = QtWidgets.QFrame(self.centralwidget)
        self.frame_visualise.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_visualise.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_visualise.setLineWidth(13)
        self.frame_visualise.setObjectName("frame_visualise")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_visualise)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_complete = QtWidgets.QLabel(self.frame_visualise)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_complete.setFont(font)
        self.label_complete.setObjectName("label_complete")
        self.verticalLayout_4.addWidget(self.label_complete)
        self.layout_visualise_product = QtWidgets.QHBoxLayout()
        self.layout_visualise_product.setObjectName("layout_visualise_product")
        self.edit_visualise_product = QtWidgets.QLineEdit(self.frame_visualise)
        self.edit_visualise_product.setObjectName("edit_visualise_product")
        self.layout_visualise_product.addWidget(self.edit_visualise_product)
        self.button_visualise_product = QtWidgets.QPushButton(self.frame_visualise)
        self.button_visualise_product.setObjectName("button_visualise_product")
        self.layout_visualise_product.addWidget(self.button_visualise_product)
        self.verticalLayout_4.addLayout(self.layout_visualise_product)
        self.verticalLayout_5.addWidget(self.frame_visualise)
        spacerItem3 = QtWidgets.QSpacerItem(20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.frame_complete = QtWidgets.QFrame(self.centralwidget)
        self.frame_complete.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_complete.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_complete.setLineWidth(13)
        self.frame_complete.setObjectName("frame_complete")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_complete)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_complete_3 = QtWidgets.QLabel(self.frame_complete)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_complete_3.setFont(font)
        self.label_complete_3.setObjectName("label_complete_3")
        self.verticalLayout.addWidget(self.label_complete_3)
        self.button_treate_file = QtWidgets.QPushButton(self.frame_complete)
        self.button_treate_file.setEnabled(False)
        self.button_treate_file.setObjectName("button_treate_file")
        self.verticalLayout.addWidget(self.button_treate_file)
        self.verticalLayout_5.addWidget(self.frame_complete)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName("menubar")
        self.menu_phylogenie = QtWidgets.QMenu(self.menubar)
        self.menu_phylogenie.setObjectName("menu_phylogenie")
        MainWindow.setMenuBar(self.menubar)
        self.action_coraux = QtWidgets.QAction(MainWindow)
        self.action_coraux.setObjectName("action_coraux")
        self.actionHerbiers = QtWidgets.QAction(MainWindow)
        self.actionHerbiers.setObjectName("actionHerbiers")
        self.actionMangroves = QtWidgets.QAction(MainWindow)
        self.actionMangroves.setObjectName("actionMangroves")
        self.actionCoralligene = QtWidgets.QAction(MainWindow)
        self.actionCoralligene.setObjectName("actionCoralligene")
        self.menu_phylogenie.addAction(self.action_coraux)
        self.menu_phylogenie.addAction(self.actionHerbiers)
        self.menu_phylogenie.addAction(self.actionMangroves)
        self.menu_phylogenie.addAction(self.actionCoralligene)
        self.menubar.addAction(self.menu_phylogenie.menuAction())

        self.retranslateUi(MainWindow)
        self.checkbox_search_org.toggled['bool'].connect(self.edit_search_org.setEnabled)
        self.checkbox_search_name.toggled['bool'].connect(self.edit_search_name.setEnabled)
        self.checkbox_search_org.toggled['bool'].connect(self.button_search.setEnabled)
        self.checkbox_search_name.toggled['bool'].connect(self.button_search.setEnabled)
        self.button_download.clicked.connect(MainWindow.button_download_clicked)
        self.button_search.clicked.connect(MainWindow.button_search_clicked)
        self.button_visualise_product.clicked.connect(MainWindow.button_visualise_product_clicked)
        self.button_treate_file.clicked.connect(MainWindow.button_treate_file_clicked)
        self.checkbox_search_org.toggled['bool'].connect(self.combobox_search_org.setEnabled)
        self.menubar.triggered['QAction*'].connect(MainWindow.menu_phylogeny_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_download.setText(_translate("MainWindow", "TELECHARGER DES DONNEES"))
        self.label_database.setText(_translate("MainWindow", "Base de données NCBI :"))
        self.combobox_database.setItemText(0, _translate("MainWindow", "Nucleotide"))
        self.button_download.setText(_translate("MainWindow", "Accéder au moteur de recherche"))
        self.label_search.setText(_translate("MainWindow", "RECHERCHER DES DONNEES"))
        self.checkbox_search_org.setText(_translate("MainWindow", "Organisme :"))
        self.checkbox_search_name.setText(_translate("MainWindow", "Nom du gène  :"))
        self.button_search.setText(_translate("MainWindow", "Go"))
        self.label_complete.setText(_translate("MainWindow", "VISUALISER UN PRODUIT"))
        self.button_visualise_product.setText(_translate("MainWindow", "Go"))
        self.label_complete_3.setText(_translate("MainWindow", "COMPLETER LES DONNEES"))
        self.button_treate_file.setText(_translate("MainWindow", "Traiter un fichier Excel"))
        self.menu_phylogenie.setTitle(_translate("MainWindow", "Phylogenie"))
        self.action_coraux.setText(_translate("MainWindow", "Coraux"))
        self.actionHerbiers.setText(_translate("MainWindow", "Herbiers"))
        self.actionMangroves.setText(_translate("MainWindow", "Mangroves"))
        self.actionCoralligene.setText(_translate("MainWindow", "Coralligene"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
