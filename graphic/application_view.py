# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 152)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setObjectName("layout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.layout.addWidget(self.label)
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setMinimumSize(QtCore.QSize(101, 22))
        self.slider.setMaximumSize(QtCore.QSize(101, 22))
        self.slider.setMinimum(1)
        self.slider.setMaximum(3)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.layout.addWidget(self.slider)
        self.label_int = QtWidgets.QLabel(self.centralwidget)
        self.label_int.setObjectName("label_int")
        self.layout.addWidget(self.label_int)
        self.edit = QtWidgets.QLineEdit(self.centralwidget)
        self.edit.setObjectName("edit")
        self.layout.addWidget(self.edit)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.layout.addWidget(self.button)
        self.verticalLayout.addLayout(self.layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.slider.sliderMoved['int'].connect(self.label_int.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Modifier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
