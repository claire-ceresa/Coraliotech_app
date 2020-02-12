from PyQt5.QtWidgets import QMessageBox


def create_messageBox(title, text):
    """create and execute a QMessageBox"""
    message = QMessageBox()
    message.setText(text)
    message.setWindowTitle(title)
    message.exec()
