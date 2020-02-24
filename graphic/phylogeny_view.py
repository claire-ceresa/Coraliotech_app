# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phylogeny.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 307)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        self.verticalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Nom"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Rang"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Anthozoa"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "Classe"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Hexacorallia"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "Sous classe"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "Scleractinia"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(1, _translate("MainWindow", "Ordre"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).setText(0, _translate("MainWindow", "Pocilloporidae"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).setText(1, _translate("MainWindow", "Famille"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
