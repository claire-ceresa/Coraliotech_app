# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excel_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 343)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_worksheet = QtWidgets.QHBoxLayout()
        self.layout_worksheet.setObjectName("layout_worksheet")
        self.checkbox_organism = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_organism.setObjectName("checkbox_organism")
        self.layout_worksheet.addWidget(self.checkbox_organism)
        self.label_worksheet = QtWidgets.QLabel(self.centralwidget)
        self.label_worksheet.setObjectName("label_worksheet")
        self.layout_worksheet.addWidget(self.label_worksheet)
        self.combobox_var_worksheet = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_var_worksheet.setEnabled(False)
        self.combobox_var_worksheet.setObjectName("combobox_var_worksheet")
        self.layout_worksheet.addWidget(self.combobox_var_worksheet)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_worksheet.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layout_worksheet)
        self.checkbox_product = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_product.setObjectName("checkbox_product")
        self.verticalLayout.addWidget(self.checkbox_product)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add = QtWidgets.QToolButton(self.centralwidget)
        self.button_add.setArrowType(QtCore.Qt.NoArrow)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(1)
        self.table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        self.table.horizontalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table)
        self.button_export = QtWidgets.QPushButton(self.centralwidget)
        self.button_export.setObjectName("button_export")
        self.verticalLayout.addWidget(self.button_export)
        self.label_created = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_created.setFont(font)
        self.label_created.setText("")
        self.label_created.setAlignment(QtCore.Qt.AlignCenter)
        self.label_created.setObjectName("label_created")
        self.verticalLayout.addWidget(self.label_created)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button_add.clicked.connect(MainWindow.button_add_clicked)
        self.button_export.clicked.connect(MainWindow.button_export_clicked)
        self.checkbox_organism.toggled['bool'].connect(self.combobox_var_worksheet.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkbox_organism.setText(_translate("MainWindow", "Diviser par rapport à l\'organisme"))
        self.label_worksheet.setText(_translate("MainWindow", "1 feuille par"))
        self.checkbox_product.setText(_translate("MainWindow", "Diviser par rapport au produits d\'interêt"))
        self.button_add.setText(_translate("MainWindow", "Ajouter une colonne"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        self.button_export.setText(_translate("MainWindow", "Exporter vers un fichier Excel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
