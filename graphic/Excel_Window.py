from PyQt5.QtWidgets import *
from graphic.excel_view import *
from objects.DB_Product import DB_Product


class Excel_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for excel_view
    """
    def __init__(self, parent=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Creation d'un fichier Excel")
        self._create_cell_combobox(column=0)

    def button_clicked(self):
        count = self.table.columnCount()
        self.table.setColumnCount(count+1)
        self._create_cell_combobox(column=count)

    def _create_cell_combobox(self, column):
        attributes = DB_Product().get_attributes()
        combo = QComboBox()
        for attribute in attributes:
            combo.addItem(attribute)
        self.table.setCellWidget(0, column, combo)
        self.table.resizeColumnsToContents()
