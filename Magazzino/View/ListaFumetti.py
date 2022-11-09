import os.path
import pickle
import os

from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
from Magazzino.Controller.GestoreFumetti import GestoreFumetti
from Magazzino.Model.Fumetto import Fumetto
from Magazzino import Database

from Magazzino.View.VistaFumetto import VistaFumetto
from Magazzino.View.InserimentoFumetti import InserimentoFumetti


class ListaFumetti(QWidget):

    def __init__(self, parent=None):
        super(ListaFumetti, self).__init__(parent)
        self.vista_fumetto = None
        self.fumetti = []
        print('--- Inizio layout lista fumetti ---')
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()

        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Inserisci')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)
        print('--- Fine layout lista fumetti ---')
        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Magazzino")
    def load_fumetti(self):  # RICONTROLLO
        print('Inizio load')
        try:
            if os.path.isfile('../GestioneFumetteria/Magazzino/Database/Fumetti.pickle'):
                with open('../GestioneFumetteria/Magazzino/Database/Fumetti.pickle', 'rb') as f:
                    current = list(pickle.load(f))
                    self.fumetti.extend(current)
            else:
                print('\nFile not found')
        except Exception as m:
            print(m)
            print(m.args)
            print(type(m))
        print('Fine load')

    def update_ui(self):
        try:
            self.load_fumetti()
            listview_model = QStandardItemModel(self.list_view)

            print('Inizio update')
            for fumetto in self.fumetti:
                item = QStandardItem()
                riga = f"{fumetto.categoria} {fumetto.distributore} {fumetto.editore} - {fumetto.barcode}"
                print(riga)
                # nome = QStringListModel([f"{fumetto.categoria}"])
                item.setText(riga)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                listview_model.appendRow(item)
            self.list_view.setModel(listview_model)
            print("update_ui avvenuto con successo")
        except Exception as messaggio:
            print(type(messaggio))
            print(messaggio.args)
            print(messaggio)
        print('Fine update')

    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            barcode_selezionato = int(selected.split("-")[1].strip().split(" ")[0])
            print('barcode selezionato:')
            print(barcode_selezionato)

            fumetto_ricercato = GestoreFumetti()
            f = fumetto_ricercato.ricerca_fumetto(barcode_selezionato)
            self.vista_fumetto = VistaFumetto(f,call_back = self.update_ui)
            self.vista_fumetto.show()
            print("show_selected avvenuto con successo")
        except Exception as messaggio:
            print(type(messaggio))
            print(messaggio.args)
            print(messaggio)
            return

    def show_new(self):
        self.inserisci_fumetto = InserimentoFumetti()
        self.inserisci_fumetto.show()
