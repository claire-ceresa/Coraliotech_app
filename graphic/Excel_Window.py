from PyQt5.QtWidgets import *
from graphic.excel_view import *
from objects.Excel import Excel


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
        combo = QComboBox()
        self.table.setCellWidget(0,column,combo)
