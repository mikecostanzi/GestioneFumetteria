import os.path
import json

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit
from Fumetto.GraficaA.VistaFumetto import VistaFumetto
from Fumetto.Classi.FumettoAcquistabile import FumettoAcquistabile

class InserimentoCodiceA(QWidget):

    def __init__(self, parent=None):
        super(InserimentoCodiceA, self).__init__(parent)

        self.grid_layout = QGridLayout()
        self.dato = QLabel("Digita il codice")

        self.grid_layout.addWidget(self.dato, 1, 1)

        self.grid_layout.setLayout(self.grid_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Clienti")

    def load_fumetti(self):
        pass