import xlsxwriter as x
from PyQt5.QtWidgets import *
from graphic.search_view import *
from graphic.Product_Window import Product_Window


class Search_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for principal_view
    """
    def __init__(self, parent=None, search=None):
        super(Search_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Resultat de la recherche")
        self.search = search
        self.window_product = None
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
        name = QFileDialog.getSaveFileName(self, 'Enregister', "", "Excel (*.xls *.xlsx)")
        print(name[0])

    def _set_window(self):
        print("ok set")
        nb_result = str(len(self.search.results))
        text = nb_result + " resultats trouves !"
        self.label_result.setText(text)
        print("finish")

    def _set_table(self):
        self.table_result.setRowCount(len(self.search.results))
        self.table_result.setColumnCount(5)
        self._set_headers()
        # for product in self.search.results:
        #     print(product)
        #     for column, value in enumerate(result.values()):
        #         item = QTableWidgetItem(str(value))
        #         self.table_result.setItem(line, column, item)

    def _set_headers(self):
        column_names = ["Identifiant", "Nom", "Espece", "Source", "Predicted"]
        for column, column_name in enumerate(column_names):
            header = QTableWidgetItem(column_name)
            self.table_result.setHorizontalHeaderItem(column, header)
