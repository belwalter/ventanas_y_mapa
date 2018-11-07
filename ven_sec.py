
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class Ventana_2(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("ventana2.ui", self)
