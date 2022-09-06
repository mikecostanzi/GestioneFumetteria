from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QGridLayout

from Noleggio.Grafica.InserimentoNoleggio import InserimentoNoleggio
from Noleggio.Grafica.RestituzioneNoleggio import RestituzioneNoleggio
from Noleggio.Grafica.RicercaNoleggio import RicercaNoleggio


class OperazioniNoleggio(QWidget):

    def __int__(self,parent=None):
        super(OperazioniNoleggio, self).__int__(parent)

        set_layout = QGridLayout()

        b = QLabel()
        b.setText("Scegli l'operazione:")
        set_layout.addWidget(b)
        set_layout.addWidget(self.generic_button("Inserisci",self.go_inserisci),1,0)
        set_layout.addWidget(self.generic_button("Restituzione",self.go_restituzione),1,1)
        set_layout.addWidget(self.generic_button("Ricerca",self.go_ricerca),1,2)

        self.setLayout(set_layout)
        self.resize(500, 500)
        self.setWindowTitle("Noleggio")

    def generic_button(self,titolo,click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(click)
        return button

    def go_inserisci(self):
        self.inserimento_noleggio = InserimentoNoleggio()
        self.inserimento_noleggio.show()


    def go_restituzione(self):
        self.restituzione_noleggio = RestituzioneNoleggio()
        self.restituzione_noleggio.show()
    def go_ricerca(self):
        self.ricerca_noleggio = RicercaNoleggio()
        self.ricerca_noleggio.show()