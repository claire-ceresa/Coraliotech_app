import operator
import os
from PyQt5.QtWidgets import *
from other_files.useful_functions import *
from graphic.excel_view import *
from objects.DB_Product import DB_Product
from objects.DB_Organism import DB_Organism
from objects.Excel import Excel


class Excel_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for excel_view
    """

    # Table of the correspondance between the attribute name in Python and their name seen on the IG
    corresp_var_colname = {
        'id': 'Identifiant GenBank',
        'name': 'Nom du produit',
        'predicted': 'Predit',
        'existed': 'Existant',
        'source': 'Source',
        'note': 'Note',
        'fonction': 'Fonction theorique',
        'applications': 'Applications',
        'organism.species': 'Espece',
        'organism.genus': 'Genre',
        'organism.family': 'Famille',
        'organism.order': 'Ordre',
        'organism.subclass': 'Sous-classe',
        'organism.classe': 'Classe',
        'organism.phylum': 'Embranchement',
        'organism.statut': 'Statut IUCN',
        'cds.id': 'Identifiant CDS',
        'cds.start': 'Debut CDS',
        'cds.stop': 'Fin CDS',
        'cds.length': 'Taille CDS (pb)',
        'cds.mw': 'PM theorique (kD)',
        'cds.complete': 'CDS complet',
        'cds.seqADN': 'Sequence',
        'url': 'URL'
    }

    def __init__(self, parent=None, datas_raw=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.datas_raw = datas_raw
        self.setWindowTitle("Creation d'un fichier Excel")
        self._create_cell_combobox(column=0)
        self._fill_in_combobox_worksheet()

    # METHODS OF THE CLASS #

    def button_add_clicked(self):
        """Add a column to the table"""
        count = self.table.columnCount()
        self.table.setColumnCount(count + 1)
        self._create_cell_combobox(column=count)

    def button_export_clicked(self):
        """Create the Excel file and export the datas"""
        datas_to_export = self._get_datas()
        desktop_path = os.environ['USERPROFILE'] + '\Desktop\\'
        name = QFileDialog.getSaveFileName(self, 'Enregister', desktop_path, "Excel (*.xlsx)")
        filename = name[0]

        if len(filename) > 0:
            exportation = self._export_datas(filename, datas_to_export)
            if exportation["done"]:
                message = "Le fichier a bien ete cree !"
            else:
                message = "Un probleme est survenu. Le fichier n'a pas ete cree !\n" + str(exportation["error"])
            self.label_created.setText(message)

    # GRAPHIC METHODS #

    def _create_cell_combobox(self, column):
        """Create a QComboBox in the header cell"""
        attributes = DB_Product().get_all_attributes()
        combo = QComboBox()
        combo.addItem("")

        for attribute in attributes:
            if attribute in self.corresp_var_colname:
                combo.addItem(self.corresp_var_colname[attribute])
            else:
                combo.addItem(attribute)

        combo.addItem("URL")
        self.table.setCellWidget(0, column, combo)
        self.table.resizeColumnsToContents()

    def _fill_in_combobox_worksheet(self):
        """Fill in the QComboBox of the variables to divide the workbook"""
        variables = DB_Organism().get_all_attributes()
        for variable in variables:
            name = self.corresp_var_colname["organism." + variable]
            self.combobox_var_worksheet.addItem(name)

    # OTHER FUNCTIONS #

    def _get_datas(self):
        """
        Get the data to export
        :return a dictionnary {'lists':[], 'values':[]}
        lists = a list of sub-lists of the datas
        values = the value of the attribute for each sublist or None
        """
        if self.checkbox_organism.isChecked():
            text = self.combobox_var_worksheet.currentText()
            variable_chosen = get_key(self.corresp_var_colname, text)
            datas_sorted = sorted(self.datas_raw, key=operator.attrgetter(variable_chosen))
            datas_to_export = split_list_of_product(datas_sorted, variable_chosen)

        elif self.checkbox_product.isChecked():
            datas_to_export = split_list_of_product(self.datas_raw, "name")

        else:
            datas_to_export = {"lists": [self.datas_raw], "values": [None]}

        return datas_to_export

    def _formate_datas(self, datas):
        """
        Formate the data to export them
        :param datas : a list of Products
        :return a dictionnary {'column_names':[], 'rows':[]}
        column_names = a list of the names of the columns
        rows = a list of list corresponding to each row
        """
        datas_formatted = {}
        datas_formatted["rows"] = []
        variables = []
        headers = []
        nb_columns = self.table.columnCount()

        for column in range(0, nb_columns):
            item = self.table.cellWidget(0, column)
            variable_name = item.currentText()
            variable = get_key(self.corresp_var_colname, variable_name)
            variables.append(variable)

            if variable == "applications":
                applications = get_all("Applications_possibles", "nom")
                for app_name in applications:
                    headers.append(app_name.upper())

            else:
                try:
                    text = self.corresp_var_colname[variable]
                except KeyError:
                    text = variable if variable is not None else ""
                headers.append(text.upper())

        datas_formatted["column_names"] = headers

        for product in datas:
            row = []
            for column in variables:
                if column is None:
                    row.append("")

                elif column == "url":
                    organism = getattr(product, "organism")
                    species = getattr(organism, "species")
                    row.append("https://www.iucnredlist.org/search?query=" + species.replace(" ",
                                                                                             "%20").lower() + "&searchType=species")

                elif column == "applications":
                    applications = getattr(product,"applications")
                    for application in applications:
                        row.append(application.validity)

                else:
                    attributes = column.split(".")
                    if len(attributes) > 1:
                        object = getattr(product, attributes[0])
                        value = getattr(object, attributes[1])
                        row.append(value)
                    else:
                        row.append(getattr(product, column))
            datas_formatted["rows"].append(row)

        return datas_formatted

    def _export_datas(self, filename, datas):
        """
        Export the datas
        :param filename: the name of the Excel file where the datas are saved
        :param datas: a dictionnary {'lists':[], 'values':[]}
        :return: a dictionnary {'done':bool, 'error':string}
        """
        try:
            file = Excel(filename)
            for index, data_to_export in enumerate(datas["lists"]):
                title = "  " if datas["values"][index] is None else datas["values"][index]
                worksheet = file.add_worksheet(title=title)
                datas_formatted = self._formate_datas(data_to_export)
                file.add_data(worksheet=worksheet, datas=datas_formatted)
            file.close()
            return {'done': True, 'error': None}
        except Exception as e:
            return {'done': False, 'error': str(e)}
