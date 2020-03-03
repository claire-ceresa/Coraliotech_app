from pandas import DataFrame
from openpyxl import load_workbook
from PyQt5.QtWidgets import *
from graphic.phylogeny_view import *
from database.functions_db import *


class Phylogeny_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for phylogeny_view
    """
    def __init__(self, parent=None, group=None):
        super(Phylogeny_Window, self).__init__(parent)
        self.setupUi(self)
        self.group = group
        self.setWindowTitle(self.group)
        self._fill_in_tree()

    def _fill_in_tree(self):
        """ Fill in the QTreeWidget with all the phylogeny"""
        datas = self._read_file()

        ref_items = [self.treeWidget, None, None, None]
        ref_col = 0

        for row, row_data in datas.iterrows():
            if row == 0:
                rangs = row_data
                smallest = row_data[len(row_data)-1]
                saved = get_all("Organisme", smallest)
            else:
                for column, data in enumerate(row_data):
                    if data is not None:

                        if column == ref_col:
                            item = QTreeWidgetItem(ref_items[column])

                        elif column > ref_col:
                            ref_items[column] = item
                            item = QTreeWidgetItem(ref_items[column])
                            ref_col = column

                        else:
                            item = QTreeWidgetItem(ref_items[column])
                            ref_col = column

                        item.setText(0, data)
                        item.setText(1, rangs[column])

                        if data in saved:
                            font = QtGui.QFont()
                            font.setBold(True)
                            item.setFont(0,font)

    def _read_file(self):
        """
        Open and read the phylogeny Exce file
        :return a pandas DataFrame of the values
        """
        workbook = load_workbook(filename="other_files\phylogeny.xlsx")
        worksheet = workbook[self.group]
        datas = DataFrame(worksheet.values)
        return datas

