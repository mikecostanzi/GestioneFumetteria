import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Cliente.Controller.GestoreTessera import GestoreTessera
from Cliente.View.ViewTessera import ViewTessera
from Cliente.View.InserimentoTessera import InserimentoTessera

class OperazioniTessera(QWidget):
    def __init__(self, parent = None):
        super(OperazioniTessera, self).__init__(parent)
        ot = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        ot.addWidget(self.list_view)

        ot_btn = QVBoxLayout()
        btn_open = QPushButton('Apri')
        btn_open.clicked.connect(self.show_selected_info)
        ot_btn.addWidget(btn_open)

        btn_new = QPushButton('Nuovo')
        btn_new.clicked.connect(self.show_new)
        ot_btn.addWidget(btn_new)
        ot_btn.addStretch()
        ot.addLayout(ot_btn)

        self.setLayout(ot)
        self.resize(500, 500)
        self.setWindowTitle("Gestore Tessera")

    def load_tessere(self):
        if os.path.isfile("/Cliente/Database/Clienti.pkl"):
            with open("/Cliente/Database/Clienti.pkl", "rb") as f:
                current = pickle.load(f)
                self.tessere.extend(current)

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
            selected = self.list_view.selectedIndexes()[0].data() # Index Error
            tipo = selected.split("-")[1].strip().split(" ")[0]
            idCliente = int(selected.split("-")[1].strip().split(" ")[1])
            tessera = None
            if tipo == "Tessera":
                Tessera = GestoreTessera().ricercaTessera(idCliente)
            self.viewT = ViewTessera(tessera, elimina_callback=self.update_ui)
            self.viewT.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def show_new(self):
        self.inserimentoTessera = InserimentoTessera()
        self.inserimentoTessera.show()