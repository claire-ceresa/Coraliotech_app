from PyQt5 import QtWidgets, QtCore, QtGui
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
        for app_name in self.widgets_applications:

            old_value = self.widgets_applications[app_name]["object"].validity
            new_value = self.widgets_applications[app_name]["slider"].value()
            id = self.widgets_applications[app_name]["object"].id
            text_remarque = self.widgets_applications[app_name]["edit"].text()
            if len(text_remarque) > 0:
                remarque = "\"" + text_remarque + "\""
            else:
                remarque = "NULL"

            if old_value != new_value and old_value is not None:
                modif = modif_application(id=id, name_app=app_name, validite=new_value, remarque=remarque)
                if modif["commited"]:
                    text = self.label_modified.text() + "\nModification effectuée pour " + app_name + " : " + str(
                        old_value) + " -> " + str(new_value)
                else:
                    text = self.label_modified.text() + "\nErreur pour " + app_name + " : " + modif["error"]
                self.label_modified.setText(text)

            elif old_value != new_value and old_value is None:
                datas_to_insert = {'id_produit':"\"" + id + "\"",
                                   "nom_app": "\"" + app_name + "\"",
                                   'validite':str(new_value),
                                   'remarque':remarque}
                query = get_query_insert("Applications", datas_to_insert)
                insert = commit_query(query)
                if insert["commited"]:
                    text = self.label_modified.text() + "\nModification effectuée pour "+ app_name + " : " + str(new_value)
                else:
                    text = self.label_modified.text() + "\nErreur pour " + app_name + " : " + modif["error"]
                self.label_modified.setText(text)

            else:
                continue

    def slider_changed(self, application_name):
        label_int = self.widgets_applications[application_name]["label_int"]
        slider = self.widgets_applications[application_name]["slider"]
        slider_value = slider.value()
        label_int.setText(str(slider_value))
        if slider_value == 1:
            label_int.setStyleSheet('font:bold;color:red')
        elif slider_value == 2:
            label_int.setStyleSheet('font:bold;color:orange')
        else:
            label_int.setStyleSheet('font:bold;color:green')
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        label_int.setFont(font)

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
                remarque = self.widgets_applications[app_name]["object"].remark
                edit = self.widgets_applications[app_name]["edit"]
                edit.setText(remarque)

    def _create_window(self):
        for application in self.data_applications:
            self._create_application(application)
        self._create_button()

    def _create_application(self, application):
        self.widgets_applications[application.name_app] = {}
        self.widgets_applications[application.name_app]["object"] = application

        layout = QtWidgets.QHBoxLayout()
        layout.setObjectName("layout_" + application.name_app.lower())
        label = QtWidgets.QLabel(self.centralwidget)
        label.setText("")
        label.setObjectName("label_" + application.name_app.lower())
        label.setText(application.name_app)
        layout.addWidget(label)
        slider = QtWidgets.QSlider(self.centralwidget)
        slider.setMinimumSize(QtCore.QSize(101, 22))
        slider.setMaximumSize(QtCore.QSize(101, 22))
        slider.setMinimum(1)
        slider.setMaximum(3)
        slider.setOrientation(QtCore.Qt.Horizontal)
        layout.addWidget(slider)
        label_int = QtWidgets.QLabel(self.centralwidget)
        label_int.setObjectName("label_int_" + application.name_app.lower())
        label_int.setText("1")
        layout.addWidget(label_int)
        edit = QtWidgets.QLineEdit(self.centralwidget)
        edit.setObjectName("edit_" + application.name_app.lower())
        layout.addWidget(edit)
        self.verticalLayout.addLayout(layout)
        slider.valueChanged['int'].connect(lambda widget=slider: self.slider_changed(application.name_app))

        self.widgets_applications[application.name_app]["label"] = label
        self.widgets_applications[application.name_app]["slider"] = slider
        self.widgets_applications[application.name_app]["label_int"] = label_int
        self.widgets_applications[application.name_app]["edit"] = edit

    def _create_button(self):
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.button.setText("Modifier")
        self.verticalLayout.addWidget(self.button)
        self.button.clicked.connect(self.button_modif_clicked)
        self.label_modified = QtWidgets.QLabel(self.centralwidget)
        self.label_modified.setObjectName("label_modified")
        self.label_modified.setText("")
        self.verticalLayout.addWidget(self.label_modified)





