import os.path
import pickle
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
from Magazzino.Controller.GestoreFumetti import GestoreFumetti
from Magazzino.Model.Fumetto import Fumetto
from Magazzino.View.VistaFumetto import VistaFumetto
from Magazzino.View.InserimentoFumetti import InserimentoFumetti

class ListaFumetti(QWidget):

    def __init__(self, parent=None):
        super(ListaFumetti, self).__init__(parent)
        self.fumetti = []
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
        if os.path.isfile(os.getcwd()+'\\..\\Magazzino\\Database\\Fumetti.pickle'):
            file = open(os.getcwd()+'\\..\\Magazzino\\Database\\Fumetti.pickle', 'rb')

            # dump information to that file
            data = pickle.load(file)
            print(data)
            self.fumetti.extend(data)
            print("Load avvenuto con successo")
        # close the file
        # file.close()
        '''''
        with open(os.getcwd()+'\\..\\Magazzino\\Database\\Fumetti.pickle', 'rb') as f:
            data = pickle.load(f)
        '''''




    def update_ui(self):
        self.load_fumetti()
        listview_model = QStandardItemModel(self.list_view)
        for fumetto in self.fumetti:
            item = QStandardItem()
            print("funziona1")
            riga = f"{fumetto.categoria} {fumetto.distributore} - {fumetto.barcode}"
            print("funziona2")
            item.setText(riga)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)
        print("update_ui avvenuto con successo")

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
            print("show_selected avvenuto con successo")
        except IndexError:
            print("INDEX ERROR")
            return

    def show_new(self):
        self.inserisci_fumetto = InserimentoFumetti()
        self.inserisci_fumetto.show()
