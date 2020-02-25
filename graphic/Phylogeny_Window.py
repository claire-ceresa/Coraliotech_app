from pandas import DataFrame
from openpyxl import load_workbook
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
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
        self.fill_in_tree()


    def fill_in_tree(self):
        datas = self.read_file()
        saved_families = get_all_families()

        ref_items = [self.treeWidget, None, None, None]
        ref_col = 0

        for row, row_data in datas.iterrows():
            if row == 0:
                rangs = row_data
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

                        if data in saved_families:
                            font = QtGui.QFont()
                            font.setBold(True)
                            item.setFont(0,font)



    def read_file(self):
        """open and read the phylogeny datas of the ile"""
        workbook = load_workbook(filename="other_files\phylogeny.xlsx")
        worksheet = workbook[self.group]
        datas = DataFrame(worksheet.values)
        return datas

