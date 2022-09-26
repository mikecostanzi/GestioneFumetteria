import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QHBoxLayout, QPushButton, QVBoxLayout
from Magazzino.Controller.GestoreFumetti import GestoreFumetti
from Magazzino.View.InserimentoFumetti import InserimentoFumetti
from Magazzino.View.VistaFumetto import VistaFumetto


class ListaFumetti(QWidget):

    def __int__(self, parent=None):
        super(ListaFumetti, self).__int__(parent)

        self.lista_view = QListView()
        self.update_ui()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.lista_view)

        buttons_layout = QVBoxLayout()

        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_apri)
        buttons_layout.addWidget(open_button)

        open_button2 = QPushButton('Nuovo')
        open_button2.clicked.connect(self.show_nuovo)
        buttons_layout.addWidget(open_button2)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,600)
        self.setWindowTitle("Magazzino")

    def load_fumetti(self):
        if os.path.isfile('Database/Fumetti.pickle'):
            with open('Database/Fumetti.pickle', 'rb') as f:
                current = list(pickle.load(f))
                self.fumetti.extend(current.values())

    def update_ui(self):
        self.fumetti = []
        self.load_fumetti()
        listview_model = QStandardItemModel(self.list_view)
        for fumetto in self.fumetti:
            item = QStandardItem()
            riga = f"{fumetto.categoria} {fumetto.editore} - {fumetto.barcode}"
            item.setText(riga)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(15)
            item.setFont(font)
            listview_model.appendRow(item)
        self.lista_view.setModel(listview_model)
    def show_apri(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            barcode = int(selected.split("-")[1].strip().split(" ")[1])
            fumetto = None
            if tipo == "Fumetto":
                fumetto = GestoreFumetti().ricercaFumetto(barcode)
            self.vista_fumetto = VistaFumetto(fumetto, elimina_callback=self.update_ui)
            self.vista_fumetto.show()
        except IndexError:
            print("Index Error")
            return
    def show_nuovo(self):
        self.inserimento_fumetto = InserimentoFumetti()
        self.inserimento_fumetto.show()