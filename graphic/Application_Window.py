from PyQt5 import QtWidgets, QtCore
from graphic.application_view import Ui_MainWindow
from database.functions_db import *

class Application_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    controlling class for the application_view
    """
    # KJ766310.1 datas
    # KJ780789.1 vide

    def __init__(self, parent=None, applications=None, id=None):
        super(Application_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des applications")
        self.data_applications = applications
        self.widgets_applications = {}
        self.id = id
        self._create_window()
        self._set_window()

    # CLASS METHODS #

    def button_modif_clicked(self):
        print("ok")

    # GRAPHIC METHODS #

    def _set_window(self):
        for app_name in self.widgets_applications:
            slider = self.widgets_applications[app_name]["slider"]
            label_int = self.widgets_applications[app_name]["label_int"]
            validity = self.widgets_applications[app_name]["object"].validity
            if validity is not None:
                slider.setValue(validity)
                if validity == 1:
                    label_int.setStyleSheet('font:bold;color:red')
                elif validity == 2:
                    label_int.setStyleSheet('font:bold;color:orange')
                else:
                    label_int.setStyleSheet('font:bold;color:green')


    def _create_window(self):
        for application in self.data_applications:
            self._create_application(application)
        self._create_button()

    def _create_application(self, application):
        self.widgets_applications[application.name_app] = {}
        self.widgets_applications[application.name_app]["object"] = application

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setObjectName("layout_" + application.name_app.lower())
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label_" + application.name_app.lower())
        self.label.setText(application.name_app)
        self.layout.addWidget(self.label)
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setMinimumSize(QtCore.QSize(101, 22))
        self.slider.setMaximumSize(QtCore.QSize(101, 22))
        self.slider.setMinimum(1)
        self.slider.setMaximum(3)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.layout.addWidget(self.slider)
        self.label_int = QtWidgets.QLabel(self.centralwidget)
        self.label_int.setObjectName("label_int_" + application.name_app.lower())
        self.label_int.setText("1")
        self.layout.addWidget(self.label_int)
        self.edit = QtWidgets.QLineEdit(self.centralwidget)
        self.edit.setObjectName("edit_" + application.name_app.lower())
        self.layout.addWidget(self.edit)
        self.verticalLayout.addLayout(self.layout)
        self.slider.valueChanged['int'].connect(self.label_int.setNum)

        self.widgets_applications[application.name_app]["label"] = self.label
        self.widgets_applications[application.name_app]["slider"] = self.slider
        self.widgets_applications[application.name_app]["label_int"] = self.label_int
        self.widgets_applications[application.name_app]["edit"] = self.edit

    def _create_button(self):
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.button.setText("Modifier")
        self.verticalLayout.addWidget(self.button)
        self.button.clicked.connect(self.button_modif_clicked)





