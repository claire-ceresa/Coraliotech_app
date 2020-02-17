# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 479)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.table_result = QtWidgets.QTableWidget(self.centralwidget)
        self.table_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_result.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_result.setObjectName("table_result")
        self.table_result.setColumnCount(0)
        self.table_result.setRowCount(0)
        self.verticalLayout.addWidget(self.table_result)
        self.button_export = QtWidgets.QPushButton(self.centralwidget)
        self.button_export.setObjectName("button_export")
        self.verticalLayout.addWidget(self.button_export)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.table_result.itemDoubleClicked['QTableWidgetItem*'].connect(MainWindow.table_item_clicked)
        self.button_export.clicked.connect(MainWindow.button_export_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.table_result.setSortingEnabled(True)
        self.button_export.setText(_translate("MainWindow", "Exporter en csv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
