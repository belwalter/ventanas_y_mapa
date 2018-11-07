
import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication

from ven_sec import Ventana_2

class Principal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("prueba.ui", self)
        self.setWindowTitle("nueva ventana")
        self.boton.clicked.connect(self.abrir)
        self.combo.currentIndexChanged.connect(self.completar)
        self.texto.textChanged.connect(self.escribir)
        self.show()

    def abrir(self):
        vent_2 = Ventana_2()
        vent_2.exec_()
        self.texto.setText(vent_2.lineEdit.text())

    def completar(self):
        self.texto.setText(self.combo.currentText())

    def escribir(self):
        self.textuno.append(self.texto.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
