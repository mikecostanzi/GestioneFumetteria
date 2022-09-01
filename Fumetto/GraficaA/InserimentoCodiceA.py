import os.path
import json

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit
from Fumetto.GraficaA.VistaFumetto import VistaFumetto
from Fumetto.Classi.FumettoAcquistabile import FumettoAcquistabile
from Fumetto.GraficaA.ClienteSelezionato import ClienteSelezionato

class InserimentoCodiceA(QWidget):

    def __init__(self, parent=None):
        super(InserimentoCodiceA, self).__init__(parent)

        self.grid_layout = QGridLayout()

        self.list_view = QListView()

        #self.update_ui()

        #self.lista_layout = QHBoxLayout()
        #self.lista_layout.addWidget(self.list_view)

        self.dato = QLabel("Digita il codice")
        self.barra_ricerca = QLineEdit()

        self.open_button = QPushButton('Apri')
        self.open_button.clicked.connect(self.show_selecteded_info)

        self.r_button = QPushButton('Avvia Ricerca')
        self.r_button.clicked.connect(self.lista)

        self.grid_layout.addWidget(self.dato, 1, 1)
        self.grid_layout.addWidget(self.barra_ricerca, 1, 2)
        self.grid_layout.addWidget(self.list_view, 2, 1)
        self.grid_layout.addWidget(self.open_button, 3, 1)
        self.grid_layout.addWidget(self.r_button, 3, 2)

        self.setLayout(self.grid_layout)
        self.resize(500, 500)
        self.setWindowTitle("Gestisci Clienti")



        """"
        buttons_layout = QVBoxLayout()
        
        buttons_layout.addWidget(open_button)

        
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)
        """

    def load_fumetti(self):
        pass
    def lista(self):
        pass
    def show_selecteded_info(self):
        self.open_cliente = ClienteSelezionato()
        self.open_cliente.show()