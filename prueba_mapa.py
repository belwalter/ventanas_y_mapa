
import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MapaUrl():

    def __init__(self):
        self.centro = "ecuador"
        self.zoom = "&zoom=1"
        self.size = "&size=500x500"
        self.formato = "&formato=png"
        self.maptype = "&maptype=roadmap"
        self.marcadores = "" #"&markers=color:green|label:M|-32.4818434,-58.2391088|-32.4829361,-58.2398935"
        self.marcadores2 = "" #"&markers=color:purple|label:J|concepcion del uruguay"
        self.path = ""
        self.path2 = ""
        self.api_key = "&key=AIzaSyAJ2aEs0UpGAW-G4mleFU6nasD6U1RkfT0"

    def get_url(self):
        parametros = self.centro + self.zoom + self.size + self.formato + self.maptype + self.marcadores+self.marcadores2+self.path+self.path2+self.api_key
        return "https://maps.googleapis.com/maps/api/staticmap?" + parametros

    def tipomapa(self, num):
        """0 - roadmap, 1 - satellite, 2 - hybrid, and 3 -terrain"""
        tipo = ["roadmap", "satellite", "hybrid", "terrain"]
        self.maptype = "&maptype=" + tipo[num]

    def set_marcadores(self, lista, lista2):
        marcas = "|"
        marcas = marcas.join(lista)
        self.marcadores = "&markers=color:green|label:M|" + marcas
        marcas2 = "|"
        marcas2 = marcas2.join(lista2)
        self.marcadores2 = "&markers=color:yellow|" + marcas2

    def set_camino(self, lista, lista2):
        marcas = "|"
        marcas = marcas.join(lista)
        self.path = "&path=color:red|weight:2|"+marcas
        marcas2 = "|"
        marcas2 = marcas2.join(lista2)
        self.path2 = "&path="+marcas2


class Principal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("prueba.ui", self)
        self.browser = QWebEngineView()
        self.browser.resize(500,500)

        m = MapaUrl()
        m.tipomapa(0)

        lista = ['argentina', 'brasil', 'cuba']
        lista2 = ['españa', 'japon', 'italia', 'rusia']

        m.set_marcadores(lista, lista2)
        m.set_camino(lista, lista2)
        url = m.get_url()
        print(url)

        self.browser.load(QUrl(url))
        self.browser.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
