from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from objects.NCBI_Product import NCBI_Product
from objects.DB_Product import DB_Product
from graphic.product_view import Ui_MainWindow
from graphic.Application_Window import Application_Window
from database.functions_db import *



class Product_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for the product_view
    """
    def __init__(self, parent=None, id=None):
        super(Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(id)
        self.id = id
        self.product = DB_Product(id=self.id)
        self.existed = self.product.existed
        self.app_checkboxes = []
        self.create_frame_app()
        self.window_application = None
        if self.existed:
            self.set_window()
            self.set_url()

    # METHODS OF THE CLASS #

    def app_button_modif_clicked(self):
        self.window_application = Application_Window()
        self.window_application.show()

    def esp_button_open_clicked(self):
        self.species_web_page.load(self.url)
        self.species_web_page.showMaximized()


    # GRAPHIC METHODS #

    def create_frame_app(self):
        """create the checkboxes for the applications"""
        applications = get_all_applications_possibles()
        layout = QVBoxLayout()
        self.app_groupbox_checkboxes.setLayout(layout)
        for application in applications:
            checkbox = QCheckBox()
            checkbox.setText(application[0])
            layout.addWidget(checkbox)
            self.app_checkboxes.append(checkbox)

    def set_window(self):
        """initialize the window"""
        self.set_labels()
        self.set_fiche()
        self.set_applications()

    def set_labels(self):
        """initialize the characteristics of the label"""
        self.prod_label_name.setText(self.product.name)
        self.prod_label_source.setText(self.product.source)
        self.prod_label_id.setText(self.product.id)
        text_cds = str(self.product.cds.start) + "-" + str(self.product.cds.stop)
        self.prod_label_cds_value.setText(text_cds)
        self.prod_label_length_value.setText(str(self.product.cds.length) + " pb")
        self.prod_label_weight_value.setText(str(self.product.cds.mw) + " kD")
        if self.product.cds.complete == 0:
            self.prod_label_complete_value.setText("non")
            self.prod_label_complete_value.setStyleSheet('color:red')
        else:
            self.prod_label_complete_value.setText("oui")
        if self.product.predicted == 0:
            self.prod_label_pred_value.setText("non")
        else:
            self.prod_label_pred_value.setText("oui")
            self.prod_label_pred_value.setStyleSheet('color:red')
        self.prod_edit_note.setPlainText(self.product.note)
        self.esp_label_name.setText(self.product.organism.species)

    def set_applications(self):
        """initialize the applications of the product"""
        for application in self.product.applications:
            for checkbox in self.app_checkboxes:
                if application["nom_app"] == checkbox.text():
                    checkbox.setChecked(True)
                    checkbox.setStyleSheet('font:bold')

    def set_fiche(self):
        """initialize the GenBank fiche"""
        protein = NCBI_Product(self.id)
        protein.save_genbank_file()
        text = open('fiche.txt').read()
        self.edit_fiche.setPlainText(text)

    def set_url(self):
        """initialize the url of the website IUCN Red List"""
        species = self.product.organism.species.replace(" ", "%20")
        self.url = QUrl("https://www.iucnredlist.org/search?query=" + species.lower() + "&searchType=species")
