import xlsxwriter as x
from PyQt5.QtWidgets import *
from graphic.search_view import *
from graphic.Product_Window import Product_Window
from objects.Excel import Excel


class Search_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for principal_view
    """
    def __init__(self, parent=None, search=None):
        super(Search_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Resultats de la recherche")
        self.search = search
        self.window_product = None
        self.columns = [{"name":"Identifiant", "attribute":"id"},
                        {"name":"Nom", "attribute":"name"},
                        {"name":"Espece", "attribute":"species"},
                        {"name":"Source", "attribute":"source"},
                        {"name":"Predicted", "attribute":"predicted"}]
        self._set_window()
        if len(self.search.results) > 0:
            self._set_table()

    def table_item_clicked(self):
        row = self.table_result.currentRow()
        item = self.table_result.item(row, 0)
        id = item.text()
        self.window_product = Product_Window(id=id)
        self.window_product.show()

    def button_export_clicked(self):
        name = QFileDialog.getSaveFileName(self, 'Enregister', "", "Excel (*.xlsx)")
        file = Excel(name[0])
        worksheet = file.add_worksheet()
        file.add_QTableWidget(self.table_result, worksheet)
        file.close()

    def _set_window(self):
        nb_result = str(len(self.search.results))
        text = nb_result + " resultats trouves !"
        self.label_result.setText(text)

    def _set_table(self):
        self.table_result.setRowCount(len(self.search.results))
        self.table_result.setColumnCount(5)
        self._set_headers()
        self._fill_in_table()

    def _fill_in_table(self):
        for num_line, product in enumerate(self.search.results):
            for num_col, column in enumerate(self.columns):
                value = getattr(product, column['attribute'])
                item = QTableWidgetItem(str(value))
                self.table_result.setItem(num_line, num_col, item)

    def _set_headers(self):
        for position, column in enumerate(self.columns):
            header = QTableWidgetItem(column["name"])
            self.table_result.setHorizontalHeaderItem(position, header)
