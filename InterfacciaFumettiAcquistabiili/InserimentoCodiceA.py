from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QSizePolicy, QGridLayout

from InterfacciaFumettiAcquistabiili.ModificaA import ModificaA
from InterfacciaFumettiAcquistabiili.EliminaA import EliminaA

class InserimentoCodiceA(QWidget):

    def __int__(self,parent=None):
        super(InserimentoCodiceA, self).__init__(parent)

        grid_layout = QGridLayout()
        testo_opzione = QLabel()
        testo_opzione.setText("Inserisci il codice a barre")
        grid_layout.addWidget(testo_opzione)
        barcodeC = QLabel()
        grid_layout.addWidget(barcodeC, 1, 0)
        grid_layout.addWidget(self.inserimento_codice(), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Modifica", self.go_modifica()), 2, 0)
        grid_layout.addWidget(self.get_generic_button("Elimina", self.go_elimina()), 2, 1)

        self.setLayout(grid_layout)
        self.resize(500, 500)
        self.setWindowTitle("Inserimento Bar-Code")

    def inserimento_codice(self):
        codice = self.qlines["barcodeA"].text()
        return codice

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_modifica(self):
        self.modifica = ModificaA()
        self.modifica.show()
        pass

    def go_elimina(self):
        self.elimina = EliminaA(a)
        self.elimina.show()
        pass

