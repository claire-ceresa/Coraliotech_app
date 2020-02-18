from PyQt5.QtWidgets import *
from graphic.excel_view import *
from objects.DB_Product import DB_Product
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
    }

    def __init__(self, parent=None, datas_raw=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.datas_raw = datas_raw
        self.setWindowTitle("Creation d'un fichier Excel")
        self._create_cell_combobox(column=0)

    def button_add_clicked(self):
        count = self.table.columnCount()
        self.table.setColumnCount(count+1)
        self._create_cell_combobox(column=count)

    def button_export_clicked(self):
        name = QFileDialog.getSaveFileName(self, 'Enregister', "", "Excel (*.xlsx)")
        file = Excel(name[0])
        worksheet = file.add_worksheet()
        datas = self._formate_datas()
        file.add_data(worksheet=worksheet, datas=datas)
        file.close()

    def _formate_datas(self):
        datas = []

        variables = []
        headers = []
        nb_columns = self.table.columnCount()
        for column in range(0, nb_columns):
            item = self.table.cellWidget(0,column)
            variable = item.currentText()
            variables.append(variable)
            try:
                text = self.corresp_var_colname[variable]
            except KeyError:
                text = variable
            headers.append(text)
        datas.append(headers)

        for product in self.datas_raw:
            row = []
            for column in variables:
                attributes = column.split(".")
                if len(attributes) > 1:
                    object = getattr(product, attributes[0])
                    value = getattr(object, attributes[1])
                    row.append(value)
                else:
                    row.append(getattr(product, column))
            datas.append(row)

        return datas

    def _create_cell_combobox(self, column):
        attributes = DB_Product().get_attributes()
        combo = QComboBox()
        for attribute in attributes:
            combo.addItem(attribute)
        self.table.setCellWidget(0, column, combo)
        self.table.resizeColumnsToContents()
