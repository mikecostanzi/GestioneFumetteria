from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QHBoxLayout

from Noleggio.Grafica.InserimentoNoleggio import InserimentoNoleggio
from Noleggio.Grafica.RestituzioneNoleggio import RestituzioneNoleggio
from Noleggio.Grafica.RicercaNoleggio import RicercaNoleggio



class OperazioniNoleggio(QWidget):

    def __init__(self, parent=None):
        super(OperazioniNoleggio, self).__init__(parent)
        l = QHBoxLayout()
        """""
        b = QLabel()
        b.setText("Scegli l'operazione:")
        l.addWidget(b)
        """""
        l.addWidget(self.generic_button("Inserimento", self.go_inserimento))
        l.addWidget(self.generic_button("Restituzione", self.go_restituzione))
        l.addWidget(self.generic_button("Ricerca", self.go_ricerca))

        self.setLayout(l)
        self.resize(300, 300)
        self.setWindowTitle("Scegli l'operazione:")

    def generic_button(self, titolo, click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(click)
        return button
    def go_ricerca(self):
        self.ricerca_noleggio = RicercaNoleggio()
        self.ricerca_noleggio.show()

    def go_restituzione(self):
        self.restituzione_noleggio = RestituzioneNoleggio()
        self.restituzione_noleggio.show()

    def go_inserimento(self):
        self.inserimento_noleggio = InserimentoNoleggio()
        self.inserimento_noleggio.show()
