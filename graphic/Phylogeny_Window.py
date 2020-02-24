from pandas import DataFrame
from openpyxl import load_workbook
from PyQt5.QtWidgets import *
from graphic.phylogeny_view import *


class Phylogeny_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for principal_view
    """
    def __init__(self, parent=None, group=None):
        super(Phylogeny_Window, self).__init__(parent)
        self.setupUi(self)
        self.group = group
        self.setWindowTitle(self.group)
        self.fill_in_tree()

    def fill_in_tree(self):
        datas = self.read_file()
        strings = ["Anthozoa", "Scleractinia"]
        try:
            l = []  # list of QTreeWidgetItem to add
            for i in strings:
                l.append(QTreeWidgetItem(i))  # create QTreeWidgetItem's and append them

                self.treeWidget.addTopLevelItems(l)  # add everything to the tree
        except Exception as e:
            print(e)

    def read_file(self):
        workbook = load_workbook(filename="other_files\phylogeny.xlsx")
        worksheet = workbook[self.group]
        datas = DataFrame(worksheet.values)
        return datas

