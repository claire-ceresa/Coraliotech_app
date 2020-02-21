import operator
from PyQt5.QtWidgets import *
from useful_functions import *
from graphic.excel_view import *
from objects.DB_Product import DB_Product
from objects.DB_Organism import DB_Organism
from objects.Excel import Excel

class Excel_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for excel_view
    """

    corresp_var_colname = {
        'id':'Identifiant GenBank',
        'name':'Nom du produit',
        'predicted':'Predit',
        'existed':'Existant',
        'source':'Source',
        'note':'Note',
        'fonction':'Fonction theorique',
        'applications':'Applications',
        'organism.species':'Espece',
        'organism.genus':'Genre',
        'organism.family':'Famille',
        'organism.order':'Ordre',
        'organism.subclass':'Sous-classe',
        'organism.classe':'Classe',
        'organism.phylum':'Embranchement',
        'organism.statut': 'Statut IUCN',
        'cds.id' : 'Identifiant CDS',
        'cds.start' : 'Debut CDS',
        'cds.stop' : 'Fin CDS',
        'cds.length' : 'Taille CDS (pb)',
        'cds.mw' : 'PM theorique (kD)',
        'cds.complete' : 'CDS complet',
        'cds.seqADN' : 'Sequence'
    }

    def __init__(self, parent=None, datas_raw=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.datas_raw = datas_raw
        self.setWindowTitle("Creation d'un fichier Excel")
        self._create_cell_combobox(column=0)
        self._fill_in_combobox_worksheet()

    def button_add_clicked(self):
        count = self.table.columnCount()
        self.table.setColumnCount(count+1)
        self._create_cell_combobox(column=count)

    def button_export_clicked(self):
        if self.checkbox_worksheet.isChecked():
            text = self.combobox_var_worksheet.currentText()
            variable_chosen = get_key(self.corresp_var_colname, text)
            datas_sorted = sorted(self.datas_raw, key=operator.attrgetter(variable_chosen))
            datas_to_export = split_list_of_product(datas_sorted, variable_chosen)
        else:
            datas_to_export = [self.datas_raw]

        try:
            name = QFileDialog.getSaveFileName(self, 'Enregister', "", "Excel (*.xlsx)")
            file = Excel(name[0])
            for data_to_export in datas_to_export:
                worksheet = file.add_worksheet()
                datas = self._formate_datas(data_to_export)
                file.add_data(worksheet=worksheet, datas=datas)
            file.close()
            message = "Le fichier a bien ete cree !"
        except Exception as e:
            message = "Un probleme est survenu. Le fichier n'a pas ete cree !\n"
            message = message + str(e)

        self.label_created.setText(message)

    ## GRAPHIC METHODS ##

    def _create_cell_combobox(self, column):
        attributes = DB_Product().get_all_attributes()
        combo = QComboBox()
        for attribute in attributes:
            if attribute in self.corresp_var_colname:
                combo.addItem(self.corresp_var_colname[attribute])
            else:
                combo.addItem(attribute)
        self.table.setCellWidget(0, column, combo)
        self.table.resizeColumnsToContents()

    def _fill_in_combobox_worksheet(self):
        variables = DB_Organism().get_all_attributes()
        for variable in variables:
            name = self.corresp_var_colname["organism."+variable]
            self.combobox_var_worksheet.addItem(name)

    ## OTHER FUNCTIONS ##

    def _formate_datas(self, datas):
        datas_formatted = []

        variables = []
        headers = []
        nb_columns = self.table.columnCount()
        for column in range(0, nb_columns):
            item = self.table.cellWidget(0,column)
            variable_name = item.currentText()
            variable = get_key(self.corresp_var_colname, variable_name)
            variables.append(variable)
            try:
                text = self.corresp_var_colname[variable]
            except KeyError:
                text = variable
            headers.append(text)
        datas_formatted.append(headers)

        for product in datas:
            row = []
            for column in variables:
                attributes = column.split(".")
                if len(attributes) > 1:
                    object = getattr(product, attributes[0])
                    value = getattr(object, attributes[1])
                    row.append(value)
                else:
                    row.append(getattr(product, column))
            datas_formatted.append(row)

        return datas_formatted


