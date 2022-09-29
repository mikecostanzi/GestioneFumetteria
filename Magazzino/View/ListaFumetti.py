import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
from Magazzino.Controller.GestoreFumetti import GestoreFumetti
from Magazzino.Model.Fumetto import Fumetto
from Magazzino.View.VistaFumetto import VistaFumetto
from Magazzino.View.InserimentoFumetti import InserimentoFumetti

class ListaFumetti(QWidget):

    def __init__(self, parent=None):
        super(ListaFumetti, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Magazzino")

    '''
        file = open('Magazzino/Database/Fumetti.pickle', 'wb')
        # dump information to that file
        pickle.dump(list(range(19)),file)
        # close the file
        file.close()
    '''


    def load_fumetti(self):
        # open a file, where you stored the pickled data
        file = open('Magazzino/Database/Fumetti.pickle', 'rb')

        # dump information to that file
        data = pickle.load(file)

        # close the file
        file.close()
        print(data)
        self.fumetti.extend(data)

    def update_ui(self):
        self.fumetti = []
        self.load_fumetti()
        listview_model = QStandardItemModel(self.list_view)
        for fumetto in self.fumetti:
            item = QStandardItem()
            riga = f"{fumetto.categoria} {fumetto.distributore} - {type(fumetto).__name__} {fumetto.barcode}"
            item.setText(riga)
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
            barcode = int(selected.split("-")[1].strip().split(" ")[1])
            fumetto = None
            if tipo == "Fumetto":
                fumetto = GestoreFumetti().ricercaFumetto(barcode)
            self.vista_fumetto = VistaFumetto(fumetto, elimina_callback=self.update_ui)
            self.vista_fumetto.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def show_new(self):
        self.inserisci_fumetto = InserimentoFumetti()
        self.inserisci_fumetto.show()
