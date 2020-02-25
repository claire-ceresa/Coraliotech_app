from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class WisdomCompositeWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.qtreewidget = QtWidgets.QTreeWidget()
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.qtreewidget)
        self.setLayout(vbox)

        self.qtreewidget.setColumnCount(2)
        self.qtreewidget.setHeaderLabels(["Wisdom"])
        self.qtreewidget.setItemsExpandable(True)



        ref = self.qtreewidget
        growth_qtwi = QtWidgets.QTreeWidgetItem(ref, ["Growth"])

        ref = growth_qtwi
        growth_faith_qtwi = QtWidgets.QTreeWidgetItem(ref, ["Faith"])

        growth_virtue_qtwi = QtWidgets.QTreeWidgetItem(ref, ["Virtue"])

        ref = growth_faith_qtwi
        QtWidgets.QTreeWidgetItem(ref, ["Not to kill"])
        QtWidgets.QTreeWidgetItem(ref, ["Not to steal"])
        QtWidgets.QTreeWidgetItem(ref, ["Avoiding sexual misconduct"])
        QtWidgets.QTreeWidgetItem(ref, ["Not to lie"])
        QtWidgets.QTreeWidgetItem(ref, ["Avoiding intoxicants"])

        ref = growth_qtwi
        growth_generosity_qtwi = QtWidgets.QTreeWidgetItem(ref, ["Generosity"])

        growth_wisdom_qtwi = QtWidgets.QTreeWidgetItem(ref, ["Wisdom"])

        ref = growth_wisdom_qtwi
        QtWidgets.QTreeWidgetItem(ref, ["Wants to see monks"])
        QtWidgets.QTreeWidgetItem(ref, ["Wants to hear the good Dharma"])
        QtWidgets.QTreeWidgetItem(ref, ["Retains in mind the teachings he has heard"])
        QtWidgets.QTreeWidgetItem(ref,
            ["Examines the meaning of the teachings that have been retained in mind"])
        QtWidgets.QTreeWidgetItem(ref,
            ["Understands the meaning of the Dharma and then practices in accordance with the Dharma"])

