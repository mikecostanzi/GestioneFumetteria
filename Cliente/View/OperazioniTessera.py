import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Cliente.View.ViewTessera import ViewTessera
from Cliente.View.InserimentoTessera import InserimentoTessera

from Cliente.Model.Tessera import Tessera


class OperazioniTessera(QWidget):

    def __init__(self, parent=None):
        super(OperazioniTessera, self).__init__(parent)
        t = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        t.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()

        t.addLayout(buttons_layout)

        self.setLayout(t)
        self.resize(500, 500)
        self.setWindowTitle("Operazioni Tessera")

    def load_tessere(self):
        if os.path.isfile('Cliente/Database/Clienti.pickle'):
            with open('Cliente/Database/Clienti.pickle', 'at') as f:
                current = list(pickle.load(f))
                self.tessere.extend(current.values())
        else:
            print("Nicola sempre colpa tua")

    def update_ui(self):
        self.tessere = []
        self.load_tessere()
        listview_model = QStandardItemModel(self.list_view)
        for tessera in self.tessere:
            item = QStandardItem()
            nome = f"{tessera.nome} {tessera.cognome} - {type(tessera).__name__} {tessera.idCliente}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            tessera = None
            if tipo == "Tessera":
                tessera = Tessera().ricercaUtilizzatoreCodice(codice)
            self.view_tessera = ViewTessera(tessera, elimina_callback=self.update_ui)
            self.view_tessera.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def show_new(self):
        self.inserisci_tessera = InserimentoTessera(callback=self.update_ui)
        self.inserisci_tessera.show()
