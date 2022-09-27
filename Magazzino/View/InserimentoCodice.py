import os.path
import json

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QPushButton, QGridLayout, QLabel, QLineEdit
from Magazzino.View.ClienteSelezionato import ClienteSelezionato


class InserimentoCodiceA(QWidget):

    def __init__(self, parent=None):
        super(InserimentoCodiceA, self).__init__(parent)

        self.grid_layout = QGridLayout()
        self.list_view = QListView()

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

    def load_fumetti(self):
        if os.path.isfile('Magazzino/Database/Fumetti.pickle'):
            with open('Magazzino/Database/Fumetti.pickle', 'r') as f:
                current = dict(json.load(f))
                self.fumetti.extend(current.values())


    def lista(self):
        self.fumetti = []
        self.load_fumetti()
        #self.ricerca = GestoreFumettiA()
        #self.ricerca.ricercaFumettoA(self.barra_ricerca)
        lista_model = QStandardItemModel(self.list_view)
        for fumetto in self.fumetti:
            item = QStandardItem()
            riga = f"{fumetto.barcodeA} {fumetto.categoria} {fumetto.collana} {fumetto.sottocollana}"
            item.setText(riga)
            item.setEditable(False)
            item.setFont(item.font().setPointSize(18))
            lista_model.appendRow(item)
        self.list_view.setModel(lista_model)



    def show_selecteded_info(self):
        self.open_cliente = ClienteSelezionato()
        self.open_cliente.show()