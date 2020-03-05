from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
from objects.NCBI_Product import NCBI_Product
from objects.DB_Product import DB_Product
from graphic.product_view import Ui_MainWindow
from graphic.Application_Window import Application_Window
from other_files.useful_functions import *



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
        self.app_labels = []
        self._create_frame_app()
        self.window_application = None
        self.species_web_page = QWebEngineView()
        if self.existed:
            self._set_window()
            self._set_url()

    # METHODS OF THE CLASS #

    def app_button_modif_clicked(self):
        """Open the Application window"""
        self.window_application = Application_Window()
        self.window_application.show()

    def esp_button_open_clicked(self):
        """Open the IUCN RedList page of the species"""
        self.species_web_page.setUrl(self.url)
        self.species_web_page.showMaximized()

    # GRAPHIC METHODS #

    def _create_frame_app(self):
        """Create the QCheckBox for the different applications"""
        applications = get_all_applications_possibles()
        layout_box = QVBoxLayout()
        self.app_groupbox_checkboxes.setLayout(layout_box)
        for application in applications:
            label_app = QLabel()
            label_app.setText(application[0])
            layout_box.addWidget(label_app)
            self.app_labels.append(label_app)

    def _set_window(self):
        """Initialize the window"""
        self._set_labels()
        self._set_applications()
        internet = connected_to_internet("https://www.ncbi.nlm.nih.gov/")
        if internet["connected"]:
            self._set_fiche()
        else:
            self.edit_fiche.setPlainText("Aucune connexion a Internet !")

    def _set_labels(self):
        """Initialize the text of the QLabels with the information of the Product"""
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
        self.esp_label_famille_value.setText(self.product.organism.family)
        self.esp_label_ordre_value.setText(self.product.organism.order)
        self.esp_label_classe_value.setText(self.product.organism.classe)
        self.esp_label_statut_value.setText(self.product.organism.statut)

    def _set_applications(self):
        """Initialize the QCheckBox of the applications of the Product"""
        for application in self.product.applications:
            for label in self.app_labels:
                if application["nom_app"] == label.text():
                    text = label.text() + " (" + str(application["validite"]) + ")"
                    label.setText(text)
                    if application["validite"] == 1:
                        label.setStyleSheet('color:red')
                    elif application["validite"] == 2:
                        label.setStyleSheet('color:orange')
                    else:
                        label.setStyleSheet('font:bold;color:green')

    def _set_fiche(self):
        """Initialize the GenBank fiche"""
        protein = NCBI_Product(self.id)
        protein.save_genbank_file()
        text = open('fiche.txt').read()
        self.edit_fiche.setPlainText(text)

    def _set_url(self):
        """Initialize the url of the IUCN RedList page of the species"""
        species = self.product.organism.species.replace(" ", "%20").lower()
        url_text = 'https://www.iucnredlist.org/search?query={0}&searchType=species'.format(str(species))
        self.url = QUrl(url_text)

