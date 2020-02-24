from PyQt5.QtWidgets import *
from graphic.application_view import Ui_MainWindow


class Application_Window(QMainWindow, Ui_MainWindow):
    """
    controlling class for the product_view
    """
    def __init__(self, parent=None):
        super(Application_Window, self).__init__(parent)
        self.setupUi(self)


