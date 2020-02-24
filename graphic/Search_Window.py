from PyQt5.QtWidgets import *
from graphic.search_view import *
from graphic.Product_Window import Product_Window
from graphic.Excel_Window import Excel_Window
from objects.Excel import Excel


class Search_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for search_view
    """
    def __init__(self, parent=None, search=None):
        super(Search_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Resultats de la recherche")
        self.search = search
        self.window_product = None
        self.window_personnalise = None
        self.columns = [{"name":"Identifiant GenBank", "attribute":"id"},
                        {"name":"Nom du produit", "attribute":"name"},
                        {"name":"Espece", "attribute":"organism"},
                        {"name":"Source", "attribute":"source"},
                        {"name":"Predit", "attribute":"predicted"}]
        self._set_window()
        if len(self.search.results) > 0:
            self._set_table()

    def table_item_clicked(self):
        """open the Product window"""
        row = self.table_result.currentRow()
        item = self.table_result.item(row, 0)
        id = item.text()
        self.window_product = Product_Window(id=id)
        self.window_product.show()

    def button_export_clicked(self):
        """export the table without modif"""
        name = QFileDialog.getSaveFileName(self, 'Enregister', "", "Excel (*.xlsx)")
        if len(name[0]) > 0:
            file = Excel(name[0])
            worksheet = file.add_worksheet()
            file.add_QTableWidget(self.table_result, worksheet)
            file.close()

    def button_personnalise_clicked(self):
        """open the window to export to a personnalised file"""
        self.window_personnalise = Excel_Window(datas_raw=self.search.results)
        self.window_personnalise.show()

    def _set_window(self):
        """print the number of results"""
        nb_result = str(len(self.search.results))
        text = nb_result + " resultats trouves !"
        self.label_result.setText(text)

    def _set_table(self):
        """set the QTableWidget"""
        self.table_result.setRowCount(len(self.search.results))
        self.table_result.setColumnCount(5)
        self._set_headers()
        self._fill_in_table()

    def _set_headers(self):
        for position, column in enumerate(self.columns):
            header = QTableWidgetItem(column["name"])
            self.table_result.setHorizontalHeaderItem(position, header)

    def _fill_in_table(self):
        for num_line, product in enumerate(self.search.results):
            for num_col, column in enumerate(self.columns):
                if column['attribute'] == 'organism':
                    organism = getattr(product, column['attribute'])
                    value = getattr(organism, 'species')
                else:
                    value = getattr(product, column['attribute'])
                item = QTableWidgetItem(str(value))
                self.table_result.setItem(num_line, num_col, item)

